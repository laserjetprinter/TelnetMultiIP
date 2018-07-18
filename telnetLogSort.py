import csv
from string import *

stored = {}   	#dictionary to store IP and connection status
counter = 0   	#case to track first IP occurrence
curIpVal = ""	#stores current IP value
prevIpVal = ""  #sotres previous IP value

#opens input telnet log file
with open('TELNET-CSV-LOG-FILE-OUTPUT-FROM-POWERSHELL-SCRIPT-FILEPATH') as csvfile:
	read_csv = csv.reader(x.replace('\0', '') for x in csvfile) #replaces blank line with null value
			
	for row in read_csv:
		
		if len(row)==0: #if current row is null, skip
			continue
		
		elif counter == 0: #if on first IP address
			if row[0][2].isdigit(): #if the value is a digit, it is an IP
				prevIpVal = row[0][2:]
				curIpVal = prevIpVal
				counter+=1
		
		elif row[0][0].isdigit(): #if it is an IP and is not the first address
			curIpVal = row[0]
			if prevIpVal[0][0].isdigit(): #previous is IP and not blank, no connection made
				stored[prevIpVal] = False
				prevIpVal = curIpVal
			else:
				prevIpVal = curIpVal
					
		elif row[0][0]=="C" and row[0][1]=="o": #if current is IP and log has details on it
			if row[0][-2]=="s": #no connection made
				stored[curIpVal]=False
				prevIpVal = "Not"
			else: #connection made
				stored[curIpVal]=True
				prevIpVal = "Not"

csvfile.close() #close file reader
    
#write to a new formatted csv, containing telnet ip and connection status
with open('FINAL-FORMATTED-OUTPUT-CSV-FILE-FILEPATH',"w") as output:
    writer = csv.writer(output, delimiter=',', lineterminator='\n')
    for key,value in stored.items():
        writer.writerow([key,value])
output.close()

stored = {} #clear dictionary memory