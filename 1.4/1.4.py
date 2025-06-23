import ipaddress
import random

#network = ipaddress.IPv4Network('192.168.1.0/24', strict=True)
#print (network)

class IPv4RandomNetwork (ipaddress.IPv4Network):
   def __init__(self):
       network = random.randint(0x0B000000, 0xDF000000)
       prefix = random.randint(8, 24)
       ipaddress.IPv4Network.__init__(self,(network, prefix),strict=False)

random_network = IPv4RandomNetwork ()
print (random_network)

    #def regular (self)
     #   return (True)
      #  return (False)

