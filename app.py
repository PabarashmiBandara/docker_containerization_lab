from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    # Insert your actual university student ID below
    return jsonify({
        "student_id": "245011N", 
        "name": "Pabarashmi Bandara",
        "message": "My containerized API is running!"
    })

@app.route('/health')
def health():
    return jsonify({"status": "ok"})

if __name__ == '__main__':
    # Binding to 0.0.0.0 allows the container to expose the app to the host
    app.run(host='0.0.0.0', port=5000)