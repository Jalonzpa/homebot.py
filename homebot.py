#!/usr/bin/python
# Sets and imports everything needed to make the program run
import time
import os
import sys
ingravailable=""
favmeal = ""

def main():
    print("Main")

# Checks if the file exists
    if os.path.exists("/home/chip/homebot_code/donealready.txt"):
        print("reading")
# Reads the file
        file_reading = open("donealready.txt", "r")
        read = file_reading.read()
        file_reading.close()
        print(read)
# If the file reads "done", it skips the intro and goes straight to instructions
        if read == "done":
            instructions()
# Otherwise, it goes from the start, and writes "done" so it won't repeat it next time the program is run
    else:
        print("Writing")
        file_write = open("donealready.txt", "w")
        file_write.write("done")
        file_write.close()

        talk("Hello. I am HomeBot, your personal cooking helper. I will help you with all your cooking needs, set reminders, and help you text people while you are cooking so you don't get your phone dirty.")
        talk("But first, I need to ask you some questions.")

        questions()
        favmealcheck()

        talk("How many times do you want me to help you make %s this week? (Answer with a number.)" % favmeal)
        timeweek = raw_input()
        time.sleep(1)
        talk("Ok, I'll help you make %s %s times this week." % (favmeal, timeweek))

        ingredients()
        ingrcheck()
# Lets HomeBot talk
def talk(my_string):
    os.system('/usr/bin/flite -t "' + my_string + '"')
# Asks the user questions
def questions():
    global favmeal
    freq = ""
    famlike = ""
    
    print("questions")
    talk("First, What is your favorite meal? Choose from chicken, kraft dinner, or potatoes.")
    favmeal = raw_input()
    favmeal_write = open("favmeal.txt", "w")
    favmeal_write.write('%r' % (favmeal))
    favmeal_write.close()

    talk("Second, how often do you have that meal?")
    freq=raw_input()
    talk("Third, does everyone in your family like that meal?")
    famlike=raw_input()
    talk("So you have %r %r, and %r." % (favmeal, freq, famlike.replace("yes", "everyone in your family likes %s") % (favmeal)))
    print("end questions")
# Checks if the favorite meal is correct
def favmealcheck():
    global favmeal
    allgood = False

    print("favmealcheck")
    while not allgood:
        if favmeal == 'chicken':
            talk("Your favorite meal is chicken, correct?")
	    correct=raw_input()
            if correct == 'yes':
                allgood=True
            else:
	        questions()
        
	elif favmeal == 'kraft dinner':
            talk("Your favorite meal is Kraft dinner, correct?")
            correct=raw_input()
            if correct == 'yes':
	         allgood=True
            else:
		questions()
        elif favmeal == 'potatoes':
            talk("Your favorite meal is potatoes, correct?")
            correct=raw_input()    
	    if correct == 'yes':
               allgood=True
               questions()
            else:
                talk("You didn't write either chicken, kraft dinner, or potatoes. Please try again.")
                allgood=False
		
	print("end favmealcheck")
# Tells the user what ingredients they need
def ingredients():
    allgood2 = False

    print("ingredients")
    while not allgood2:
        if favmeal == 'chicken':
            talk("You need these ingredients: a whole chicken, herbs like rosemary, chive, cilantro, or anything else, whole lemons, pepper, and salt. Do you have all these ingredients?")
            ingravailable=raw_input()
            time.sleep(1)
            allgood2=True
        elif favmeal == 'kraft dinner':
            talk("You'll just need these 3 ingredients: elbow noodles, breadcrumbs, and cheese. Do you have those?")
            ingravailable=raw_input()
            time.sleep(1)
            allgood2=True
        elif favmeal == 'potatoes':
            talk("You need these ingredients: potatoes, cheese, sour cream, and bacon. Do you have those?")
            ingravailable=raw_input()
            time.sleep(1)
            allgood2=True
	
    print ("end ingredients")
# Talks to the user about their ingredients, or lack thereof
def ingrcheck():
    allgood3 = False
    global ingravailable

    print("ingrcheck")
    global ingravailable
    while not allgood3:
        if ingravailable == 'yes':
            talk("Great! You are all set for tonight.")
            allgood3 = True
	    sys.exit()
        elif ingravailable == 'no':
            talk("All right. If you go get those ingredients, I'll help you when you get back. Deal?")
            allgood3 = True
            sys.exit()
        else:
	    allgood3 = False
	
	print("end ingrcheck")
    # Gives the user instructions on how to cook their meal
def instructions():
    print("Instruction read")
    favmeal_read = open("favmeal.txt", "r")
    favmealins = favmeal_read.read()
    print(favmealins)
    favmeal_read.close()

    print("instructions")
    if favmealins == 'chicken':
        talk("All right. Here's the first thing to do: preheat the oven to 400 degrees.")
        time.sleep(2)
        talk("Rub the chicken all over with salt and pepper. Then, cut slits in the chicken and tuck your herbs in.")
        time.sleep(2)
        talk("Now, put the diced lemon into the cavity.")
        time.sleep(2)
        talk("Put the chicken in a roasting pan, and put it in the oven with the cover on. Let it cook for one to one and a half hours, and then lower the temperature to 350 degrees.")
        time.sleep(2)
        talk("Keep it in until the internal temperature is 165 degrees.")
        time.sleep(2)
        talk("Once you have it out, you can start to pull it apart. Be careful! It's hot! Make sure to pull along the grain, not against it.")
        time.sleep(2)
        talk("You can now serve it in buns, or eat it by itself.")
    elif favmealins == 'kraft dinner':
        talk("First things first; bring a big pot of water to a boil. Cook 8 ounces of elbow noodles in the water (while it's boiling), making sure to stir until cooked but still firm to the bite, usually 8 minutes.")
        time.sleep(2)
        talk("Drain the noodles now. Melt a quarter cup butter in a pan over medium heat, and stir in a quarter cup all purpose flour and half a teaspoon salt until smooth (usually 5 minutes).")
        time.sleep(2)
        talk("Slowly pour 2 cups milk into the butter flour mixture whule continuously stirring until the mix is smooth and bubbling.")
        time.sleep(2)
        talk("Add 2 cups shredded cheddar cheese to the milk mixture and stir until the mix is melted, usually 2 to 4 minutes.")
        time.sleep(2)
        talk("Stir the mixture into the noodles until the whole thing is coated.")
        time.sleep(1)
        time.sleep(1)
        talk("Now you can add a bit more pepper if you want. You can now serve it!")
    elif favmealins == 'potatoes':
        talk("Make sure to wash and scrub the potato. Prick it in several places with a fork.")
        time.sleep(1)
        talk("Cook in the microwave for 5 minutes. Then, turn it over and cook for 5 more minutes.")
        time.sleep(2)   
        talk("Season it with as much pepper and salt as you'd like, and mash up the inside a bit with a fork. Top it with some butter and 2 tablespoons of cheese.")
        time.sleep(2)
        talk("Return it to the microwave and cook for about one more minute.")
        time.sleep(1)
        talk("Top it with more cheese, if you'd like, and sour cream, also optional. You can now serve it!")

    print("end instructions")

def repeatcheck():
    read = ""

    if os.path.exists("/home/chip/homebot_code/donealready.txt"):
        file_write1 = open("donealready.txt", "w")
	file_write1.write("")
        file_write1.close()
    else:
	print("reading")
        file_reading = open("donealready.txt", "r")
        read = file_reading.read()
        file_reading.close()

    if read == "done":
        instructions()
    else:
        print("Writing")
        file_write = open("donealready.txt", "w")
        file_write.write("done")
        file_write.close()

	talk("Hello. I am HomeBot, your personal cooking helper. I will help you with all your cooking needs, set reminders, and help you text people while you are cooking so you don't get your phone dirty.")
	talk("But first, I need to ask you some questions.")

        questions()
        favmealcheck()
  
        talk("How many times do you want me to help you make %s this week? (Answer with a number.)" % favmeal)
        timeweek=raw_input()
        time.sleep(1)
        talk("Ok, I'll help you make %s %s times this week." % (favmeal, freq))

        ingredients()
        ingrcheck()


if __name__ == "__main__":
    main()
    print("Main")
