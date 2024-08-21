from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, World!"


# Define additional routes here
@app.route('/api/data', methods=['GET'])
def get_data():
    # Example of a route that returns JSON data
    return jsonify({"message": "Hello from the API!"})


if __name__ == '__main__':
    app.run(debug=True)
