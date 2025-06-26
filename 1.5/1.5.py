import glob
ListOfIP=[]
#count = 0

files=glob.iglob('C://p4ne//log_files//*.log')
#print(type(files))

for i in files:
    print(i)
    with open (i) as file:
        for j in file:
            #count = count + 1
            raw_line = j
            line = raw_line.strip()

            if line.find('ip address')==0:
                lineWithoutText = line.replace("ip address", "")
                PureLine = lineWithoutText.strip()
                #print (PureLine)
                ListOfIP.append(PureLine)
    #i.close() - так и не понял, почему эта штука не работает (((

SetOfIP = set(ListOfIP)
ListOfIP = list (SetOfIP)

for count in ListOfIP:
    print ("|%-40s|" % count)#,"|%20s|" % i.network_address, "|%20s|" % i.netmask)



