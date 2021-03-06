from flask import Flask, request, jsonify,g

app = Flask(__name__)

@app.before_request
def authenticate():
    if request.authorization:
        g.user = request.authorization["username"]
    else:
        g.user = "Anonymous"


@app.route("/api")
def my_microservice():
    return jsonify({"hello" : g.user})


if __name__ == "__main__":
    app.run()