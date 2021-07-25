from flask import Flask
from teams import teams
app = Flask(__name__)

app.register_blueprint(blueprint=teams)
if __name__ == "__main__":
    app.run()