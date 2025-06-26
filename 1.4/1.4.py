import ipaddress
import random
listOfIPv4 = []

class IPv4RandomNetwork (ipaddress.IPv4Network):
   def __init__(self):
       self.network = random.randint(0x0B000000, 0xDF000000)
       self.prefix = random.randint(0, 32)
       ipaddress.IPv4Network.__init__(self,(self.network, self.prefix),strict=False)

   def is_regular(self):
       return self.is_global

   def networkAndPrefixToNumber(self):
       netAndPrefToNumber = (int(self.network) + (int(self.prefix) << 32))
       #print ("|%20s|" % netAndPrefToNumber, "|%20s|" % self, "|%20s|" % self.network_address, "|%20s|" % self.netmask)
       return (netAndPrefToNumber)

def simplefunc(x):
    return x.networkAndPrefixToNumber()

i = 0
while i<10:
    random_network = IPv4RandomNetwork()
    listOfIPv4.append (random_network)
    i = i + 1

print (listOfIPv4)

for i in sorted(listOfIPv4, key=simplefunc):
    print ("|%20s|" % i.networkAndPrefixToNumber(), "|%20s|" % i, "|%20s|" % i.network_address, "|%20s|" % i.netmask)
