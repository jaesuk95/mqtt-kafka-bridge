import paho.mqtt.client as mqtt
from pykafka import KafkaClient
import asyncio
import concurrent.futures

# MQTT broker settings
mqtt_broker = "127.0.0.1"
mqtt_port = 1883
mqtt_topic = "mqtt_first_test"

# Kafka broker settings
# kafka_broker = "127.0.0.1:9092"
kafka_broker = "192.168.49.2:9092"
kafka_topic_name = 'kafka_test'

# Create a MQTT client instance
mqtt_client = mqtt.Client()

# Create a Kafka producer
kafka_client = KafkaClient(hosts=kafka_broker)
kafka_topic = kafka_client.topics[kafka_topic_name]
kafka_producer = kafka_topic.get_producer()

# Function to handle connection status
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker")
        # Subscribe to the MQTT topic
        client.subscribe(mqtt_topic)
    else:
        print(f"Failed to connect to MQTT broker with result code {rc}")

# Function to handle MQTT messages
def on_message(client, userdata, message):
    msg_payload = str(message.payload.decode('utf-8'))
    print('Received MQTT message:', msg_payload)

    # Asynchronously publish the MQTT message to Kafka
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(publish_to_kafka(msg_payload))

# Set the callback functions
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message

# Connect to the MQTT broker
mqtt_client.connect(mqtt_broker, mqtt_port, keepalive=60)

# Start the MQTT client loop
mqtt_client.loop_start()

# Asynchronous function to publish messages to Kafka
async def publish_to_kafka(msg_payload):
    # Use asyncio.run_in_executor to run blocking Kafka publish in a separate thread
    with concurrent.futures.ThreadPoolExecutor() as executor:
        await asyncio.get_event_loop().run_in_executor(
            executor,
            lambda: kafka_producer.produce(bytes(msg_payload, 'utf-8'))
        )

# Run the event loop
try:
    asyncio.get_event_loop().run_forever()
except KeyboardInterrupt:
    print("Terminating...")
    mqtt_client.disconnect()
    asyncio.get_event_loop().stop()
    asyncio.get_event_loop().run_until_complete(asyncio.gather(*asyncio.all_tasks()))
