from flask import Flask, jsonify
from flask_cors import CORS
import socket
from common.config import ProductionConfig, DevelopmentConfig



print(socket.gethostname())

app = Flask(__name__)

app.config.from_object(ProductionConfig)

print(app.config)

if __name__ == "__main__":
    app.run(host=app.config.get("SERVER_IP"), port=app.config.get("SERVER_PORT"))