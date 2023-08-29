from flask import Flask

from os import path
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from flask_cors import CORS
cur_dir = path.abspath(path.dirname(__file__))
app = Flask(__name__)
CORS(app)
app.config['MQTT_BROKER_URL'] = '192.168.137.163'  # Replace with your MQTT broker IP or hostname
app.config['MQTT_BROKER_PORT'] = 1883  # Default MQTT port
app.config['SECRET_KEY'] = 'helloworld'
uri = "mongodb+srv://Admin:lDndxUTsB1YUQtAP@cluster0.qtbiew7.mongodb.net/?retryWrites=true&w=majority"
db = MongoClient(uri, server_api=ServerApi('1')).PokaYokeSystem #DB Name Here
employees = db['employee']
logs = db['log']
seq = db['sequence']
def create_app():
    from routes.home import home_route
    from .mqtt_server import mqtt
    app.register_blueprint(home_route)
    mqtt.init_app(app)
    app.app_context().push()    
    return app