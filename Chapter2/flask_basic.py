from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/api", methods=['POST', 'DELETE', 'GET'])
def my_microservice():
    return jsonify({"test" : "test"})

if __name__ == "__main__":
    app.run()

