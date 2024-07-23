import random
import subprocess
from paho.mqtt import client as mqtt_client


broker = 'broker.emqx.io'
port = 1883
topic = "/SIC5/S.A.F.E/test/response"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 100)}'
username = 'emqx'
password = 'public'


def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(mqtt_client.CallbackAPIVersion.VERSION1, client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def run_yolov5():
    command = [
        'python', './detect.py',
        '--weights', 'yolov5s.pt',
        '--source', '0'
    ]
    subprocess.run(command)

def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

        string_msg = msg.payload.decode()

        if "Sukses" in string_msg:
            run_yolov5()

    client.subscribe(topic)
    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    run()