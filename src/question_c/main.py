#add import

import question_c

while True:
    user_guess = int(input("pick a number between 1 and 5: "))
    random_number = question_c.get_random_number()

    while user_guess < 1 or user_guess > 5:
        user_guess = int(input("Your number is not between 1 and 5.pick another number between 1 and 5: "))

    while user_guess != random_number:
        print("U SUCK, try again. ")
        user_guess = int(input("pick a number between 1 and 5: "))
        while user_guess < 1 or user_guess > 5:
            user_guess = int(input("Your number is not between 1 and 5.pick another number between 1 and 5: "))
    
    if user_guess == random_number: 
        print("congradulations you are correct!!Do you want to try again?: ")
        Try_again = str(input("select Y to try again: ") )
        if Try_again == "Y" or Try_again == "y":
            print ("You selected Try_again")       
        else: 
            print ("GAME OVER!!!!")

            break
   
    
        
