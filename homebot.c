#include <stdio.h>
#include <stdbool.h>
#include <time.h>

void delay(int delaytime); //time function prototype

void main(void) //main function
{
	int if_selection = 0, menu_selection = 0; //declares and initializes two variables
	bool program_running = true;
	
	while (program_running)
	{	
		printf("MENU:\n\n1. Chicken\n2. Kraft Dinner\n3. Potatoes\n\n"); //Prints main menu
		
		scanf("%i", &menu_selection); //Continually scans for an integer typed by the user

		while (if_selection == 0)
		{
			switch (menu_selection)
			{
			case 1: //If the user types 1
				system("clear");
				printf("Well chicken it is!");
				delay(2);
				system("clear");

				//Give step by step recipe instructions for chicken.


				break;
			case 2: //If user types 2

				break;

      case 3: //If user types 3
      
        break;
        
      default: //If user doesn't type 1, 2, or 3
				printf("I'm sorry, you didn't enter a correct value. Please try again.\n\n");

				delay(2);

				system("clear");

				break;
			}
			break;
		}
	} //Main While

} //Main

void delay(int delaytime)
{
	int Time;

	Time = time(0) + delaytime;

	while (time(0) != Time)
	{

	}

}
