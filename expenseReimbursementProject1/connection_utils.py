import os
from psycopg2._psycopg import OperationalError
from psycopg2 import connect


def create_connection():
    try:
        conn = connect(
            host=os.environ.get('HOST') or "basdb.cljyge3jembp.us-east-2.rds.amazonaws.com",  # 'basdb.cljyge3jembp.us-east-2.rds.amazonaws.com',
            database=os.environ.get('DB_NAME') or "postgres",  # 'postgres',
            user=os.environ.get('DB_USERNAME') or "postgres",  # postgres',
            password=os.environ.get('DB_PASSWORD') or "Bas12345",  # Bas12345',
            port=os.environ.get('PORT') or "5432",  # '5432'
        )
        return conn

    except OperationalError as e:

        print(e)


connection = create_connection()