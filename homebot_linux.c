#include <stdio.h> //standard input/output; for printf and scanf
#include <stdbool.h> //standard bool; for booleans
#include <stdlib.h> ///find out what this is for
#include <unistd.h> //for sleep/delay functions

int main(void) //main function
{
	int if_selection = 0, menu_selection = 0; //declares and initializes two variables
	bool program_running = true;
	
	system("clear");
	
	printf("Hello there! I'm HomeBot, your personal cooking helper! I'll help you with instructions, proportions, and pretty much everything cooking.");
	printf("So, first I need to ask you some questions so that I can assist you better.");
	sleep(2);
	printf("So I never got to ask, what's your name?");
	scanf(%s,name);
	print("Hello %s!", name);

	while (program_running)
	{	
		printf("MENU:\n\n1. Chicken\n2. Home-made Kraft Dinner\n3. Potatoes\n\n"); //Prints main menu
		
		scanf("%i", &menu_selection); //Continually scans for an integer typed by the user

		while (if_selection == 0)
		{
			switch (menu_selection)
			{
			case 1: //If the user types 1 (chicken)
				system("clear");
				printf("Well, chicken it is!\n\n");
				sleep(2);
				system("clear");

				printf("All right. Here\'s the first thing to do: preheat the oven to 400 degrees.\n\n");
				sleep(2);
				printf("Rub the chicken all over with salt and pepper. Then, cut slits in the chicken and tuck your herbs in.\n\n");
				sleep(2);
				printf("Now, put the diced lemon into the cavity.\n\n");
				sleep(2);
				printf("Put the chicken in a roasting pan, and put it in the oven with the cover on. Let it cook for one to one and a half hours, and then lower the temperature to 350 degrees.\n\n");
				sleep(2);
				printf("Keep it in until the internal temperature is 165 degrees.\n\n");
				sleep(2);
				printf("Once you have it out, you can start to pull it apart. Be careful! It\'s hot! Make sure to pull along the grain, not against it.\n\n");
				sleep(2);
				printf("You can now serve it in buns, or eat it by itself.\n\n");

				system("clear");
				break;
				
			case 2: //If user types 2 (kraft dinner)
				system("clear");
				printf("Alright, Kraft dinner!\n\n");
				sleep(2);
				system("clear");
				
				printf("First things first; bring a big pot of water to a boil. Cook 8 ounces of elbow noodles in the water (while it's boiling), making sure to stir until cooked but still firm to the bite, usually 8 minutes.\n\n");
				sleep(2);
				printf("Drain the noodles now. Melt a quarter cup butter in a pan over medium heat, and stir in a quarter cup all purpose flour and half a teaspoon salt until smooth (usually 5 minutes).\n\n");
				sleep(2);
				printf("Slowly pour 2 cups milk into the butter flour mixture while continuously stirring until the mix is smooth and bubbling.\n\n");
				sleep(2);
				printf("Add 2 cups shredded cheddar cheese to the milk mixture and stir until the mix is melted, usually 2 to 4 minutes.\n\n");
				sleep(2);
				printf("Stir the mixture into the noodles until the whole thing is coated.\n\n");
				sleep(1);
				printf("Now you can add a bit more pepper if you want. You can now serve it!\n\n");

				system("clear");
				break;
				
      		case 3: //If user types 3 (potatoes)
				system("clear");
				printf("Ok, let's have some potatoes!\n\n");
				sleep(2);
				system("clear");
				
				printf("Make sure to wash and scrub the potato. Prick it in several places with a fork.\n\n");
				sleep(2);
				printf("Cook in the microwave for 5 minutes. Then, turn it over and cook for 5 more minutes.\n\n");
				sleep(2);
				printf("Season it with as much pepper and salt as you'd like, and mash up the inside a bit with a fork. Top it with some butter and 2 tablespoons of cheese.\n\n");
				sleep(2);
				printf("Return it to the microwave and cook for about one more minute.\n\n");
				sleep(2);
				printf("Top it with more cheese, if you'd like, and sour cream, also optional. You can now serve it!\n\n");

				system("clear");
				break;
        
      		default: //If user doesn't type 1, 2, or 3
			system("clear");	
			
			printf("I'm sorry, you didn't enter a correct value. Please try again.\n\n");

			sleep(2);

			system("clear");

			break;
			}
		break;
		} //if_selection while
	} //main While
return 0;
} //main
