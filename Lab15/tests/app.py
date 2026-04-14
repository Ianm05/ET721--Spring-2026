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
    return jsonify(items), 200


# READ SINGLE ITEM + UPDATE
@app.route('/items/<item_id>', methods=['GET', 'PUT'])
def handle_item(item_id):
    item = items.get(item_id)

    # GET request
    if request.method == 'GET':
        if not item:
            return jsonify({'error': "Item not found"}), 404
        return jsonify(item), 200

    # PUT request
    elif request.method == 'PUT':
        if not item:
            return jsonify({'error': "Item not found"}), 404

        data = request.get_json()
        items[item_id] = data

        return jsonify({'id': item_id, 'item': data}), 200


# ✅ DELETE route (separate and clean)
@app.route('/items/<item_id>', methods=['DELETE'])
def delete_item(item_id):
    if item_id not in items:
        return jsonify({'error': 'Item not found'}), 404

    del items[item_id]

    return jsonify({'message': 'Item deleted'}), 200

# At the bottom of app.py, add this route (for testing only)
@app.route('/reset', methods=['POST'])
def reset():
    items.clear()
    return '', 204


if __name__ == '__main__':
    app.run(debug=True)