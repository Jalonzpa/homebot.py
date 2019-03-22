#!/usr/bin/python
# Sets and imports everything needed to make the program run
import time
import os
import sys
import config
allgood=False
allgood2=False
allgood3=False
meal=""
freq=""
famlike=""
ingravailable=""

with open("instructions.txt") as f:
        lines = f.readlines()

lines = [line.rstrip('\n') for line in open("instructions.txt")]
# Simple little script to enable scroll typing
def sprint(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.03)
os.system("clear")
sprint("Booting HomeBotOS...")
time.sleep(2)
os.system("clear")

def main():
    # Asks user baseline questions
    def questions():
        os.system("clear") # Clears the console screen
        sprint("So, what do you want tonight? ")
        sprint("We have a few things on the menu currently.\nType the number that corresponds with the food you want!\n")
        time.sleep(1) # Pauses for one second
        sprint("\n\nMENU:\n\n1. Chicken\n2. Kraft dinner\n3. Potatoes\n")
        global meal
        menu = input()
        if menu == "1":
            meal = "chicken"
        if menu == "2":
            meal = "kraft dinner"
        if menu == "3":
            meal = "potatoes"
        sprint("Awesome! I'll help you make %s." % (meal))
        time.sleep(1)
    # Tells the user what ingredients they need
    def ingredients():
        global ingravailable
        global ingredientcheck
        ingredientcheck = False
        while not ingredientcheck: # When the user says "y" or "n", ingredientcheck is equal to True, otherwise it repeats the function
            os.system("clear")
            if meal == 'chicken':
                sprint(config.ingredients["chicken"] + " (y/n)") # Pulls in ingredients from the config.py file and appends (y/n) to the end of it
                ingravailable=input()
            elif meal == 'kraft dinner':
                sprint(config.ingredients["kd"] + " (y/n)")
                ingravailable=input()
            elif meal == 'potatoes':
                sprint(config.ingredients["potatoes"] + " (y/n)")
                ingravailable=input()

        # Tells the user whether they're good to go or not
            if ingravailable == 'y':
                sprint("Great. You're all set!")
                time.sleep(2)
                ingredientcheck = True
            elif ingravailable == 'n':
                sprint("All right. If you go get those ingredients, I'll help you when you get back. Deal?")
                ingredientcheck = True
                sys.exit()
            else:
                sprint("Whoops! Something went wrong! Try again.")
                time.sleep(2)
                ingredientcheck = False
    # Gives the user instructions on how to cook their food
    def instructions():
        os.system("clear")
        if meal == "chicken":
            for i in config.chicken: # Iterates over the line numbers in the config.py file
                sprint(lines[i]) # Prints one instruction line at a time
                print("\n\nPress [Enter] to continue.\n")
                input()
                os.system("clear")
        if meal == "kraft dinner":
            for i in config.kd:
                print(lines[i])
                sprint("\nPress [Enter] to continue.\n")
                input()
                os.system("clear")
        if meal == "potatoes":
            for i in config.potatoes:
                print(lines[i])
                sprint("\nPress [Enter] to continue.\n")
                input()
                os.system("clear")
# Introduction
    sprint("Hello! I am HomeBot, your personal cooking helper.\nI am going to help you with all your cooking needs! ")
    time.sleep(3)
    questions()

    sprint("\n\nHow many times do you want me to help you make %s this week? (Answer with a number.)\n" % meal)
    timeweek=input()
    time.sleep(1)
    sprint("\nOk, I'll help you make %s %s times this week." % (meal, timeweek))
    time.sleep(2)

    ingredients()
    instructions()

if __name__ == "__main__":
    main()
    print("Main")
