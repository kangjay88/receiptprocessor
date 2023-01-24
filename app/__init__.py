from flask import Flask
from config import Config
from .receipts.receipts import receipts  # registering a blueprint

app = Flask(__name__)
app.register_blueprint(receipts)

app.config.from_object(Config)