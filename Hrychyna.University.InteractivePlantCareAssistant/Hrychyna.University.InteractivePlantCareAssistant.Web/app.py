from flask import Flask, request, jsonify, render_template
from flask_mysqldb import MySQL
import json

app = Flask(__name__)

# Конфігурація доступу до MySQL
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'forumdb'

mysql = MySQL(app)


@app.route('/')
def forum():
    return render_template('forum.html')


@app.route('/threads', methods=['GET', 'POST'])
def threads():
    if request.method == 'POST':
        # Додавання нової теми
        details = request.json
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO threads(title) VALUES (%s)", [details['title']])
        mysql.connection.commit()
        cursor.close()
        return jsonify({'status': 'success', 'message': 'Thread added'}), 201

    elif request.method == 'GET':
        # Отримання всіх тем
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM threads")
        threads = cursor.fetchall()
        cursor.close()
        return jsonify(threads)


@app.route('/threads/<int:id>/messages', methods=['GET', 'POST'])
def messages(id):
    if request.method == 'POST':
        # Додавання нового повідомлення до теми
        details = request.json
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO messages(thread_id, content) VALUES (%s, %s)", (id, details['content']))
        mysql.connection.commit()
        cursor.close()
        return jsonify({'status': 'success', 'message': 'Message added'}), 201

    elif request.method == 'GET':
        # Отримання повідомлень теми
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM messages WHERE thread_id = %s", [id])
        messages = cursor.fetchall()
        cursor.close()
        return jsonify(messages)


if __name__ == '__main__':
    app.run(debug=True)
