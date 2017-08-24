# main.py
import os
import csv
from statesdata import *
from datetime import datetime

EmpID = []
FirstName = []
LastName = []
DOB = []
SSN = []
State = []
strlast = ""

# inputfile = os.path.join('Resources', strfile)
csvpath = os.path.join('Resources', 'employee_data3.csv')

with open(csvpath, encoding="utf-8", newline='') as csvfile:
	# read file 
	csvreader = csv.reader(csvfile, delimiter=',')

	# bypass header
	next(csvreader, None)
	for row in csvreader:
		# print(row[1])
		# add emp id to EmpID
		EmpID.append(row[0])

		# split name column		
		strNames = row[1].split(" ")
		# print(str(len(strNames)) + " " +  strNames[0] + "    " + strNames[1])
		# First Name
		FirstName.append(strNames[0])

		# LastName
		# check if more than 1 last name example Michael Rogers Jr.
		if len(strNames) > 2:
			for i in range(1, len(strNames)):
				# print(str(i) + " : " + strNames[i])
				if i>1:
					strlast += " "
				strlast += str(strNames[i])
			LastName.append(strlast)
		else:
			LastName.append(strNames[1])

		# Date of Birth (DD/MM/YYYY) format
		newdate = datetime.strptime(row[2], '%Y-%m-%d').strftime('%d/%m/%Y')
		# print(row[2] + " -> " + newdate)
		DOB.append(newdate)

		# SSN
		ssnlist = list(row[3])
		for i in range(0, 6):
			if ssnlist[i] != '-':
				ssnlist[i] = '*'

		SSN.append(''.join(ssnlist))
		# print(row[3] + " -> " + ''.join(ssn))

		# state
		# stateKey = [key for key, value in states.items() if value == row[4]]
		# print (states.keys()[states.values()])
		# print(row[4] + " -> " + str(stateKey))

		found = ""
		for k,v in states.items():
			if v == row[4]:
				# print(k + " : " + v)
				found = k
				break

		if len(found) > 0:
			State.append(found)
			# print(found)
		else:
			State.append("**Invalid State**")

bossCSV = zip(EmpID,FirstName,LastName,DOB,SSN,State)

# Specify the file to write to
outpath = os.path.join('outpath', 'result_' + csvpath.rsplit('\\', 1)[1].rsplit('.',1)[0] + '.csv' )
# print(outpath)

with open(outpath, 'w', newline="") as csvFile:
        csvWriter = csv.writer(csvFile, delimiter=',')
        csvWriter.writerow(["Emp ID","First Name","Last Name","DOB","SSN","State"])
        csvWriter.writerows(bossCSV)

print("PyBoss ran successfully")