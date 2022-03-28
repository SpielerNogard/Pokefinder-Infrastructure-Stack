from flask import Flask,request, abort
import json
import paho.mqtt.client as mqtt
from logging import getLogger
TOPIC3 = "Pokefinder/answers"
BROKER_ADDRESS = "51.255.143.136"
PORT = 1883
QOS = 1
app = Flask(__name__)
logger = getLogger()

@app.route("/", methods=['POST'])
def index():
    try:
        data = json.loads(request.data)
        logger.info(f'Received Webhook from {request.remote_addr}')
        if isinstance(data, list):
            for a in data:
                client = mqtt.Client()
                client.connect(BROKER_ADDRESS, PORT)
                
                client.publish(f"MAD/{a.get('type', 'fail')}", json.dumps(a), qos=QOS)
                client.loop()
                logger.info(f"Published on: MAD/{a.get('type', 'fail')}")
        else:
            client = mqtt.Client()
            client.connect(BROKER_ADDRESS, PORT)
            logger.info("Connected to MQTT Broker: " + BROKER_ADDRESS)
            client.publish(f"MAD/{data.get('type', 'fail')}", json.dumps(data), qos=QOS)
            client.loop()
            logger.info(f"Published on: MAD/{data.get('type', 'fail')}")
        return "OK"
    except Exception as e:
        logger.error(f'{e}')
        return abort(400)


def run():
    app.run(port=5000, debug=True, host="0.0.0.0")

if __name__ == '__main__':
    run()