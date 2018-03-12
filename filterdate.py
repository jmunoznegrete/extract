import sys

def getFileOut(FileIn):
    fileOut = FileIn.split(".csv")[0] + "_fi.csv"
    return fileOut

try:
    FileIn = sys.argv[1]
    FileOut = getFileOut(sys.argv[1])
except IndexError :
    print "Error: usage: python filterdate.py filename.csv"
    exit(0)

with open(FileIn, 'r') as fin:
    with open(FileOut, 'a+') as fout:
        i = 0
        for line in fin:
            if i== 0:
                fout.write(line)
                i = i+1
                continue

            line = line.split('\r')[0]
            if (float(line.split(',')[5]) == 0.0):
                continue
            indice = line.find('.000 GMT')
            if (indice > 0):
                lineout = line[0:indice]+line[indice+13:]+'\n'
            else:
                lineout = line + '\n'
            ##print lineout[:-1]
            fout.write(lineout)

print 'Done with ', FileIn,' and ', FileOut
