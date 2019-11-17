import requests
import json
import traceback

from keycloak_config import KeycloakConfig

kc = KeycloakConfig()


class Keycloak:

    @classmethod
    def keycloak_post(cls, endpoint, data):
        url = kc.KEYCLOAK_URI + 'admin/realms/' + kc.KEYCLOAK_REALM + endpoint
        headers = cls.get_keycloak_headers()
        response = requests.post(url, headers=headers, json=data)
        if response.status_code >= 300:
            # app.logger.error(response.text)
            raise KeycloakAdminError(response)
        return response

    @classmethod
    def get_keycloak_headers(cls):
        return {
            'Authorization': 'Bearer ' + cls.get_keycloak_access_token(),
            'Content-Type': 'application/json'
        }

    @classmethod
    def get_keycloak_access_token(cls):
        data = {
            'grant_type': 'password',
            'client_id': 'admin-cli',
            'username': kc.KEYCLOAK_ADMIN_USER,
            'password': kc.KEYCLOAK_ADMIN_PASS
        }

        url = kc.KEYCLOAK_URI + 'realms/' + kc.KEYCLOAK_MASTER_REALM + '/protocol/openid-connect/token'

        response = requests.post(url, data=data)
        if response.status_code != requests.codes.ok:
            raise KeycloakAdminError(response)
        data = response.json()
        return data.get('access_token')

    @classmethod
    def keycloak_user_login(cls, body):
        for field in ['username', 'password']:
            if field not in body:
                return {'Field {} is missing!'.format(field)}, 400

        data = {
            'grant_type': 'password',
            'client_id': kc.KEYCLOAK_CLIENT_ID,
            'client_secret': kc.KEYCLOAK_CLIENT_SECRET,
            'username': body['username'],
            'password': body['password']
        }

        url = ''.join([
            kc.KEYCLOAK_URI,
            'realms/',
            kc.KEYCLOAK_REALM,
            '/protocol/openid-connect/token'
        ])

        response = requests.post(url, data=data)

        if response.status_code > 200:
            message = "Error on username/password"
            return {'message': message}, 400

        tokens_data = response.json()

        # ret = {
        #     'tokens': {"access_token": tokens_data['access_token'],
        #                "refresh_token": tokens_data['refresh_token'], }
        # }

        return {"access_token": tokens_data['access_token'],
                "refresh_token": tokens_data['refresh_token'], }, 200


class KeycloakAdminError(Exception):
    message = 'Keycloak error'

    def __init__(self, response, message=None):
        if message is not None:
            self.message = message
        # Call the base class constructor with the parameters it needs
        super().__init__(self.message)
        # Now for your custom code...
        self.response = response

    @staticmethod
    def traceback(self):
        return traceback.format_exc()

    def __str__(self):
        return json.dumps({
            'message': self.message,
            'status_code': self.response.status_code,
            'text': self.response.text
        })