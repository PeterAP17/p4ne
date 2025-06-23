import glob
ListOfIP=[]
count = 0

files=glob.iglob('C://p4ne//log_files//*.log')

for i in files:
    with open (i) as file:
        for j in file:
            count = count + 1
            raw_line = j
            line = raw_line.strip()

            if line.find('ip address')==0:
                lineWithoutText = line.replace("ip address", "")
                PureLine = lineWithoutText.strip()
                print (PureLine)
                ListOfIP.append(PureLine)

SetOfIP = set(ListOfIP)
ListOfIP = list (SetOfIP)

for i in ListOfIP:
    print (i)



