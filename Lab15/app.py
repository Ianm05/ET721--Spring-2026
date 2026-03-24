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
    return jsonify(items),

# READ SINGLE ITEM
@app.route('/items/<item_id>', methods= ['GET'])
def get_oneitem(item_id):
    item = items.get(item_id)
    if not item:
        # 404 = serve is reachable but the item you asked for doesn't exist
        return jsonify({'Error':"Item not found"}), 404
    
    return jsonify(item)


if __name__ == '__main__':
    app.run(debug=True)