inputfile = '06.Project Input File.txt'
mergefile = '06.Project Merge File.txt'
outputfile = '06.Project Output File.txt'

inputcount = 0
mergecount = 0
outputcount = 0

infile = open(inputfile, 'r')
outfile = open(outputfile, 'w')

for line in infile:
    inputcount += 1
    if '**Insert Merge File Here**' in line:
        mergefile = open(mergefile, 'r')
        for mergeline in mergefile:
            outfile.write(mergeline)
            mergecount += 1
            outputcount += 1
        mergefile.close()
    else:
        outfile.write(line)
        outputcount += 1

infile.close()
outfile.close()

print(f"{inputcount} input file records")
print(f"{mergecount} merge file records")
print(f"{outputcount} output file records")

