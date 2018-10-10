from kafka import KafkaConsumer
import json
import time
import sys
import base64
import requests

class token_generator:

    userinfo = {
        "username": "device-manager",
        "service": "admin"
    }

    jwt = "{}.{}.{}".format(base64.b64encode("model".encode()).decode(),
                            base64.b64encode(json.dumps(
                                userinfo).encode()).decode(),
                            base64.b64encode("signature".encode()).decode())

    def get_token(self):
        return self.jwt

def get_topic(service, subject):

    token = token_generator()
    jwt = token.get_token()
    
    url = "{}/topic/{}".format('http://172.20.0.19:80', subject)

    response = requests.get(url, headers={"authorization": jwt})
    if 200 <= response.status_code < 300:
        payload = response.json()
        return payload['topic']

def python_kafka_consumer_performance(topic):

    consumer = KafkaConsumer(
        bootstrap_servers='172.20.0.15:9092',
        auto_offset_reset = 'latest', # start at 
        group_id = '1'
    )
    msg_consumed_count = 0
    consumer.subscribe([topic])
    for msg in consumer:
        msg_consumed_count += 1
        event = json.loads(msg.value)
        value = int(event['data']['label'])
        print(value)
        if(msg_consumed_count - value != 0):
            print("msg out of order")
            print(value, msg.timestamp, msg_consumed_count, time.time(), msg_consumed_count - value)
        print(value, msg.timestamp, msg_consumed_count, time.time(), msg_consumed_count - value)
    consumer.close()    

if __name__=="__main__":
    topic_consumer = get_topic("admin", "dojot.device-manager.device")
    python_kafka_consumer_performance(topic_consumer)


