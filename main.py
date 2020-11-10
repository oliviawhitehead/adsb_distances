import json
from kafka import KafkaConsumer
import test
def main():

    consumer = KafkaConsumer('adsb-data', bootstrap_servers=['my-cluster-kafka-bootstrap:9092'], auto_offset_reset='earliest')

    for message in consumer:

        # Decode the received message
        ascii_msg = message.value.decode('ascii')
        # Do some formatting
        ascii_msg = ascii_msg.replace("'", "\"")
        # Turn into a dict
        output_dict = json.loads(ascii_msg)

        '''
        ############## CUSTOM CODE GOES HERE ###################
        '''
        test.TargetDistance(output_dict)
       
        '''
        ########################################################
        '''


    return None