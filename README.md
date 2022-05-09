# Multiprotocol Gateway 

**This is a Multiprotocol Platform that works as a Gateway that 
implements different protocols.**


In fact, this platform is based mainly on gRPC that gurantees the communication and the transfer of data exchanged between the servers and the clients .

This is a Gateway that manages distincts protocls including:

   MQTT
   ModBus TCP
   ModBus RTU 
   wIFI
   ZigBee
   LoRa
   BLE...
 
In this project we implemented just 2 protocols which are : MQTT and ModBus TCP

**Implemented Protocls :**

    MQTT
    ModBusTCP

Main Actors of this Gateway are :

## ModBus TCP Client :
 This actor will initiate the communication in the platform after receiving the data from the ModBus TCP server .

## MQTT Server:
 This actor provides the main service in the platform which is to publish the data received into the Mosquitto Broker. It makes the link between the ModBus TCP client and the Broker :it is like a Gateway.

## ConfigManager Server:
 This actor provides an essential service for the launch of any client or server present in the platform. In fact, any client or server before starting the communication, he must send a request to this server to provide him with the necessary connection parameters.

## ModBus TCP Server:
 This actor is the starting point of the communication, it is this one who allows the ModBus TCP client to acquire the data.

The specification of the needs is used to associate each actor of the system with the set of actions with which it intervenes. We use the **_use case diagrams_** to model the functional requirements.

The use case diagram in the following figure gives a global view of the platform that we want to realize.
![use case](https://www.facebook.com/messenger_media/?thread_id=100034786336294&attachment_id=5246519828704774&message_id=mid.%24cAABa-ynnniaG2m0BU2AqSe3esHDz)


We present below all the sequence diagrams corresponding to the use cases presented previously and the class diagram.

1/Global Platform Sequence Diagram :
![sequence diagram](https://www.facebook.com/messenger_media/?thread_id=100034786336294&attachment_id=5246519828704774&message_id=mid.%24cAABa-ynnniaG2m0BU2AqSe3esHDz)
2/Detailed Sequence Diagram:
![sequence diagram](https://www.facebook.com/messenger_media/?thread_id=100034786336294&attachment_id=5246519828704774&message_id=mid.%24cAABa-ynnniaG2m0BU2AqSe3esHDz)
3/Class diagram 
![class digram](https://www.facebook.com/messenger_media/?thread_id=100034786336294&attachment_id=5246519828704774&message_id=mid.%24cAABa-ynnniaG2m0BU2AqSe3esHDz)


