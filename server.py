from flask import Flask
import os
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")

@app.route('/')
def employees():
    return 'Hello employees'

if __name__ == "__main__":
    port = os.getenv("PORT")
    environment = os.getenv("ENV") == 'True'
    app.run(port=port, debug=environment)