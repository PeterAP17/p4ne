import ipaddress
import random
listOfIPv4 = []

class IPv4RandomNetwork (ipaddress.IPv4Network):
   def __init__(self):
       self.network = random.randint(0x0B000000, 0xDF000000)
       self.prefix = random.randint(8, 24)
       ipaddress.IPv4Network.__init__(self,(self.network, self.prefix),strict=False)

   def is_regular(self):
       return self.is_global

   def networkPrefixToNumber(self):
       return (int(self.network) + (int(self.prefix) << 32))

def simplefunc(x):
    return x.networkPrefixToNumber()

i = 0
while i<100:
    random_network = IPv4RandomNetwork()
    listOfIPv4.append (random_network)
    i = i + 1

#print (sorted(listOfIPv4, key=simplefunc))

for n in sorted(listOfIPv4, key=simplefunc):
    print(n)


