from flask import Flask, jsonify, request
import yaml
app = Flask(__name__)


def yamlify(data, status=200, headers=None):
    _headers = {"Content-Type" : "application/x-yaml"}
    if headers is not None:
        _headers.update(headers)
    return yaml.safe_dump(data), status, _headers

@app.route("/api")
def my_microservice():
    return yamlify(["hello", "yaml", "world"])


if __name__ == "__main__":
    app.run()