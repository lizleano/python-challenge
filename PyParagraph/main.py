# main.py
import os
import csv
import re

wordCount = []
words = []
sCount = 0
wCount = 0

# print("Please place files in Resources directory")
# strfile = input("Enter filename you want to analyze: example <budget_data_1.csv> ")

# inputfile = os.path.join('Resources', strfile)
inputfile = os.path.join('Resources', 'paragraph_2.txt')

with open(inputfile,'r', encoding="utf-8") as f:
	# # count sentences
	for line in f:
		# print(line)

		arrSentence = re.split("(?<=[.!?]) +", line.strip())
		arrSentence = list(filter(None, arrSentence))
		# print(len(arrSentence))
		sCount = sCount + len(arrSentence)

		# Extends list by appending elements from the iterable
		words.extend(line.strip().split(" "))
		# print(arrSentence)

# print (sCount)
# print (len(words))
# remove all word that's empty
for word in words:
	if word == "":
		words.remove(word)

# # count words
for word in words:
	# print(word + " " + str(len(word)))
	# print(word + " " + str(len(re.findall('[0-9a-zA-Z]', word))))
	# wordCount.append(len(re.findall('[0-9a-zA-Z]', word)))
	wordCount.append(len(word))

totalLetters = sum(wordCount)
# print(totalLetters)

print("Paragraph Analysis")
print("-----------------------------------")

# Approximate word count
wCount = len(words)
print("Approximate Word Count: " + str(wCount))

# Approximate sentence count
# sCount = len(arrSentence)
print("Approximate Sentence Count: " + str(sCount))

# Average Letter Count
avgLetter = sum(wordCount)/float(wCount)
print("Average Letter Count: " + str(avgLetter))

# Average Sentence Length
avgSentence = float(wCount/sCount)
print("Average Sentence Length: " + str(avgSentence))

# Specify the file to write to
outpath = os.path.join('outpath', 'result_' + inputfile.rsplit('\\', 1)[1].rsplit('.',1)[0] + '.txt' )
# print(outpath)
# Open the file using "write" mode. Specify the variable to hold the contents
with open(outpath, 'w') as file:
	file.write("Paragraph Analysis\n")
	file.write("-----------------------------------\n")
	file.write("Approximate Word Count: " + str(wCount) + "\n")
	file.write("Approximate Sentence Count: " + str(sCount) + "\n")
	file.write("Average Letter Count: " + str(avgLetter) + "\n")
	file.write("Average Sentence Length: " + str(avgSentence) + "\n")