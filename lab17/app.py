import os
import uuid
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
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM images ORDER BY uploaded_at DESC")
        images = cursor.fetchall()
        cursor.close()
        conn.close()
    except Exception as e:
        print("DB ERROR:", e)
        images = []

    return render_template('index.html', images=images)

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
        # 🔥 Make filename unique
        filename = f"{uuid.uuid4().hex}_{secure_filename(file.filename)}"
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)

        # Save file
        file.save(filepath)

        # Save to database
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO images (filename) VALUES (%s)", (filename,))
            conn.commit()
            cursor.close()
            conn.close()
        except Exception as e:
            print("DB ERROR:", e)
            return jsonify({'error': 'Database error'}), 500

        return jsonify({
            'message': 'Image uploaded successfully',
            'filename': filename  # 👈 important for frontend
        })

    return jsonify({'error': 'Invalid file type'}), 400

#-----------------------------------------------
# DELETE AN IMAGE ROUTE
#-----------------------------------------------
@app.route('/delete/<int:image_id>', methods=['DELETE'])
def delete_image(image_id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT filename FROM images WHERE id=%s", (image_id,))
        result = cursor.fetchone()

        if result:
            filename = result[0]
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

            if os.path.exists(file_path):
                os.remove(file_path)

            cursor.execute("DELETE FROM images WHERE id=%s", (image_id,))
            conn.commit()

        cursor.close()
        conn.close()

        return jsonify({'message': 'Deleted successfully'})

    except Exception as e:
        print("DELETE ERROR:", e)
        return jsonify({'error': str(e)}), 500
#-----------------------------------------------    
# RUN APP
#-----------------------------------------------
if __name__ == '__main__':
    app.run(debug=True)