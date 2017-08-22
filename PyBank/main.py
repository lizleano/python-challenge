# main.py
import os
import csv


bankDates = []
bankRevenue = []
nbrOfMonths = 0
totalRevenue = 0
average = 0.00
minimum = 0
maximum = 0

# print("Please place files in Resources directory")
# strfile = input("Enter filename you want to analyze: example <budget_data_1.csv> ")

strfile = "budget_data_2.csv"

csvpath = os.path.join('Resources', strfile)

with open(csvpath, newline='') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')

	next(csvreader, None)
	for row in csvreader:
		bankDates.append(row[0])
		bankRevenue.append(int(row[1]))
		
print("Financial Ananlysis")
print("-----------------------------------")
#total number of months
nbrOfMonths = len(bankDates)
print("Total Months: " + str(nbrOfMonths))

#total amount of revenue gained for entire period
totalRevenue = sum(bankRevenue)
print("Total Revenue: $" + str(totalRevenue))

#the average change in revenue between months over entire period
average = int(totalRevenue / nbrOfMonths)
print("Average Revenue Change: $" + str(average))

# greatest increase in revenue (date and amount)
increase = max(bankRevenue)
i = int(bankRevenue.index(increase))
print("Greatest increase in Revenue: " + bankDates[i] + " ($" + str(increase) + ")")

# greatest decrease in revenue (date and amount)
decrease = min(bankRevenue)
d = int(bankRevenue.index(decrease))
# print(idx)
# print(bankDates[idx])
print("Greatest decrease in Revenue: " + bankDates[d] + " ($" + str(decrease) + ")")


# print(csvpath)
# Specify the file to write to
outpath = os.path.join('outpath', 'result_' + csvpath.rsplit('\\', 1)[1].rsplit('.',1)[0] + '.txt' )
# print(outpath)

# Open the file using "write" mode. Specify the variable to hold the contents
with open(outpath, 'w') as file:
	file.write("Financial Ananlysis\n")
	file.write("-----------------------------------\n")
	file.write("Total Months: " + str(nbrOfMonths) + "\n")
	file.write("Total Revenue: $" + str(totalRevenue) + "\n")
	file.write("Average Revenue Change: $" + str(average) + "\n")
	file.write("Greatest Increase in Revenue: " + bankDates[i] + " ($" + str(increase) + ")" + "\n")
	file.write("Greatest Decrease in Revenue: " + bankDates[d] + " ($" + str(decrease) + ")" + "\n")