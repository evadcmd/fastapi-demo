# fastapi-demo

a simple demo of fastapi

- python 3.8
- postgresql
- docker runable

## How to use

1. Edit the database entities in 「app/model.py」.
2. Edit the RESTful API in 「app/restapi/\*\*.py」.
3. Execute database migration.
   [TODO]
4. run & test.
   if you want, you could change the basic settings in the「config.yml」 file

## db migration

we use alembic to manage database migration.
follow the steps to manage database entities:

1. change model definitions in app/model.py
2. under root folder:

```bash
$ alembic revision --autogenerate -m '${comment about the revision}'
```

3. apply the changes to the database:

```bash
$ alembic upgrade
```

## Run & Test

### Run server (Docker)

```bash
$ docker-compose up -d --build
```

stop the container

```bash
$ docker-compose down
```
