FROM postgres
ENV POSTGRES_PASSWORD=somepassword
ENV POSTGRES_DB car_dealership
ENV PGDATA=/var/lib/postgresql/data/pgdata
ENV POSTGRES_HOST_AUTH_METHOD=trust
COPY create_table.sql /docker-entrypoint-initdb.d/
