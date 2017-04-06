#!/usr/bin/python
allgood=False

while not allgood:
        print "What is your favorite meal that you have? (Choose from: chicken, kraft dinner, or potatoes)"
        favmeal=raw_input()

        print "How often do you have that meal?"
        favmealfreq=raw_input()

        print "Does everyone in your family like that meal? (Answer in complete sentence)"
        favmealfam=raw_input()

        print "So you have %r %r, and %r." % (favmeal, favmealfreq, favmealfam.replace("my", "your"))


        if favmeal == 'chicken':
                 print "Your favorite meal is chicken."
                 allgood=True
        elif favmeal == 'kraft dinner':
                 print "Your favorite meal is Kraft dinner."
                 allgood=True
        elif favmeal == 'potatoes':
                 print "Your favorite meal is potatoes."
                 allgood=True
        else:
                 print "You didn't write either chicken, kraft dinner, or potato. Please try again."
                 allgood=False

print "How many times do you want me to help you make %s this week?" % favmeal
favmealweek=raw_input()

print "Ok, I'll help you make %s %s times this week." % (favmeal, favmealweek)

if favmeal=='chicken':
        print "You need these ingredients: a whole chicken, herbs like rosemary, chive, cilantro, or anything else, whole lemons, pepper, and salt. Do you have all these ingredients?"
        ingravailable=raw_input()

        if ingravailable=='yes':
                print "Great! You are all set for tonight."

        else:
                 print "All right. If you go get those ingredients, I'll help you when you get back. Deal?"

if favmeal=='kraft dinner':
        print "You'll just need these 2 ingredients: elbow noodles, and cheese. Do you have those?"
        ingravailable=raw_input()

        if ingravailable=='yes':
                print "Great! You are all set for tonight."

        else:
                 print "All right. If you go get those ingredients, I'll help you when you get back. Deal?"

if favmeal=='potatoes':
        print "You need these ingredients: potatoes, cheese, sour cream, and bacon. Do you have those?"
        ingravailable=raw_input()

        if ingravailable=='yes':
                print "Great! You are all set for tonight."

        else:
                 print "All right. If you go get those ingredients, I'll help you when you get back. Deal?"
                        
if favmeal=='chicken':
        print "All right. Here's the first thing to do: preheat the oven to 400 degrees."
        print "Rub the chicken all over with salt and pepper. Then, cut slits in the chicken and tuck your herbs in."
        print "Now, put the diced lemon into the cavity."
        print "Put the chicken in a roasting pan, and put it in the oven with the cover on. Let it cook for one to one and a half hours, and then lower the temperature to 350 degrees."
        print "Keep it in until the internal temperature is 165 degrees."
        print "Once you have it out, you can start to pull it apart. Be careful! It's hot! Make sure to pull along the grain, not against it."
        print "Or, if you wish, you can keep it whole and eat the You can now serve it in buns, or eat it by itself."
