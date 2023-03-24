# from peewee import *
import mysql.connector
from mysql.connector import Error
from config import DB_NAME, USER, PASSWORD, HOST


# db = MySQLDatabase(DB_NAME, user=USER, port=3306, password=PASSWORD, host=HOST)
# print(db.connection())
#
#
# class BaseModel(Model):
#     id = PrimaryKeyField(unique=True)
#
#     class Meta:
#         database = db
#         order_by = 'id'
#
#
# class User(BaseModel):
#     id_telegram = IntegerField(unique=True)
#     first_name = CharField
#     last_name = CharField
#
#     class Meta:
#         db_table = 'Users'
#
#
# class Request(BaseModel):
#     id_telegram = IntegerField
#     date = DateField
#     request = CharField
#     result = TextField
#
#     class Meta:
#         db_table = 'Requests'

def create_connection_mysql_db(db_host, user, password, db_name: str = None) -> mysql.connector.connection:
    connection_db = None
    try:
        connection_db = mysql.connector.connect(
            host=db_host,
            port=3306,
            user=user,
            password=password,
            database=db_name
        )
        print("Successfully connected")
    except Error as db_connection_error:
        print("Connection error", db_connection_error)
    return connection_db


def create_db(connection: mysql.connector.connect, db_name: str):
    with connection.cursor() as cursor:
        create_db_sql_query = f"CREATE DATABASE IF NOT EXISTS {db_name}"
        try:
            cursor.execute(create_db_sql_query)
            print("Database created successfully")
        except Error as db_creation_error:
            print(f"The error '{db_creation_error}' occurred")


def create_table_users(connection: mysql.connector.connect):
    with connection.cursor() as cursor:
        create_table_user_sql_query = "CREATE TABLE IF NOT EXISTS Users (Telegram_ID INT NOT NULL," \
                                      "First_name VARCHAR(30)," \
                                      "Last_name VARCHAR(30)," \
                                      "PRIMARY KEY (Telegram_ID)" \
                                      ")"
        try:
            cursor.execute(create_table_user_sql_query)
            print("Table 'Users' created successfully")
        except Error as db_creation_error:
            print(f"The error '{db_creation_error}' occurred")


def create_table_requests(connection: mysql.connector.connect):
    with connection.cursor() as cursor:
        create_table_requests_sql_query = "CREATE TABLE IF NOT EXISTS Requests (id INT NOT NULL AUTO_INCREMENT," \
                                          "Request TEXT," \
                                          "Response TEXT," \
                                          "Telegram_ID INT," \
                                          "PRIMARY KEY (id)," \
                                          "FOREIGN KEY (Telegram_ID) REFERENCES Users (Telegram_ID)" \
                                          ")"
        try:
            cursor.execute(create_table_requests_sql_query)
            print("Table 'Requests' created successfully")
        except Error as db_creation_error:
            print(f"The error '{db_creation_error}' occurred")


def insert_info(connection: mysql.connector.connect,
                telegram_id: int, first_name: str, last_name: str,
                request: str, response: str):
    with connection.cursor() as cursor:
        insert_info_user_sql_query = "INSERT INTO Users" \
                                     "(Telegram_ID, First_name, Last_name)" \
                                     "VALUES" \
                                     f"('{telegram_id}', '{first_name}', '{last_name}')"
        try:
            cursor.execute(insert_info_user_sql_query)
            connection.commit()
            print(f"User {first_name} {last_name} ({telegram_id}) successfully added")
        except Error as db_creation_error:
            print(f"The error '{db_creation_error}' occurred")

        insert_info_request_sql_query = "INSERT INTO Requests" \
                                        "(Request, Response, Telegram_ID)" \
                                        "VALUES" \
                                        f"('{request}', '{response}', '{telegram_id}')"
        try:
            cursor.execute(insert_info_request_sql_query)
            connection.commit()
            print(f"User ({telegram_id}) request successfully added")
        except Error as db_creation_error:
            print(f"The error '{db_creation_error}' occurred")



