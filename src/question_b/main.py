#add import

import question_b
pickles = "yes" 

while pickles == "yes" or pickles == "y" or pickles == "Y" :

    num = input("ENTER A NUMBER ")
    num = int (num)
    y = question_b.is_prime(num)

    print (y)

    pickles = str(input("if you want to try again , Enter yes .If not enter no: "))

    if pickles != "yes" and pickles != "y" and pickles != "Y":

        print ("exiting program") 










# Write a program that runs until the user decided to quit, prompt the user for a number, 
   # and display the result.
