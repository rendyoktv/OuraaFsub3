FROM postgres:latest

ENV POSTGRES_PASSWORD=password

ENV POSTGRES_USER=docker

ENV POSTGRES_DB=docker

COPY initdb.sql /docker-entrypoint-initdb.d/initdb.sql