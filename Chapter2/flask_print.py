from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/api2")
def python_msd():
    print(request)
    print("\n")
    print(request.environ)
    print("\n")

    response = jsonify({"test2": "test2"})

    print(response)
    print("\n")

    print(response.data)
    print("\n")

    return response


if __name__ == "__main__":
    app.run()