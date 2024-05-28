import pypyodbc as odbc
import pandas as pd

server = 'interactive-plant-care-assistant.database.windows.net'
database = 'InteractivePlantCareAssistant'
connection_string = 'Driver={ODBC Driver 18 for SQL Server};Server=tcp:interactive-plant-care-assistant.database.windows.net,1433;Database=InteractivePlantCareAssistant;Uid=dariia;Pwd={idkJingYuan1};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'
conn = odbc.connect(connection_string)


# Функція для вставки даних у таблицю feedback
def insert_feedback(name, email, message):

    # SQL запит для вставки даних
    sql = "INSERT INTO feedback (name, email, message) VALUES (?, ?, ?);"

    # Виконання SQL запиту з використанням параметрів для уникнення SQL ін'єкцій
    cursor = conn.cursor()
    cursor.execute(sql, (name, email, message))

    # Збереження змін до бази даних
    conn.commit()

    # Закриття з'єднання
    cursor.close()
    conn.close()


# Код для тестування функції
if __name__ == "__main__":
    # Припустимо, що дані форми передаються як аргументи функції
    name = "surname"
    email = "user@example.com"
    message = "this is text message."

    # Вставка даних у таблицю feedback
    insert_feedback(name, email, message)
