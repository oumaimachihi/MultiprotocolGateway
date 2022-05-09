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


![class diagram](https://user-images.githubusercontent.com/87174876/167430014-a83f75e8-438d-40a9-acf0-8d7cc6e63e50.png)


We present below all the sequence diagrams corresponding to the use cases presented previously and the class diagram.

1/Global Platform Sequence Diagram :
![use case](https://user-images.githubusercontent.com/87174876/167430058-b1b0de05-9284-436b-a325-cdba603055ba.png)

2/Detailed Sequence Diagram:
![sequence diagram](https://user-images.githubusercontent.com/87174876/167430092-c9cab831-7491-470c-a65d-3c2daa3b63a2.png)

3/Class diagram 
![sequence diagram2](https://user-images.githubusercontent.com/87174876/167430111-73a60528-bbbb-49b1-a745-ec87cc1f53b3.png)
