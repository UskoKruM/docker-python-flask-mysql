# Imports
from decouple import config
import pymysql

# Exception Handler
from src.utils.ExceptionHandler import ExceptionHandler


def get_connection() -> pymysql.connections.Connection:
    try:
        return pymysql.connect(
            host=config('MYSQL_HOST'),
            database=config('MYSQL_DATABASE'),
            user=config('MYSQL_USER'),
            password=config('MYSQL_PW')
        )
    except Exception as ex:
        ExceptionHandler.log_exception(ex)
