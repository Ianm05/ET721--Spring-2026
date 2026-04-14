from flask import Flask, render_template, request, jsonify
import mysql.connecter

app = Flask(__name__)

#-----------------------------
# Database config
#-----------------------------
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'flaskuser'
app.config['MYSQL_PASSWORD'] = 'password123'
app.config['MYSQL_DB'] = 'todo_db'

db = mysql.connector.connect(
    host= app.config['MYSQL_HOST'],
    user = app.config['MYSQL_USER'],
    password = app.config['MYSQL_PASSWORD'],
    database = app.config['MYSQL_DB']
)

#-----------------------------
# Home route
#----------------------------- 
@app.route('/')
def index():
    return render_template('index.html')

#-----------------------------
# get all task
#------------------------------
@app.route('/tasks', methods=['GET'])
def get_tasks():
    try:
        with db.cursor(dictionary = True) as cursor:
            cursor.execute("SELECT * FROM tasks")
            tasks = cursor.fetchall()
            return jsonify(tasks)
    except mysql.connector.Error as e:
        return jsonify({'error': str(e)}), 500
    
    #--------------------------------
    # add new task
    #-------------------------------
@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    task = data.get('task')

    if task:
        cursor = db.cursor()
        cursor.execute("INSERT INTO tasks (task) VALUES (%s)", (task,))
        db.commit()
        cursor.close()
        return jsonify({'status': 'success'}), 201
    return jsonify({'status': 'error', 'message': 'Invalid task data'}), 400

#-----------------------------
# run app
#-----------------------------
if __name__ == '__main__':
    app.run(debug=True)