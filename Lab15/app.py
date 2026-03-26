"""
Ian Martinez
March 24, 2026
lab15: Restful API and Unit test in a Flask app
"""
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# in-memory database (dictionary)
items = {}

@app.route('/')
def home():
    return render_template('index.html')


# CREATE an item
@app.route('/items', methods=['POST'])
def create_item():
    data = request.get_json()

    item_id = str(len(items) + 1)
    items[item_id] = data

    return jsonify({'id': item_id, 'item': data}), 201


# READ ALL ITEMS
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items), 200   # ✅ fixed missing status


# READ SINGLE ITEM ,UPDATE + DELETE
@app.route('/items/<item_id>', methods=['GET', 'PUT', 'DELETE'])
def get_oneitem(item_id):
    item = items.get(item_id)

    
    if request.method == 'GET':
        if not item:
            return jsonify({'error': "Item not found"}), 404
        return jsonify(item), 200

    # PUT request
    elif request.method == 'PUT':
        if not item:
            return jsonify({'error': "Item not found"}), 404

        data = request.get_json()
        if not data:
            return jsonify({'error' :  'Invalid input'}), 400
        
        item[item_id] = data 
        return render_template('update.html', item_id = item_id, item = data)
    
    # DELETE
    elif request.method == "DELETE":
        item[item_id] = data
        deleted_item = item.pop(item_id)
        return render_template('delete.html' , item_id = item_id ,  item = data)
    

if __name__ == '__main__':
    app.run(debug=True)