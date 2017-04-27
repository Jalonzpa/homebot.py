#!/usr/bin/python
import time
allgood=False

while not allgood:
        print "What is your favorite meal that you have? (Choose from: chicken, kraft dinner, or potatoes)"
        favmeal=raw_input()
        time.sleep(1)
        print "How often do you have that meal?"
        favmealfreq=raw_input()
        time.sleep(1)
        print "Does everyone in your family like that meal? (Answer in complete sentence)"
        favmealfam=raw_input()
        time.sleep(1)
        print "So you have %r %r, and %r." % (favmeal, favmealfreq, favmealfam.replace("my", "your"))
        time.sleep(2)

        if favmeal == 'chicken':
                 print "Your favorite meal is chicken, correct?"
                 allgood=True
        elif favmeal == 'kraft dinner':
                 print "Your favorite meal is Kraft dinner, correct?"
                 allgood=True
        elif favmeal == 'potatoes':
                 print "Your favorite meal is potatoes, correct?"
                 allgood=True
        else:
                 print "You didn't write either chicken, kraft dinner, or potato. Please try again."
                 allgood=False
                time.sleep(2)
print "How many times do you want me to help you make %s this week? (Answer with a number)" % favmeal
favmealweek=raw_input()
time.sleep(1)
print "Ok, I'll help you make %s %s times this week." % (favmeal, favmealweek)
time.sleep(1)
if favmeal=='chicken':
        print "You need these ingredients: a whole chicken, herbs like rosemary, chive, cilantro, or anything else, whole lemons, pepper, and salt. Do you have all these ingredients?"
        ingravailable=raw_input()
        time.sleep(1)
        if ingravailable=='yes':
                print "Great! You are all set for tonight."

        else:
                 print "All right. If you go get those ingredients, I'll help you when you get back. Deal?"
time.sleep(1)
if favmeal=='kraft dinner':
        print "You'll just need these 2 ingredients: elbow noodles, and cheese. Do you have those?"
        ingravailable=raw_input()
time.sleep(1)
        if ingravailable=='yes':
                print "Great! You are all set for tonight."

        else:
                 print "All right. If you go get those ingredients, I'll help you when you get back. Deal?"
time.sleep(1)
if favmeal=='potatoes':
        print "You need these ingredients: potatoes, cheese, sour cream, and bacon. Do you have those?"
        ingravailable=raw_input()
time.sleep(1)
        if ingravailable=='yes':
                print "Great! You are all set for tonight."
time.sleep(1)
        else:
                 print "All right. If you go get those ingredients, I'll help you when you get back. Deal?"
time.sleep(1)     
if favmeal=='chicken':
        print "All right. Here's the first thing to do: preheat the oven to 400 degrees."
        time.sleep(1)
        print "Rub the chicken all over with salt and pepper. Then, cut slits in the chicken and tuck your herbs in."
        time.sleep(1)
        print "Now, put the diced lemon into the cavity."
        time.sleep(1)
        print "Put the chicken in a roasting pan, and put it in the oven with the cover on. Let it cook for one to one and a half hours, and then lower the temperature to 350 degrees."
        time.sleep(1)
        print "Keep it in until the internal temperature is 165 degrees."
        time.sleep(1)
        print "Once you have it out, you can start to pull it apart. Be careful! It's hot! Make sure to pull along the grain, not against it."
        time.sleep(1)
        print "Or, if you wish, you can keep it whole and eat the You can now serve it in buns, or eat it by itself."     
