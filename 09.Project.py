distances=[]
distancesfile=open("09.Project Distances.csv")
x = distancesfile.readline()
while x != "":
    y = x.split(",")
    distances.append(y)
    x = distancesfile.readline()
    

distancesfile.close()
for row in distances:
    for element in row:
        print(element, end=" ") 
    print() 

for row in distances:
    print("{:>8s} {:>20s} {:>23s}".format(*row[:3]))
