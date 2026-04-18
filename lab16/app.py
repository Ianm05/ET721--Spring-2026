from flask import Flask, render_template, request, jsonify
import mysql.connector  
app = Flask(__name__)

#-----------------------------
# Database config
#-----------------------------
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'flaskuser'
app.config['MYSQL_PASSWORD'] = 'password123'
app.config['MYSQL_DB'] = 'todo_db'

db = mysql.connector.connect(
    host=app.config['MYSQL_HOST'],
    user=app.config['MYSQL_USER'],
    password=app.config['MYSQL_PASSWORD'],
    database=app.config['MYSQL_DB']
)

#-----------------------------
# Home route
#-----------------------------
@app.route('/')
def index():
    return render_template('index.html')

#-----------------------------
# Get all tasks
#-----------------------------
#-----------------------------
# Get all tasks
#-----------------------------
@app.route('/tasks', methods=['GET'])
def get_tasks():
    try:
        db.reconnect(attempts=3, delay=1)  
        with db.cursor(dictionary=True) as cursor:
            cursor.execute("SELECT * FROM tasks")
            tasks = cursor.fetchall()
            return jsonify(tasks)
    except mysql.connector.Error as e:
        return jsonify({'error': str(e)}), 500

#-----------------------------
# Add  a new task
#-----------------------------
#-----------------------------
# Add a new task
#-----------------------------
@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    task = data.get('task')

    if task:
        db.reconnect(attempts=3, delay=1)  
        cursor = db.cursor()
        cursor.execute("INSERT INTO tasks (task) VALUES (%s)", (task,))
        db.commit()
        cursor.close()
        return jsonify({'status': 'success'}), 201
    return jsonify({'status': 'error', 'message': 'Invalid task data'}), 400

#-----------------------------
# Delete a task
#-----------------------------
@app.route('/delete_task', methods=['POST'])
@app.route('/delete_task', methods=['POST'])
def delete_task():
    data = request.get_json()
    task_id = data.get('id')

    if not task_id:
        return jsonify({'status': 'error', 'message': 'No ID provided'}), 400

    db.reconnect(attempts=3, delay=1)  
    cursor = db.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
    db.commit()
    cursor.close()

    return jsonify({'status': 'deleted'})
#-----------------------------
# Run app
#-----------------------------
if __name__ == '__main__':
    app.run(debug=True)