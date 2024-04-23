from flask import Flask
import mysql.connector

app = Flask(__name__)


# З'єднання з базою даних MySQL
def connect_to_mysql():
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password=' ',
            database='plants_profile_create'
        )
        print("Connected to MySQL database")
        return connection
    except mysql.connector.Error as error:
        print("Failed to connect to MySQL database:", error)
        return None


# Маршрут Flask, який використовує з'єднання з базою даних
@app.route('/')
def forum():
    connection = connect_to_mysql()
    if connection:
        # Виконайте SQL-запит тут
        # Наприклад, можна витягнути дані з таблиці і повернути їх у відповідь клієнту
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM plants_info")
        data = cursor.fetchall()
        connection.close()
        return str(data)
    else:
        return "Failed to connect to MySQL database"


if __name__ == '__main__':
    app.run(debug=True)
