from rlworldclient import RlWorldClient
import time
import random

id = random.randint(0,100)

while True:
    try:
        client = RlWorldClient("127.0.0.1",1337)
        while True:
            # print("read")
            client.read_observation_dict()
            # print("send")


            action_dict = {
                "name": "Bot " + str(id),
                "moveForwardBack":1.0,
                "moveRightLeft": 0.0,
                "turnRightLeft": random.uniform(-1.0,1.0),
                "fire": True,
            }

            client.send_action_dict(action_dict)
            # print("sleep")
            time.sleep(0.5)
    except Exception as e:
        print(e)
        time.sleep(1)