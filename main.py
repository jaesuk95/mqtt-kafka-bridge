# pip install paho-mqtt
import paho.mqtt.client as mqtt
from random import uniform
import time

# MQTT broker settings
mqtt_broker = "localhost"
port = 1883

# MQTT topic to which you want to publish data
mqtt_topic = "mqtt_first_test"

# Create an MQTT client instance
client = mqtt.Client()

# Connect to the MQTT broker
client.connect(mqtt_broker, port, keepalive=60)

while True:
    randomNumber = uniform(20.0, 21.0)
    client.publish("mqtt_first_test", randomNumber)
    print('MQTT: Just Published ' + str(randomNumber) + ' to topic mqtt_first_test')
