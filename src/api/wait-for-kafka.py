import os
from kafka import KafkaConsumer
from kafka.errors import NoBrokersAvailable
import backoff


@backoff.on_exception(backoff.expo, NoBrokersAvailable)
def ping():
    try:
        KafkaConsumer('views',
                      bootstrap_servers='{}:{}'.format(
                          os.getenv('KAFKA_HOST'),
                          os.getenv('KAFKA_PORT')
                      ))
    except NoBrokersAvailable as e:
        print(e)
        raise NoBrokersAvailable()




if __name__ == '__main__':
    ping()
