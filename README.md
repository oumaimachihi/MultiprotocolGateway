# Multiprotocol Gateway 

**This is a Multiprotocol Platform that works as a Gateway that 
implements different protocols.**


In fact, this platform is based mainly on gRPC that gurantees the communication and the transfer of data exchanged between the servers and the clients .

This is a Gateway that manages distincts protocls including:

    MQTT
    ModBus TCP/RTU
    wIFI
    ZigBee
    LoRa
 
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

![use case](https://user-images.githubusercontent.com/87174876/167430386-b85a8edc-ee19-4df4-9e37-c4650968bf62.png)

We present below all the sequence diagrams corresponding to the use cases presented previously and the class diagram.

### 1/Global Platform Sequence Diagram :
![sequence diagram](https://user-images.githubusercontent.com/87174876/167430412-f2ff18e4-dcd8-4d50-83fe-27ee60f2d60c.png)

### 2/Detailed Sequence Diagram:
![sequence diagram2](https://user-images.githubusercontent.com/87174876/167430453-053813d3-3e7e-4784-b3ab-b07702e6f584.png)

### 3/Class diagram 
![class diagram](https://user-images.githubusercontent.com/87174876/167430488-60b77bcd-5957-4de1-8ebf-8cede2e0ea1f.png)


## requirements

    grpcio==1.45.0
    grpcio-tools==1.45.0
    paho-mqtt==1.6.1
    protobuf==3.6.1
    pyModbusTCP==0.1.10


