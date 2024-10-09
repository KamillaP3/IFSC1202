inputfile = open('07.Project Angles Input.txt', 'r')
lines = inputfile.readlines()
inputfile.close()

decimaldegrees = []
for line in lines:
    
    line = line.replace('\n', '')

    degreeindex = line.index('°')
    minuteindex = line.index("'")
    secondindex = line.index('"')

    degrees = float(line[:degreeindex])
    minutes = float(line[degreeindex + 1:minuteindex])
    seconds = float(line[minuteindex + 1:secondindex])
    
    decimaldegree = degrees + (minutes / 60) + (seconds / 3600)
    decimaldegrees.append(decimaldegree)

outputfile = open('07.Project Angles Output.txt', 'w')
for decimaldegree in decimaldegrees:
    outputfile.write(f"{decimaldegree}\n")
outputfile.close()

print(f"{len(decimaldegrees)} records processed")