FROM python:3.8
RUN pip install pipenv
WORKDIR /usr/src/app
COPY Pipfile ./
COPY Pipfile.lock ./
RUN pipenv install
COPY . .
RUN pwd
RUN ls
CMD ["pipenv", "run", "python", "app.py" ]