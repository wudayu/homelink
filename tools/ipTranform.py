fileIn = open('ips.txt', 'rb')
fileOut = open('ipsAfter.txt', 'w')
fileOut.write('IPPOOL=[\n')
for line in fileIn:
    fileOut.write('  {"ipAddr":"' + line[:-2] + '"},\n')
fileOut.write(']\n')
