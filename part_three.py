from space_network_lib import *

class BrokenConnectionError(CommsError):
    pass

network=SpaceNetwork(level=3)
def new_errors(packet):
    while True:
            try:
                network.send(packet)
                return
            except (TemporalInterferenceError, DataCorruptedError):
                pass
            except LinkTerminatedError:
                print("Link lost")
                raise BrokenConnectionError
            except OutOfRangeError:
                print("Target out of range")
                raise BrokenConnectionError


