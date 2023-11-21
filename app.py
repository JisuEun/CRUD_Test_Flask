from flask import Flask, jsonify, request, send_from_directory

app = Flask(__name__, static_folder='.')

# 간단한 메모리 데이터베이스 역할을 할 딕셔너리
items = {
    '1': {'name': 'Item 1'},
    '2': {'name': 'Item 2'}
}

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/item', methods=['POST'])
def create_item():
    request_data = request.get_json()
    new_item_id = str(max([int(id) for id in items.keys()] or [0]) + 1)
    items[new_item_id] = {'name': request_data['name']}
    return jsonify(items[new_item_id])

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

@app.route('/item/<string:id>', methods=['GET'])
def get_item(id):
    return jsonify(items[id])

@app.route('/item/<string:id>', methods=['PUT'])
def update_item(id):
    request_data = request.get_json()
    items[id]['name'] = request_data['name']
    return jsonify(items[id])

@app.route('/item/<string:id>', methods=['DELETE'])
def delete_item(id):
    del items[id]
    return jsonify({'message': 'Item deleted'})

if __name__ == '__main__':
    app.run(debug=True)