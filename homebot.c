#include <stdio.h> //standard input/output; for slow_print and scanf
#include <stdbool.h> //standard bool; for booleans
#include <stdlib.h> //find out what this is for
#include <unistd.h> //for sleep/delay functions
#include <string.h> //for slow_print fucntion

void slow_print (char *strprint);
void slow_print_wait (char *strprint);
void intro();
void chicken(void);
void kraftdinner(void);
void potatoes(void);

char ingredients = 'a';

int if_selection = 0, menu_selection = 0; //declares and initializes two variables


int fgetc(FILE *stream);

int main(void) //main function
{
	int if_selection = 0, menu_selection = 0; //declares and initializes two variables
	bool program_running = true;
    char name[20];
	int config = 0;

	FILE *settings;
	settings = fopen("settings.txt", "r");

	config = fgetc(settings);

	fclose(settings);

	system("clear");

	if (config == 'a')
	{
	intro();
	FILE *settings;
	settings = fopen("settings.txt", "w");
	fprintf(settings, "b");
	fclose(settings);
	}

	int fclose(FILE *);

	while (program_running)
	{	
		slow_print("MENU:\n\n1. Chicken\n2. Home-made Kraft Dinner\n3. Potatoes\n\n"); //Prints main menu
		
		scanf("%i", &menu_selection); //Continually scans for an integer typed by the user

		while (if_selection == 0)
		{
			switch (menu_selection)
			{
			case 1: //If the user types 1 (chicken)
				chicken();
				
				break;
				
			case 2: //If user types 2 (kraft dinner)
				kraftdinner();

				break;
				
      		case 3: //If user types 3 (potatoes)
				potatoes();
				
				break;
        
      		default: //If user doesn't type 1, 2, or 3
			system("clear");	
			slow_print("I'm sorry, you didn't enter a correct value. Please try again.\n\n");
			sleep(1);
			system("clear");

			break;
			}
		break;
		} //if_selection while
    } //main While

return 0;
} //main

void slow_print (char *strprint)
{
    int index;
    int string_length = strlen(strprint);
    
    for (index = 0; index < string_length; index++)
    {
        printf("%c", strprint[index]);
        fflush(stdout);
        usleep(20000);
    }
}

void slow_print_wait (char *strprint)
{
    bool instruction_wait = true;
    int index;
    int string_length = strlen(strprint);
    char complete = 'a';

    for (index = 0; index < string_length; index++)
    {
        printf("%c", strprint[index]);
        fflush(stdout);
        usleep(20000);
    }
    
    while (instruction_wait)
    {
        scanf("%c", &complete);
        if (complete == 'y' || complete == 'Y')
        {
            instruction_wait = false;
            system("clear");
        }
        fflush(stdout);
    }

}

void intro(void)
{
	bool program_running = true;
    char name[20];
	
	system("clear");

	slow_print("Hello there! I'm HomeBot, your personal cooking helper! I'll help you with instructions, proportions, and pretty much everything cooking.\n");
	slow_print("So, first I need to ask you some questions so that I can assist you better.");
    sleep(2);
    system("clear");
	slow_print("I never got to ask, what's your name?\n");
	scanf("%s", name);
    slow_print("Hello, "); 
	slow_print(name);
	slow_print("!");

    sleep(1);
	system("clear");
	
}

void chicken(void)
{
	system("clear");
	slow_print("Well, chicken it is!\n\n");
	sleep(1);
	system("clear");

	slow_print("Alright, so if you want some great home-made chicken, you're gonna need these ingredients:\n\n");
	slow_print("1. Whole chicken\n2. Herbs like rosemary, chive, cilantro, etc.\n3. Whole lemon\n4. Pepper and salt\n\n");
	slow_print("\nDo you have all of those?\n\n");
	
	if (getchar() == 89 || getchar() == 121)
	{
		slow_print("\nGreat! You're all set.\n");
		sleep(1);
		system("clear");
	}
	else
	{
		slow_print("Ok, I'll help you make chicken once you get those ingredients.");
		sleep(1);
		system("clear");
		return;
	}

	slow_print_wait("All right. Here\'s the first thing to do: preheat the oven to 400 degrees.\n\n");
	sleep(1);
	slow_print_wait("Rub the chicken all over with salt and pepper. Then, cut slits in the chicken and tuck your herbs in.\n\n");
	sleep(1);
	slow_print_wait("Now, put the diced lemon into the cavity.\n\n");
	sleep(1);
	slow_print_wait("Put the chicken in a roasting pan, and put it in the oven with the cover on. Let it cook for one to one and a half hours, and then lower the temperature to 350 degrees.\n\n");
	sleep(1);
	slow_print_wait("Keep it in until the internal temperature is 165 degrees.\n\n");
	sleep(1);
	slow_print_wait("Once you have it out, you can start to pull it apart. Be careful! It\'s hot! Make sure to pull along the grain, not against it.\n\n");
	sleep(1);
	slow_print_wait("You can now serve it in buns, or eat it by itself.\n\n");

	system("clear");
}

void kraftdinner(void)
{
	system("clear");
	slow_print("Alright, Kraft dinner!\n\n");
	sleep(1);
	system("clear");

	slow_print("Ok, here are the ingredients that you need for kraft dinner:\n\n");
	slow_print("1. One cup elbow noodles\n2. Quarter cup butter\n3. A quarter cup of all-purpose butter\n4. Half a teaspoon of salt\n5. Two cups of milk\n6. 2 Two cups of shredded cheese (cheddar works best)\n7. Pepper and salt\n\n");
	slow_print("Do you have all of those ingredients?\n\n");
	
	if (getchar() == 89 || getchar() == 121)
	{
		slow_print("\nGreat! You're all set.\n");
		sleep(1);
		system("clear");
	}
	else
	{
		slow_print("Ok, I'll help you make chicken once you get those ingredients.");
		sleep(1);
		system("clear");
		return;
	}

	slow_print_wait("First things first; bring a big pot of water to a boil. Cook the elbow noodles in the water (while it's boiling), making sure to stir until cooked but still firm to the bite, usually 8 minutes.\n\n");
	sleep(1);
	slow_print_wait("Drain the noodles now. Melt the butter in a pan over medium heat, and stir the all purpose flour and salt until smooth (usually 5 minutes).\n\n");
	sleep(1);
	slow_print_wait("Slowly pour the milk into the butter flour mixture while continuously stirring until the mix is smooth and bubbling.\n\n");
	sleep(1);
	slow_print_wait("Add shredded cheddar cheese to the milk mixture and stir until the mix is melted, usually 2 to 4 minutes.\n\n");
	sleep(1);
	slow_print_wait("Stir the mixture into the noodles until everything is coated.\n\n");
	sleep(1);
	slow_print_wait("Now you can add a bit more pepper if you want. You can now serve it!\n\n");

	system("clear");
}

void potatoes(void)
{
	system("clear");
	slow_print("Ok, let's have some potatoes!\n\n");
	sleep(1);
	system("clear");
	
	slow_print("First, let's check out the ingredients list to make sure you have everything.\n");
	slow_print("You'll need very little things for this simple meal, but you can always add more if you'd like.\n\n");
	sleep(2);
	system("clear");

	slow_print("You'll need:\n\n1. Potatoes\n2. About two tablespoons of cheese\n3. Salt and pepper\n4. Sour cream\n\n");
	slow_print("Do you have everything?\n\n");

	if (getchar() == 89 || getchar() == 121)
	{
		slow_print("\nGreat! You're all set.\n");
		sleep(1);
		system("clear");
	}
	else
	{
		slow_print("Ok, I'll help you make chicken once you get those ingredients.");
		sleep(1);
		system("clear");
		return;
	}

	slow_print_wait("Make sure to wash and scrub the potato. Prick it in several places with a fork.\n\n");
	sleep(1);
	slow_print_wait("Cook in the microwave for 5 minutes. Then, turn it over and cook for 5 more minutes.\n\n");
	sleep(1);
	slow_print_wait("Season it with as much pepper and salt as you'd like, and mash up the inside a bit with a fork. Top it with some butter and a bit of cheese.\n\n");
	sleep(1);
	slow_print_wait("Return it to the microwave and cook for about one more minute.\n\n");
	sleep(1);
	slow_print_wait("Top it with more cheese, if you'd like, and maybe some sour cream. You can now serve it!\n\n");

	system("clear");
}