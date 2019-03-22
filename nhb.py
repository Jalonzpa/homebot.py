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
#Asks user baseline questions
    def questions():
        os.system("clear")
        sprint("So, what do you want tonight? ")
        sprint("We have a few things on the menu currently.\nType the number that corresponds with the food you want!\n")
        time.sleep(1)
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
        os.system("clear")
        global ingravailable
        if meal == 'chicken':
            sprint(config.ingredients["chicken"] + " (y/n)")
            ingravailable=input()
        elif meal == 'kraft dinner':
            sprint(config.ingredients["kd"] + " (y/n)")
            ingravailable=input()
            allgood2=True
        elif meal == 'potatoes':
            sprint(config.ingredients["potatoes"] + " (y/n)")
            ingravailable=input()
            allgood2=True
    # sprints to the user about their ingredients, or lack thereof
    def ingrcheck():
        global allgood3
        global ingravailable
        while not allgood3:
            if ingravailable == 'y':
                sprint("Great. You're all set!")
                allgood3=True
            elif ingravailable == 'n':
                sprint("All right. If you go get those ingredients, I'll help you when you get back. Deal?")
                allgood3=True
                sys.exit()
            else:
                sprint("Whoops! Something went wrong! Exiting...")
                sys.exit()
    # Gives the user instructions on how to cook their meal
    def instructions():
        os.system("clear")
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
    ingrcheck()
    instructions()

if __name__ == "__main__":
    main()
    print("Main")
