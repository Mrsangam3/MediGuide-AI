import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()


def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )


def search_medicine(medicine_name):
    connection = None
    cursor = None

    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)

        query = """
            SELECT
                name,
                generic_name,
                category,
                common_uses,
                common_side_effects,
                precautions
            FROM medicines
            WHERE LOWER(name) = LOWER(%s)
               OR LOWER(generic_name) = LOWER(%s)
            LIMIT 1
        """

        cursor.execute(
            query,
            (medicine_name, medicine_name)
        )

        return cursor.fetchone()

    finally:
        if cursor:
            cursor.close()

        if connection:
            connection.close()


if __name__ == "__main__":
    medicine = search_medicine("Paracetamol")
    print(medicine)