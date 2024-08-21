import os
import subprocess
from flask import Flask, request, jsonify, send_from_directory
from waitress import serve

app = Flask(__name__)

EXECUTABLE_PATH = os.path.join(os.path.dirname(__file__), 'bin', 'Factor_and_Simplify_SquareRoot.exe')


@app.route('/')
def index():
    return send_from_directory('', 'index.html')  # Serve the HTML file


@app.route('/run', methods=['POST'])
def run_executable():
    try:
        # Get the number from the request data
        data = request.get_json()
        number = data.get('number', '')

        # Run the executable with the argument
        command = [EXECUTABLE_PATH, number]
        result = subprocess.run(command, capture_output=True, text=True, encoding='utf-8')

        # Return the output from the executable
        return jsonify({'output': result.stdout, 'error': result.stderr})
    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    port = int(os.getenv('PORT', 8080))  # Use environment variable PORT or default to 8080
    serve(app, host='0.0.0.0', port=port)  # Use Waitress to serve the app
