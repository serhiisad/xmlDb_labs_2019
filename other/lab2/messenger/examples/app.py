import redis
import time
import traceback
import random

def check_spam(self, message):
    '''
    imitation of spam-checking
    :param self:
    :param message:
    :return:
    '''
    time.sleep(random.randint(0, 3))
    r = bool(random.getrandbits(1))
    print(r)
    return r

def RedisCheck():
    try:
        r = redis.StrictRedis(host='localhost', port=6379)                 # Connect to local Redis instance
        p = r.pubsub()                                                              # See https://github.com/andymccurdy/redis-py/#publish--subscribe
        p.subscribe('startScripts')                                                 # Subscribe to startScripts channel
        PAUSE = True

        while PAUSE:                                                                # Will stay in loop until START message received
            print("Waiting For redisStarter...")
            message = p.get_message()                                               # Checks for message
            if message:
                command = message['data']                                           # Get data from message
                if command == b'START':                                             # Checks for START message
                    PAUSE = False                                                   # Breaks loop
            time.sleep(1)

        print("Permission to start...")

    except Exception as e:
        print("Connecting error")
        print(str(e))
        print(traceback.format_exc())

RedisCheck()

#
# def WorkCheck():
#     try:
#
#         # HERE SOME INITIAL WORK IS DONE THAT SCRIPTS 1 & 2 NEED TO WAIT FOR
#         # IDs SERIAL PORTS
#         # SAVE TO db
#
#         r = redis.StrictRedis(host='localhost', port=6379)                # Connect to local Redis instance
#         p = r.pubsub()                                                    # See https://github.com/andymccurdy/redis-py/#publish--subscribe
#
#         print("Starting main scripts...")
#
#         r.publish('startScripts', 'START')                                # PUBLISH START message on startScripts channel
#
#         print("Done")
#
#     except Exception as e:
#         print("Connection error")
#         print(str(e))
#         print(traceback.format_exc())