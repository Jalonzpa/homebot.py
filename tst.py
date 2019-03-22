import time
import config
import os

os.system("clear")

done = False
meal = input("What are we having for supper tonight?\n")
number = 0

with open("instructions.txt") as f:
	lines = f.readlines()

lines = [line.rstrip('\n') for line in open("instructions.txt")]

if meal == "chicken":
        for i in config.chicken:
                print(lines[i])
                input("\nPress [Enter] to continue.\n")
if meal == "kraft dinner":
	for i in config.kd:
		print(lines[i])
		input("\nPress [Enter] to continue.\n")
if meal == "potatoes":
        for i in config.potatoes:
                print(lines[i])
                input("\nPress [Enter] to continue.\n")
#if meal == "chicken":
#	while done == False:
#		print(lines[config.chicken[number]])
#		input("\nPress [Enter] to continue.\n")
#		number += 1
#		if number == config.chicken[-1]:
#			done = True
#if meal == "kraft dinner":
#	while done == False:
#		print(lines[config.kd[number]])
#		input("\nPress [Enter] to continue.\n")
#		number += 1
#		if number == config.kd[-1]:
#			done = True
#if meal == "potatoes":
#	while done == False:
#		print(lines[config.potatoes[number]])
#		input("\nPress [Enter] to continue.\n")
#		number += 1
#		if number == config.potatoes[-1]:
#			done = True
#while True:
#	print(lines[number])
#	time.sleep(5)
#	input("\nPress [Enter] to continue.\n")
#	number += 1
