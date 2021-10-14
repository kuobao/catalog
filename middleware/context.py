
import os

# This is a bad place for this import
import pymysql

def get_db_info():
    """
    This is crappy code.

    :return: A dictionary with connect info for MySQL
    """

    db_info = {
        "host": "e6156-rds.clboe01dd0s5.us-east-2.rds.amazonaws.com",
        "user": "root",
        "password": "rootroot",
        "cursorclass": pymysql.cursors.DictCursor
    }

    return db_info
