searchterm=input("Enter Search Term: ")

confile = open("constitution.txt", "r")
lines=confile.readlines()
confile.close()

i=0
while i < len(lines):
    if searchterm in lines[i]:
        start = i
        while start > 0 and lines[start] != '\n':
            start -= 1
            end = i
        while end < len(lines) and lines[end] != '\n':
            end += 1
        for j in range(start,end+1):
            print("Line "+ str(j + 1) + ":" + lines[j], end='')

            i = end
    else:
            i += 1
