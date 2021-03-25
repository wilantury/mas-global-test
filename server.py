# Flask
from flask import Flask, request
import os

# Libraries
from flask_cors import CORS
from dotenv import load_dotenv

# blueprints
from employees.employees import employees_bp

load_dotenv()

app = Flask(__name__)

app.register_blueprint(employees_bp)

cors = CORS(app, resources={r"/api/*": {"origins": os.getenv("URL_CLIENT")}})

app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
app.config["DEBUG"] = os.getenv("DEBUG")


if __name__ == "__main__":
    port = os.getenv("PORT")
    app.run(port=port)
