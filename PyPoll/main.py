# main.py
import os
import csv
import sys
from collections import defaultdict


# print("Please place files in Resources directory")
# strfile = input("Enter filename you want to analyze: example <budget_data_1.csv> ")

strfile = "election_data_2.csv"

csvpath = os.path.join('Resources', strfile)

pollDict = defaultdict(int)
totalVotes = 0

with open(csvpath, newline='') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')

	next(csvreader, None)
	for row in csvreader:		
		pollDict[row[2]] += 1
		totalVotes += 1


# Specify the file to write to
outpath = os.path.join('outpath', 'result_' + csvpath.rsplit('\\', 1)[1].rsplit('.',1)[0] + '.txt' )
# print(outpath)

# Open the file using "write" mode. Specify the variable to hold the contents
with open(outpath, 'w') as file:
	# headers
	file.write("Election Results\n")
	file.write("-----------------------------------\n")
	file.write("Total Votes: " + str(totalVotes) + '\n')
	file.write("-----------------------------------\n")
	print("Election Results")
	print("-----------------------------------")
	print("Total Votes: " + str(totalVotes))
	print("-----------------------------------")

	# candidate/percent won/votes won
	for key, value in pollDict.items():
		percent = round((value/totalVotes)*100, 1)
		print(key + ": " + str(percent) + "% (" + str(value) + ") ")
		file.write(key + ": " + str(percent) + "% (" + str(value) + ") \n")

	# found winner
	print("-----------------------------------")
	file.write("-----------------------------------\n")
	max_value = max(pollDict.values())
	max_key = str([k for k, v in pollDict.items() if v == max_value]).strip("[").strip("]").strip("'")
	print("Winner: " + str(max_key))
	print("-----------------------------------")
	file.write("Winner: " + str(max_key) + "\n")
	file.write("-----------------------------------\n")