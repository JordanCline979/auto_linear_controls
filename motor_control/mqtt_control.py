import paho.mqtt.client as mqtt

# define callback functions
def on_connect(client, userdata, flags, rc):
    if rc == 0: print("Connected to MQTT Broker")
    else: print("Failed to connect, return code: ", rc)


# Create a client instance
client = mqtt.Client()