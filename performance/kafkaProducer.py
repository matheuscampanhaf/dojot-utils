from kafka import KafkaProducer
import json
import time
import sys


def calculate_kafka_python_perf(num_messages, count):
    producer = KafkaProducer(bootstrap_servers='172.20.0.15:9092')

    producer_start = time.time()
    topic = 'kafka-python-performance'
    msg_payload = 'testing perf'
    for i in range(num_messages):
        count += 1
        msg_payload = str(count)
        producer.send(topic,msg_payload)

    producer.flush()

    return time.time() - producer_start

if __name__=="__main__":
    num_messages = int(sys.argv[1])
    freq = int(sys.argv[2])
    seq_messages = 0
    while(True):
        time_prodution = calculate_kafka_python_perf(num_messages, seq_messages * num_messages)
        print("Produced %s messages in %s seconds" % (num_messages, time_prodution))
        seq_messages += 1
        time.sleep(freq)