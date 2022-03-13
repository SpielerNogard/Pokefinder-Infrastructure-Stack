from flask import Flask,request, abort
import json
import paho.mqtt.client as mqtt
TOPIC3 = "Pokefinder/answers"
BROKER_ADDRESS = "0.0.0.0"
PORT = 1883
QOS = 1
app = Flask(__name__)


@app.route("/", methods=['POST'])
def index():
    try:
        data = json.loads(request.data)
        print(f'Received Webhook from {request.remote_addr}')
        if isinstance(data, list):
            for a in data:
                client = mqtt.Client()
                client.connect(BROKER_ADDRESS, PORT)
                
                client.publish(f"MAD/{a.get('type', 'fail')}", json.dumps(a), qos=QOS)
                client.loop()
                print(f"Published on: MAD/{a.get('type', 'fail')}")
        else:
            client = mqtt.Client()
            client.connect(BROKER_ADDRESS, PORT)
            print("Connected to MQTT Broker: " + BROKER_ADDRESS)
            client.publish(f"MAD/{data.get('type', 'fail')}", json.dumps(data), qos=QOS)
            client.loop()
            print(f"Published on: MAD/{data.get('type', 'fail')}")
        return "OK"
    except Exception as e:
        print(e)
        return abort(400)


def run():
    app.run(port=5000, debug=True, host="0.0.0.0")

if __name__ == '__main__':
    run()