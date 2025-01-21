import paho.mqtt.client as mqtt

# define callback functions
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker")
        client.subscribe("/testing/test01")
        client.subscribe("/linear_action/tap")
    else: print("Failed to connect, return code: ", rc)

def on_message(client, userdata, msg):
    print(f"Received message: {msg.payload.decode()} on topic {msg.topic}")
    if msg.topic == "/linear_action/tap":
        if msg.payload.decode() == "5mm_tap_single": print("Tapping once... (placeholder)")
# Create a client instance
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message


# Set broker and port
broker = "localhost"
port = 1883

client.connect(broker, port)

client.loop_forever()


