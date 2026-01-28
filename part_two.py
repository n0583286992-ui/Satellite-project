import time

from space_network_lib import *
from First_system import *
from time import sleep

network=SpaceNetwork(level=2)
def attempt_transmission(packet):
    while True:
        try:
            network.send(packet)
            print("The message was sent successfully")
            return
        except TemporalInterferenceError:
            print("Interference ,waiting")
            time.sleep(2)
            continue
        except DataCorruptedError:
            print("Data corrupted retrying")
            continue

