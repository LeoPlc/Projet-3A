import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe("zigbee/devices/#")  # S'abonner à tous les appareils Zigbee

def on_message(client, userdata, msg):
    print(f"Received message on topic {msg.topic}: {msg.payload.decode()}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("votre_broker_mqtt", 1883, 60)  # Remplacez par l'adresse de votre broker
client.loop_forever()
