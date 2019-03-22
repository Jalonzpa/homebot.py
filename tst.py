import time
import config
import os

os.system("clear")

done = False
meal = input("What are we having for supper tonight?\n")
print(meal)
number = 0

with open("instructions.txt") as f:
	lines = f.readlines()

lines = [line.rstrip('\n') for line in open("instructions.txt")]


if meal == "chicken":
	while done == False:
		print(lines[config.chicken[number]])
		input("\nPress [Enter] to continue.\n")
		number += 1
		if number == config.chicken[6]:
			done = True
if meal == "kraft dinner":
	print(lines[config.kd[number]])
	input("\nPress [Enter] to continue.\n")
	number += 1
if meal == "potatoes":
	print(lines[config.potatoes[number]])
	number += 1
#while True:
#	print(lines[number])
#	time.sleep(5)
#	input("\nPress [Enter] to continue.\n")
#	number += 1
