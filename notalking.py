#!/usr/bin/python
# Sets and imports everything needed to make the program run
import time
import os
import sys
allgood=False
allgood2=False
allgood3=False
favmeal=""
freq=""
famlike=""
ingravailable=""

def main():
    # Asks the user questions
    def questions():
        print("First, What is your favorite meal? Choose from chicken, kraft dinner, or potatoes.")
        global favmeal
        favmeal=raw_input()
        print("Second, how often do you have that meal?")
        global freq
        freq=raw_input()
        print("Third, does everyone in your family like that meal?")
        global famlike
        famlike=raw_input()
        print("So you have %r %r, and %r." % (favmeal, freq, famlike.replace("yes", "everyone in your family likes %s") % (favmeal)))
    # Checks if the favorite meal is correct
    def favmealcheck():
        global allgood
        while not allgood:
            if favmeal == 'chicken':
                print("Your favorite meal is chicken, correct?")
                allgood=True
            elif favmeal == 'kraft dinner':
                print("Your favorite meal is Kraft dinner, correct?")
                allgood=True
            elif favmeal == 'potatoes':
                print("Your favorite meal is potatoes, correct?")
                allgood=True
            else:
                print("You didn't write either chicken, kraft dinner, or potatoes. Please try again.")
                allgood=False
    # Tells the user what ingredients they need
    def ingredients():
        time.sleep(1)
        global allgood2
        global ingravailable
        while not allgood2:
            if favmeal == 'chicken':
                print("You need these ingredients: a whole chicken, herbs like rosemary, chive, cilantro, or anything else, whole lemons, pepper, and salt. Do you have all these ingredients?")
                ingravailable=raw_input()
                time.sleep(1)
                allgood2=True
            elif favmeal == 'kraft dinner':
                print("You'll just need these 3 ingredients: elbow noodles, breadcrumbs, and cheese. Do you have those?")
                ingravailable=raw_input()
                time.sleep(1)
                allgood2=True
            elif favmeal == 'potatoes':
                print("You need these ingredients: potatoes, cheese, sour cream, and bacon. Do you have those?")
                ingravailable=raw_input()
                time.sleep(1)
                allgood2=True
    # Talks to the user about their ingredients, or lack thereof
    def ingrcheck():
        global allgood3
        global ingravailable
        while not allgood3:
            if ingravailable == 'yes':
                print("Great! You are all set for tonight.")
                allgood3=True
            elif ingravailable == 'no':
                print("All right. If you go get those ingredients, I'll help you when you get back. Deal?")
                allgood3=True
		sys.exit()
            else:
                talk("You need to enter in something.")
                allgood3=False
    # Gives the user instructions on how to cook their meal
    def instructions():
        if favmeal == 'chicken':
            print("All right. Here's the first thing to do: preheat the oven to 400 degrees.")
            time.sleep(4)
            print("Rub the chicken all over with salt and pepper. Then, cut slits in the chicken and tuck your herbs in.")
            time.sleep(4)
            print("Now, put the diced lemon into the cavity.")
            time.sleep(4)
            print("Put the chicken in a roasting pan, and put it in the oven with the cover on. Let it cook for one to one and a half hours, and then lower the temperature to 350 degrees.")
            time.sleep(4)
            print("Keep it in until the internal temperature is 165 degrees.")
            time.sleep(4)
            print("Once you have it out, you can start to pull it apart. Be careful! It's hot! Make sure to pull along the grain, not against it.")
            time.sleep(4)
            print("You can now serve it in buns, or eat it by itself.")
        elif favmeal == 'kraft dinner':
            print("First things first; bring a big pot of water to a boil. Cook 8 ounces of elbow noodles in the water (while it's boiling), making sure to stir until cooked but still firm to the bite, usually 8 minutes.")
            time.sleep(4)
            print("Drain the noodles now. Melt a quarter cup butter in a pan over medium heat, and stir in a quarter cup all purpose flour and half a teaspoon salt until smooth (usually 5 minutes).")
            time.sleep(4)
            print("Slowly pour 2 cups milk into the butter flour mixture whule continuously stirring until the mix is smooth and bubbling.")
            time.sleep(4)
            print("Add 2 cups shredded cheddar cheese to the milk mixture and stir until the mix is melted, usually 2 to 4 minutes.")
            time.sleep(4)
            print("Stir the mixture into the noodles until the whole thing is coated.")
            time.sleep(2)
            print("Now you can add a bit more pepper if you want. You can now serve it!")
        elif favmeal == 'potatoes':
            print("Make sure to wash and scrub the potato. Prick it in several places with a fork.")
            time.sleep(3)
            print("Cook in the microwave for 5 minutes. Then, turn it over and cook for 5 more minutes.")
            time.sleep(3)
            print("Season it with as much pepper and salt as you'd like, and mash up the inside a bit with a fork. Top it with some butter and 2 tablespoons of cheese.")
            time.sleep(4)
            print("Return it to the microwave and cook for about one more minute.")
            time.sleep(2)
            print("Top it with more cheese, if you'd like, and sour cream, also optional. You can now serve it!")

    # Introduction
    print("Hello! I am HomeBot, your personal cooking helper. I will help you with all your cooking needs, help set reminders, and also helping you text people while you are cooking so you don't get your phone dirty.")
    time.sleep(3)
    print("So, first I need to ask you some questions.")
    time.sleep(2)
    
    questions()
    favmealcheck()

    print("How many times do you want me to help you make %s this week? (Answer with a number.)" % favmeal)
    timeweek=raw_input()
    time.sleep(1)
    print("Ok, I'll help you make %s %s times this week." % (favmeal, timeweek))


    ingredients()
    ingrcheck()
    instructions()

if __name__ == "__main__":
    main()
