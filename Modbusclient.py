
import grpc
import lib.MQTT_pb2  as pb2
import lib.MQTT_pb2_grpc  as pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel :
        pb2_grpc.MQTTManagerStub(channel)
        stub= pb2_grpc.MQTTManagerStub(channel)
        print('Donner Topic')
        topic2=input()
        print('Donner Payload')
        payload2=input()
        #print('Donner Qos')
        #qos2=input()
        Acknowledgment= stub.PublishMessages(pb2.ComingData(Topic=topic2,Payload=payload2))
        print(Acknowledgment)

if __name__== '__main__':
    print('client starting the connection ')
    run()
                