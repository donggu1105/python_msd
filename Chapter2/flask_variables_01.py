from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/api/person/<person_id>")
def returnPerson(person_id):
    response = jsonify({"personId" : person_id})
    return response

if __name__ == "__main__":
    app.run()