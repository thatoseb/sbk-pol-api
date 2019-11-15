from os import environ as env
from dotenv import load_dotenv, find_dotenv

ENV_FILE = find_dotenv()

if ENV_FILE:
    load_dotenv(ENV_FILE)


class KeycloakConfig:

    KEYCLOAK_CLIENT_ID = env.get('KEYCLOAK_CLIENT_ID')
    KEYCLOAK_CLIENT_SECRET = env.get('KEYCLOAK_CLIENT_SECRET')
    KEYCLOAK_URI = env.get('KEYCLOAK_URI')
    KEYCLOAK_REALM = env.get('KEYCLOAK_REALM')
    KEYCLOAK_MASTER_REALM = env.get('KEYCLOAK_MASTER_REALM')
    KEYCLOAK_ADMIN_USER = env.get('KEYCLOAK_ADMIN_USER')
    KEYCLOAK_ADMIN_PASS = env.get('KEYCLOAK_ADMIN_PASS')
