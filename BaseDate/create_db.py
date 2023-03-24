from config import DB_NAME, USER, PASSWORD, HOST
from BaseDate.my_db import create_connection_mysql_db, create_db, create_table_users, create_table_requests


with create_connection_mysql_db(HOST, USER, PASSWORD) as connection:
    create_db(connection=connection, db_name=DB_NAME)


with create_connection_mysql_db(HOST, USER, PASSWORD, DB_NAME) as connection:
    create_table_users(connection=connection)
    create_table_requests(connection=connection)
