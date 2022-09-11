FROM postgres:latest

ENV POSTGRES_PASSWORD=secret

ENV POSTGRES_USER=bots

ENV POSTGRES_DB=bots

COPY initdb.sql /docker-entrypoint-initdb.d/initdb.sql