from flask import Flask, request, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from threading import Thread
from price_monitor import monitor_price

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://sagar:1204@5432/btc_price_alert'
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
jwt = JWTManager(app)


@app.route('/')
def home():
    return app.send_static_file('index.html')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(app.static_folder, 'favicon.ico')




@app.route('/set_alert', methods=['POST'])
def set_alert():
    data = request.json
    crypto = data['crypto']
    target_price = data['target_price']
    email = data['email']
    Thread(target=monitor_price, args=(crypto, target_price, email)).start()
    return "Alert set successfully!"

# Import routes from other modules if necessary
# from routes import *

if __name__ == '__main__':
    app.run(debug=True)
