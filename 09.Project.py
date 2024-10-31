filename = '09.Project Distances.csv'
with open(filename, mode='r') as file:
    distances = [line.strip().split(',') for line in file]

print("Distance Table:")
for row in distances:
    print(" ".join(f"{item:>10}" for item in row))

fromcity = input("Enter From City: ")

tocity = input("Enter To City: ")

fromindex = -1
for i in range(len(distances)):
    if distances[i][0] == fromcity:
        fromindex = i
        break

toindex = -1
for j in range(len(distances[0])):
    if distances[0][j] == tocity:
        toindex = j
        break

if fromindex == -1:
    print("Invalid From City")
elif toindex == -1:
    print("Invalid To City")
else:
    distance = distances[fromindex][toindex]
    print(f"{fromcity} to {tocity} - {distance} miles")