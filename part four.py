from space_network_lib import *
from part_three import *
from part_two import *
from First_system import *

class RelayPacket(Packet):
    def __init__(self,packet_to_relay, sender, proxy):
        super().__init__(packet_to_relay,sender,proxy)

    def __repr__(self):
        return f"Relaying[{self.data}] to {self.receiver} from {self.sender}"

class Satellite(SpaceEntity):
    def receive_signal(self,packet):
        if isinstance(packet,RelayPacket):
            inner_packet = packet.data
            print(f"Unwrapping and forwarding to {inner_packet.receiver}")

            attempt_transmission(inner_packet)
        else:
            print(f"Final destination reached: {packet.data}")

class Earth(SpaceEntity):
    def __init__(self,distance):
        super().__init__("Earth",distance)
        self.name="Earth"

    def receive_signal(self, packet: Packet):
        pass

earth = Earth(0)
str1 = Satellite("str1",100)
str2 = Satellite("str2",200)

p_final=Packet(data="hello from eath",sender=str1,receiver=str2)

p_earth_to_str1=RelayPacket(packet_to_relay=p_final,sender=earth,proxy=str1)

attempt_transmission(p_earth_to_str1)