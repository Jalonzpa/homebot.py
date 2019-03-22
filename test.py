import time

number = 0

with open('instructions.txt') as f:
    lines = f.readlines()

while True:
	print lines[number]
	time.sleep(1)
	input("\n\nPress [Enter] to continue.\n")
	number += 1
