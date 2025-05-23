from flask import Flask, jsonify, request

app = Flask(__name__)

items = []

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

@app.route('/items', methods=['POST'])
def add_item():
    data = request.json
    items.append(data)
    return jsonify({"message": "Item added"}), 201

if __name__ == "__main__":
    app.run(debug=True)