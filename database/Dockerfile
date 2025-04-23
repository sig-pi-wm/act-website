FROM mysql:latest

# Copy all schema-builder SQL scripts into the MySQL init directory
COPY schema-builder/*.sql /docker-entrypoint-initdb.d/

