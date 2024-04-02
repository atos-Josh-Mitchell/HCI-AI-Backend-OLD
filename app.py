from flask import Flask, jsonify, send_from_directory
import time

app = Flask(__name__, static_folder="static", template_folder="static")

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

# Route to serve static files (e.g., JavaScript, CSS, images)
# test
@app.route('/assets/<path:filename>')
def serve_static(filename):
    return send_from_directory('static/assets', filename)

@app.route('/api')
def hello():
    return jsonify(message="Hello from Flask!")

@app.route('/time')
def get_current_time():
    return {'time': time.time()}

if __name__ == '__main__':
    app.run(debug=True)
