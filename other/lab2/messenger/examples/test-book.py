import redis
import time
import threading
import traceback

redis_host = 'localhost'
redis_port = 6380
redis_password = ""


#conn = redis.Redis()

try:
    conn = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)
except ConnectionRefusedError as e:
    print("Connecting error")
    print(str(e))
    print(traceback.format_exc())


def publisher(n):

    time.sleep(1)
    for i in range(n):
        conn.publish('kanal', str(i))
        time.sleep(1)


def run_pubsub():

    threading.Thread(target=publisher, args=(3, )).start()

    pubsub = conn.pubsub()
    pubsub.subscribe(['kanal'])
    count = 0

    for item in pubsub.listen():

        print(item)


        count += 1
        if count == 4:
            pubsub.unsubscribe()
        if count == 5:
            break

run_pubsub()