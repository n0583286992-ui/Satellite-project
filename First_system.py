from space_network_lib import SpaceEntity, SpaceNetwork,Packet

network = SpaceNetwork(level=1)
class Satellite(SpaceEntity):
    def __init__(self, name, distance_from_earth,level=1):
        super().__init__(name, distance_from_earth)
        self.level = level

    def receive_signal(self, packet: Packet):
        print(f" [{self.name}]  Received: {packet}")


str1 = Satellite("str1",100)
str2 = Satellite("str2",200)

<<<<<<< HEAD
my_packet = Packet("i am the first")
=======
my_packet = Packet("i am the first",str1,str2)
>>>>>>> 54078f2 (level2)

my_packet.sender = str1
my_packet.receiver = str2
network.send(my_packet)