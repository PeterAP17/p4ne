import ipaddress
import random
listOfIPv4 = []

class IPv4RandomNetwork (ipaddress.IPv4Network):
   def __init__(self):
       network = random.randint(0x0B000000, 0xDF000000)
       prefix = random.randint(8, 24)
       ipaddress.IPv4Network.__init__(self,(network, prefix),strict=False)

   def is_regular(self):
       return self.is_global

   def key_value(self):
       return int(self.network_address) + (int(self.netmask) << 32)

def sortfunc(x):
    return x.key_value()

i = 0
while i<100:
    random_network = IPv4RandomNetwork()
    listOfIPv4.append (random_network)
    i = i + 1

for n in sorted(listOfIPv4, key=sortfunc):
    print(n)

