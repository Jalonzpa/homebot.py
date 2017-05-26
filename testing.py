#!/usr/bin/python
import time
import os
allgood=False
allgood2=False
def talk(my_string):
    os.system('/usr/bin/flite -t "' + my_string + '"')

talk("Hello! I am HomeBot, your personal cooking helper. I will help you with all your cooking needs, help set reminders, and also helping you text people while you are cooking so you don't get your phone  dirty.")
talk("So, first I need to ask you some questions.")

while not allgood:
    talk("First, What is your favorite meal? Choose from chicken, kraft dinner, or potatoes.")
    favmeal=raw_input()
    talk("Second, how often do you have that meal?")
    freq=raw_input()
    talk("Third, does everyone in your family like that meal?")
    famlike=raw_input()
    talk("So you have %r %r, and %r." % (favmeal, freq, famlike.replace("my", "your")))

    if favmeal == 'chicken':
        talk("Your favorite meal is chicken, correct?")
        allgood=True
    elif favmeal == 'kraft dinner':
        talk("Your favorite meal is Kraft dinner, correct?")
        allgood=True
    elif favmeal == 'potatoes':
        talk("Your favorite meal is potatoes, correct?")
        allgood=True
    else:
        talk("You didn't write either chicken, kraft dinner, or potatoes. Please try again.")
        allgood=False

talk("How many times do you want me to help you make %s this week? (Answer with a number.)" % favmeal)
timeweek=raw_input()
time.sleep(1)
talk("Ok, I'll help you make %s %s times this week." % (favmeal, freq))

while not allgood2:
    if favmeal== 'chicken':
        talk("You need these ingredients: a whole chicken, herbs like rosemary, chive, cilantro, or anything else, whole lemons, pepper, and salt. Do you have all these ingredients?")
        ingravailable=raw_input()
        time.sleep(1)
    elif favmeal== 'kraft dinner':
        talk("You'll just need these 3 ingredients: elbow noodles, breadcrumbs, and cheese. Do you have those?")
        ingravailable=raw_input()
        time.sleep(1)
    elif favmeal== 'potatoes':
        talk("You need these ingredients: potatoes, cheese, sour cream, and bacon. Do you have those?")
        ingravailable=raw_input()
        time.sleep(1)



    if ingravailable=='yes':
        talk("Great! You are all set for tonight.")
        allgood2=True
    elif ingravailable == 'no':
        talk("All right. If you go get those ingredients, I'll help you when you get back. Deal?")
        allgood2=True

    if favmeal=='chicken':
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
        talk("Or, if you wish, you can keep it whole and eat the You can now serve it in buns, or eat it by itself."
