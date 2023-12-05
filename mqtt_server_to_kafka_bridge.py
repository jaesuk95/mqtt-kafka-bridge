# pip install pykafka

import paho.mqtt.client as mqtt
from pykafka import KafkaClient
import time

# this application is planned to run inside of MQTT server
# then, transmit the data to Kafka-server

# MQTT broker settings
# mqtt_broker = "10.104.238.73"
mqtt_broker = "127.0.0.1"
mqtt_port = 1883

# MQTT topic to which you want to publish data
mqtt_topic = "mqtt_first_test"

# Create an MQTT client instance
mqtt_client = mqtt.Client()


# Function to handle connection status
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker")
        # Subscribe to the MQTT topic
        client.subscribe(mqtt_topic)
    else:
        print(f"Failed to connect to MQTT broker with result code {rc}")


def on_message(client, userdata, message):
    msg_payload = str(message.payload.decode('utf-8'))
    print('Received MQTT message:', msg_payload)

    # Publish the MQTT message to Kafka
    kafka_producer.produce(bytes(msg_payload, 'utf-8'))
    print('Kafka: Just published ' + msg_payload + ' to topic kafka_first_test')


# Set the callback functions
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message

# Connect to the MQTT broker
mqtt_client.connect(mqtt_broker, mqtt_port, keepalive=60)

# kafka broker settings
# kafka_broker = "192.168.1.30:9092"      # example, you are transmitting data from MQTT Local server to Kafka-server
# kafka_broker = "10.103.226.125:9092"      # example, you are transmitting data from MQTT Local server to Kafka-server
kafka_broker = "127.0.0.1:9092"      # example, you are transmitting data from MQTT Local server to Kafka-server

# Create a kafka client instance
kafka_client = KafkaClient(hosts=kafka_broker)

# Access a Kafka topic (Create one if it doesn't exist)
kafka_topic_name = 'kafka_test'
kafka_topic = kafka_client.topics[kafka_topic_name]
kafka_producer = kafka_topic.get_sync_producer()

# Start the MQTT client loop
mqtt_client.loop_forever()

# mqtt_client.loop_start()
# mqtt_client.subscribe(mqtt_topic)
# mqtt_client.on_message = on_message
# time.sleep(10)
# mqtt_client.loop_stop()

# ./bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic kafka_first_test --from-beginning
