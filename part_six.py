from part_five import *
from part_two import *

def smart_send_packet(all_entities, packet):
    source = packet.sender
    destination =packet.receiver

    relevant_nodes = []
    for entity in all_entities:
        if source.distance_from_earth < entity.distance_from_earth < destination.distance_from_earth:
            relevant_nodes.append(entity)

    relevant_nodes.sort(key=lambda x: x.distance_from_earth)

    path = [source] + relevant_nodes + [destination]


    p=packet
    for i in range(len(path)-2,-1, -1):
        p=RelayPacket(packet_to_relay=p,sender=path[i],proxy=path[i+1])

    source.send_packet(p)