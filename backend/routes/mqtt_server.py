from flask_mqtt import Mqtt
import json
from routes import logs,employees
from datetime import datetime
mqtt = Mqtt()


@mqtt.on_connect()
def on_connect(client, userdata, flags, rc):
    mqtt.subscribe('my_topic')  # Subscribe to the MQTT topic
    print("connected to topic")

@mqtt.on_message()
def on_message(client, userdata, message):
    msg = json.loads(message.payload.decode())
    print(msg)
    print("Received message:",msg["action"])
    if msg["action"] == "Login Pin":
        employee = employees.find_one({"password": msg["pass"]})
        try:
            logs.insert_one({"action": "Logged in", "name":employee['name'],'at':datetime.utcnow()})
        except:
            print('No such user')
    elif msg["action"] == "Logout Pin":
        employee = employees.find_one({"password": msg["pass"]})
        try:
            logs.insert_one({"action": "Logged out", "name":employee['name'],'at':datetime.utcnow()})
        except:
            print('No such user')
    elif msg["action"] == "Unauthorized Login":
        logs.insert_one({"action": "Unauthorized Login", "name":"",'at':datetime.utcnow()})
