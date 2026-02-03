"""
student's full name
feb 3, 2026
Lab 3, conditional statement and loop is python
"""
print("\n------ Example 1: set-up of conditional statement ----")
# conditional statement states the flow the program
age = 21
if( age >=21):
    print("You are an adult!")
elif (age<21 and age>=12):
    print("You are a teen!")
elif(age<12 and age>0):
     print("You are a kid")
else:
    print("Unable to read age")

    print("\n------- example 2: for loop in a list-----")
# for loop as a counter to print from 9 to 1, step 1
for n in range(9, 0, -1):
    print(n)

    # for loop in a list
    numbers =[3,6,1,-8,9,-5]
    count_negative = 0
    for m  in numbers:
        if m< 0:
            count_negative += 1
        else:
            print(f"There is/are {count_negative} negative numbers")
            # for else, the else statement will run only after the complete of all iterations in the loop

    print("\n------- example 3: while loop as a counter -----")
# while loop  to print from -3 to 5, inclusive, step of 2, output -3, -1, 1, 3, 5
x = -3
while x <=5:
    print(x)
    x += 2  

    print("\n------- example 4: while loop to validate an input----")
    #The program collects a nummber from the user and print if the number is even or odd 
    # after it, the prgram will ask the user if another number will be tested
    # if the user types 'y' or 'Y', the program will repeat, otherwise it will end

    decision_user = 'y'
    user_number = 0
    while True:
        user_number = int(input(" Enter a number: "))
        if user_number% 2 == 0:
            print(f"{user_number} is EVEN")    
        elif user_number ==0:
            print("The number is ZERO")
        else:
            print(f"{user_number} is ODD")

            decision_user = input("Do you want to test another number? (y/n): ")    
            if decision_user !='y' and decision_user != 'Y':      
                break    

            print("\n----- EXCERCISE 1: Valiate a number between 1 and 9 -------")
            number = int(input("Enter a number:"))
            if 1<= number <=9:
                print("Valid number")
            else:
                print("Invalid number")
            
                         

            print("\n----- EXCERCISE 2: I am  guessing a number between 1 and 10. You have three attempts to guess it.")
            import random 
            secret_number = random.randint(1,10)
            attempts = 3   
            for attempt in range(attempts):
                user_guess = int(input("Enter your guess (between 1 and 10): "))
                if user_guess == secret_number:
                    print("Congratulations! You guessed the correct number.")
                    break
                else:
                    print("Wrong guess. Try again.")
            else:
                print(f"Sorry, you've used all attempts. The correct number was {secret_number}.")
           
             
  