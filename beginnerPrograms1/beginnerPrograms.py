#this program lists a bunch of different beginner projects try to make when you don't know what to do.

beginList = [
    "Guessing Game",
    "Dice Roll Simulator",
    "Currency Converter",
    "Word Counter",
    "Higher or Lower",
    "Rock Paper Scissors",
    "Binary Search Algorithm",
    "Countdown Timer",
    "Interactive Quiz",
    "Hangman",
    "Max Arrangments",
    "Calculator"
]
beginlistInfo = [
    "Guessing Game - Create a game where a random number from 1 to x is chosen and the user can input their guess. Give them a certain amount of lives.",
    "Dice Roll Simulator - Create a game where 2 or more dice are rolled with their values printed, then added together.",
    "Interactive Quiz - Create a game that asks general knowledge questions and gives the user 3 options to choose from.",
    "Currency Converter - Create a program that can convert a currency of your choice to another.",
    "Word Counter - Create a program that lets the user input sentences, then counts how many words they typed.",
    "Rock Paper Scissors - Create a classic rock-paper-scissors game that is versus the computer.",
    "Hangman - Create a classic hangman game where a random word is chosen, and the user guesses letters. 8 lives before user loses.",
    "Countdown Timer - Create a timer that counts down from a time the user inputs.",
    "Binary Search Algorithm",
    "Max Arrangments - Create a program that lets the user input x amount of numbers, then tell them how many different ways they can be arranged.",
    "Calculator - Create a fully functioning calculator.",
    "Higher or Lower - Generate a random number from 1-100 and have the user guess. If the number is higher than answer say go lower, if number is lower say go higher."
]
print("Welcome to the program catalog. Here are all the project ideas we have. ")
for i, char in enumerate(beginList):
    print(i+1, beginList[i])
    
def main():
    getInfo = str(input(f'Would you like to get project info, submit a completion or exit?.\nEnter 1 for project info. Enter 2 to submit a completion. Anything else will exit. '))
    if getInfo == "1":
        projectChoice = int(input(f'Type in a number to see more information about each project. '))
        projectChoice -= 1
        while projectChoice < 0 or projectChoice >= len(beginlistInfo):
                print("That isn't a valid choice.")
                projectChoice = int(input("Please choose a valid project number. "))
                projectChoice -= 1
        review = "y"
        while review == "y":
            for i in beginlistInfo:
                l = beginList[int(projectChoice)]
                if l in i:
                    print(f'\n{i}')   
            review = input("Do you want to view another project? Enter 'y' for yes, and 'n' for no. ")   
            if review == "y":
                    projectChoice = int(input("Enter the next project number you'd like to view. "))
                    projectChoice -= 1
                    while projectChoice < 0 or projectChoice >= len(beginlistInfo):
                        print("That isn't a valid choice.")
                        projectChoice = int(input("Please choose a valid project number. "))
                        projectChoice -= 1            
    elif getInfo == "2":
        file_path = "c:/Users/tempuser/Desktop/Projects/beginnerPrograms/completedPrograms.txt"
        dupeComplete = True
        print(f'If you have finished a project you can submit it here to be saved.\n')
        completedProject = int(input("Enter the number of which project you completed. "))
        completedProject -= 1
        for comp in beginList:
            while completedProject < 0 or completedProject >= len(beginList):
                print("That value is outside of the range, please enter a valid number.")
                completedProject = int(input("Enter the number of which project you completed. "))
                completedProject -= 1
            l = beginList[int(completedProject)]
            if l in comp:
                with open(file_path, 'r') as file:
                    for line in file:
                        if comp in line:
                            break
                    else: 
                        dupeComplete = False
        if dupeComplete == True:
            print("You already submitted this project as complete.")
        else:
            print(f'Saving {l}.')
            with open(file_path, 'a') as file:
                file.write(f'\nYou completed: {l}')
    else:
        print("Goodbye")
main()