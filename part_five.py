from part_four import *
from part_two import *

earth=Earth(0)
str1=Satellite("str1",100)
str2=Satellite("str2",200)
str3=Satellite("str3",300)
str4=Satellite("str4",400)


p_final = Packet(data="!Hello From Earth", sender=str3, receiver=str4)
p_layer1 = RelayPacket(packet_to_relay=p_final,sender=str2,proxy=str3)
p_layer2 = RelayPacket(packet_to_relay=p_layer1,sender=str1,proxy=str2)
p_layer3 = RelayPacket(packet_to_relay=p_layer2,sender=earth,proxy=str1)
attempt_transmission(p_layer3)