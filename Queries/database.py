import json
import os

import mysql.connector


def connect_to_database():
    with open('Queries/config.json', 'r') as f:
        db_config = json.load(f)

    db_config = db_config['database']
    return mysql.connector.connect(
        host=db_config['host'],
        user=db_config['user'],
        password=db_config['password'],
        database=db_config['database']
    )


def close_connection(connection):
    connection.close()


def execute_query(connection, query, data=None):
    cursor = connection.cursor()
    if data:
        cursor.execute(query, data)
    else:
        cursor.execute(query)
    connection.commit()
    affected_rows = cursor.rowcount
    cursor.close()
    return affected_rows


def execute_and_fetch_query(connection, query, data=None):
    cursor = connection.cursor()
    if data:
        cursor.execute(query, data)
    else:
        cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return [row[0] for row in result]
