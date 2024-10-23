properties=[]
propertiesfile=open("Exam Two Properties.csv")
x = propertiesfile.readline()
while x != "":
    y = x.split(",")
    properties.append(y)
    x = propertiesfile.readline()
    

propertiesfile.close()

for i in range(len(properties)):
    print(properties[i][0],properties[i][1])

zipcodes=[]
found=False
for i in range(len(properties)):
     zip_code=properties[i][3]
     price=float(properties[i][4])
     for j in range(len(zipcodes)):
          if zipcodes[j][0] == zip_code:
            zipcodes[j][1] += 1
            zipcodes[j][2] += price
            found = True
            break
     if not found:
        x = []
        x.append(zip_code)
        x.append(1)
        x.append(price)
        zipcodes.append(x)
          
print("\nZip Code  Count of Properties  Average Property Price")
for zipcode in zipcodes:
    averageprice = zipcode[2] / zipcode[1]
#    print(f"{zipcode[0]}, {zipcode[1]}, {averageprice:.2f}")
    print("{:>8s} {:20d} {:23.2f}".format(zipcode[0],zipcode[1],averageprice))

