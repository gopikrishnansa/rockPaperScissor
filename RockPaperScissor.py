import random
import os
import time
import threading
user_score = 0  # Initialize user_score outside the function
system_score = 0  # Initialize system_score outside the function

'''def timer():
    for i in range(10, 0, -1):
        print(f"Time remaining: {i} seconds")
        print("Select your choice 1-rock, 2- paper, 3- scissor: ")
        time.sleep(1)
        os.system("clear")
    print("Time's up!")'''
def gameData():
    data = ["Rock","Paper","Scissor"]
    count = [0,1,2]
    global data_current
    global user_input
    data_current = random.choice(data)
    #print(data_current)


    while True:
        '''timer_thread = threading.Thread(target=timer())
        timer_thread.start()
        
        timer_thread.join()'''
        your_choice = input("Select your choice \n1- Rock, \n2- Paper, \n3- Scissor: \n")
        if your_choice == '1':
            user_input = 'Rock'
            print("user input is", user_input, ", \nsystem input is", data_current)
            break  # Exit the loop if a valid choice is made
        elif your_choice == '2':
            user_input = 'Paper'
            print("user input is", user_input, ", \nsystem input is", data_current)
            break  # Exit the loop if a valid choice is made
        elif your_choice == '3':
            user_input = 'Scissor'
            print("user input is", user_input, ", \nsystem input is", data_current)
            break  # Exit the loop if a valid choice is made
        else:
            print("Please choose a valid option (1, 2, or 3). Try again.")

def execution():

    gameData()
    global user_score  # Make user_score global
    global system_score  # Make system_score global
    if user_input == data_current:
        print("Try again")
    elif data_current == 'Rock' and user_input == 'Paper' :
        user_score = user_score +1
        #print("you won and your score is ", user_score)
    elif data_current == 'Rock' and user_input == 'Scissor' :
        system_score = system_score + 1
        #print("System won and the score is ", system_score)
    elif data_current == 'Paper' and user_input == 'Rock' :
        system_score = system_score + 1
        #print("System won and the score is ", system_score)
    elif data_current == 'Paper' and user_input == 'Scissor' :
        user_score = user_score + 1
        #print("you won and your score is ", user_score)
    elif data_current == 'Scissor' and user_input == 'Rock' :
        user_score = user_score + 1
        #print("you won and your score is ", user_score)
    elif data_current == 'Scissor' and user_input == 'Paper' :
        system_score = system_score + 1
        #print("System won and the score is ", system_score)

def table():
    headers = ["System", "You"]
    # Sample data
    data = [
        [system_score, user_score, ],
    ]
    # Print headers
    for header in headers:
        print(f"{header:<10}", end=" ")  # Adjust width as needed
    print()
    # Print a line separator
    print("-" * 20)
    # Print data rows
    for row in data:
        for value in row:
            print(f"{value:<10}", end=" ")  # Adjust width as needed
        print()




turn = int(input("enter how many tries you want for the game? "))
for i in range(0,turn):
    table()
    execution()
    time.sleep(2)
    os.system("clear")

if user_score > system_score:
    print("====================")
    print("You won")
    print("====================")
else:
    print("====================")
    print("system won")
    print("====================")

table()

