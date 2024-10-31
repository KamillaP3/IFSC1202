import csv

file = '09.Project Distances.csv'
with open(file, mode='r') as file:
    reader = csv.reader(file)
    distances = [row for row in reader]

print("Distance Table:")
for row in distances:
    print(" ".join(f"{item:>10}" for item in row))

fromcity = input("Enter From City: ")

# Prompt for a To City
tocity = input("Enter To City: ")

# Search the zeroth column for the From City
fromindex = -1
for i in range(len(distances)):
    if distances[i][0] == fromcity:
        fromindex = i
        break

# Search the zeroth row for the To City
toindex = -1
for j in range(len(distances[0])):
    if distances[0][j] == tocity:
        toindex = j
        break

# Check if the cities were found and display the result
if fromindex == -1:
    print("Invalid From City")
elif toindex == -1:
    print("Invalid To City")
else:
    distance = distances[fromindex][toindex]
    print(f"{fromcity} to {tocity} - {distance} miles")