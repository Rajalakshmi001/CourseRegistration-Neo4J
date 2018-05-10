from kafka import KafkaConsumer
from neo4j.v1 import GraphDatabase
from enrollments import *
import json

topic = 'NEO4J'
db = None
def listen(consumer):
    print ("Subscribed to Kafka topic: ", topic)
    for msg in consumer:
        try:
            if msg.value is None:
                print("BAD MESSAGE: ", msg)
                continue
            print("GOOD: ", msg.value)
            payload = msg.value
            category = payload['category']
            data = payload['data']
            cmd = payload['command']
            
            if category == 'ENROLLMENT':
                enrollment_handler(cmd, data)

        except Exception as e:
            print(e)

def enrollment_handler(cmd, data):
    if cmd == 'CREATE':
        enrollment_create(db, data)
    elif cmd == 'DELETE':
        enrollment_delete(db, data)
def decode_message(m):
    try:
        return json.loads(m.decode('utf-8'))
    except Exception as e:
        return None

if __name__ == '__main__':
    consumer = KafkaConsumer(topic, 
    bootstrap_servers='137.112.89.91:9092',
        #group_id='Neo4jReg', 
        group_id=None,
        auto_offset_reset = 'earliest',
        value_deserializer = decode_message
        )
    db = GraphDatabase.driver("bolt://137.112.89.94:7687", auth=("neo4j", "An3WeeWa"))
    listen(consumer)
