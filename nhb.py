#!/usr/bin/python
# Sets and imports everything needed to make the program run
import time
import os
import sys
import config
allgood=False
allgood2=False
allgood3=False
favmeal=""
freq=""
famlike=""
ingravailable=""

def sprint(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.03)
os.system("clear")
sprint("Welcome to HomeBotOS!")
time.sleep(2)
os.system("clear")

def main():
#Asks user baseline questions
    def questions():
        os.system("clear")
	sprint("So, what do you want tonight?")
	sprint("We have a few things on the menu currently.\nType the number that corresponds with the food you want!\n")
	time.sleep(3)
	os.system("clear")
	print("MENU:\n\n1.Chicken\n2.Kraft dinner\n3.Potatoes\n")
        global favmeal
        menu=raw_input()
	if menu == "1":
		favmeal = "chicken"
	if menu == "2":
		favmeal = "kraft dinner"
	if menu == "3":
		favmeal = "potatoes"
	sprint("Awesome! I'll help you make %s." % (favmeal))
	time.sleep(1)
    # Tells the user what ingredients they need
    def ingredients():
	os.system("clear")
        global ingravailable
        if favmeal == 'chicken':
	    sprint(config.ingredients["chicken"])
            ingravailable=raw_input()
        elif favmeal == 'kraft dinner':
	    sprint(config.ingredients["kd"])
            ingravailable=raw_input()
            allgood2=True
        elif favmeal == 'potatoes':
	    sprint(config.ingredients["potatoes"])
            ingravailable=raw_input()
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
        if favmeal == 'chicken':
            sprint("All right. Here's the first thing to do: preheat the oven to 400 degrees.")
            time.sleep(2)
            sprint("Rub the chicken all over with salt and pepper. Then, cut slits in the chicken and tuck your herbs in.")
            time.sleep(2)
            sprint("Now, put the diced lemon into the cavity.")
            time.sleep(2)
            sprint("Put the chicken in a roasting pan, and put it in the oven with the cover on. Let it cook for one to one and a half hours, and then lower the temperature to 350 degrees.")
            time.sleep(2)
            sprint("Keep it in until the internal temperature is 165 degrees.")
            time.sleep(2)
            sprint("Once you have it out, you can start to pull it apart. Be careful! It's hot! Make sure to pull along the grain, not against it.")
            time.sleep(2)
            sprint("You can now serve it in buns, or eat it by itself.")
        elif favmeal == 'kraft dinner':
            sprint("First things first; bring a big pot of water to a boil. Cook 8 ounces of elbow noodles in the water (while it's boiling), making sure to stir until cooked but still firm to the bite, usually 8 minutes or so.")
            time.sleep(2)
            sprint("Drain the noodles now. Melt a quarter cup butter in a pan over medium heat, and stir in a quarter cup all purpose flour and half a teaspoon salt until smooth (usually 5 minutes).")
            time.sleep(2)
            sprint("Slowly pour 2 cups milk into the butter flour mixture whule continuously stirring until the mix is smooth and bubbling.")
            time.sleep(2)
            sprint("Add 2 cups shredded cheddar cheese to the milk mixture and stir until the mix is melted, usually 2 to 4 minutes.")
            time.sleep(2)
            sprint("Stir the mixture into the noodles until the whole thing is coated.")
            time.sleep(1)
            time.sleep(1)
            sprint("Now you can add a bit more pepper if you want. You can now serve it!")
        elif favmeal == 'potatoes':
            sprint("Make sure to wash and scrub the potato. Prick it in several places with a fork.")
            time.sleep(1)
            sprint("Cook in the microwave for 5 minutes. Then, turn it over and cook for 5 more minutes.")
            time.sleep(2)
            sprint("Season it with as much pepper and salt as you'd like, and mash up the inside a bit with a fork. Top it with some butter and 2 tablespoons of cheese.")
            time.sleep(2)
            sprint("Return it to the microwave and cook for about one more minute.")
            time.sleep(1)
            sprint("Top it with more cheese, if you'd like, and sour cream, also optional. You can now serve it!")

# Introduction
    sprint("Hello! I am HomeBot, your personal cooking helper.\n I am going to help you with all your cooking needs!")
    time.sleep(3)
    questions()

    sprint("How many times do you want me to help you make %s this week? (Answer with a number.)" % favmeal)
    timeweek=raw_input()
    time.sleep(1)
    sprint("Ok, I'll help you make %s %s times this week." % (favmeal, timeweek))


    ingredients()
    ingrcheck()
    instructions()

if __name__ == "__main__":
    main()
    print("Main")
