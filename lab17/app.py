import os
from flask import Flask, render_template, request, jsonify
import mysql.connector
from werkzeug.utils import secure_filename

app = Flask(__name__)

#------------------
# configuration
#------------------
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

#-----------------------------------------------
# MYSQL CONNECTION
#-----------------------------------------------
db_config = {
    'host': 'localhost',
    'user': 'flaskuser',
    'password': 'password123',
    'database': 'image_app'
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

#-----------------------------------------------
# LOADING PAGE
#-----------------------------------------------
@app.route('/')
def index():
    Conn = get_db_connection()
    cursor = Conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM images ORDER BY uploaded_at DESC")
    images = cursor.fetchall()
    cursor.close()
    Conn.close()
    return render_template('index.html', images = images)

#-----------------------------------------------
# UPLOAD IMAGE
#-----------------------------------------------
@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # Save image info to database
        Conn = get_db_connection()
        cursor = Conn.cursor()
        cursor.execute("INSERT INTO images (filename) VALUES (%s)", (filename,))
        Conn.commit()
        cursor.close()
        Conn.close()

        return jsonify({'message': 'Image uploaded successfully'}) 
    else:
        return jsonify({'error': 'Invalid file type'}), 400

# -----------------------------------------------
# RUN APP
# -----------------------------------------------
if __name__ == '__main__':
    app.run(debug=True)

