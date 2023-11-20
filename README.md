# MQTT Kafka Bridge Test

This project is a test implementation of a bridge between MQTT and Kafka.

## Why MQTT and Kafka?

### MQTT

MQTT (Message Queuing Telemetry Transport) is a lightweight and efficient messaging protocol designed for constrained devices and low-bandwidth, high-latency, or unreliable networks. It is well-suited for IoT environments where resources may be limited and where a lightweight, publish-subscribe communication model is beneficial.

### Kafka

Kafka, on the other hand, is a distributed streaming platform built for handling large volumes of data and real-time data streaming. It is often used in data center environments where a stable network and substantial compute resources are available.

## The Bridge

Combining MQTT and Kafka in an IoT environment can offer several advantages:

1. **Lightweight Communication:** MQTT is well-suited for resource-constrained IoT devices, providing a lightweight and efficient messaging protocol.

2. **Data Streaming and Processing:** Kafka excels at handling large volumes of data streams, making it suitable for processing and analyzing data from IoT devices at scale.

3. **Reliability and Durability:** Kafka's durability features ensure that data is not lost even in the face of system failures. This can be critical in IoT scenarios where data integrity is paramount.

4. **Integration with Existing Systems:** Kafka's capabilities make it a powerful intermediary for integrating IoT data with other enterprise systems, analytics platforms, or storage solutions.

### Mosquitto MQTT Broker

In the default mode of the Mosquitto MQTT broker, messages are not stored on disk by default. They are maintained in memory. If there are no subscribers for a topic at the time a message is published, the message is not saved for future subscribers. This behavior aligns with the lightweight and low-latency design principles of MQTT.
