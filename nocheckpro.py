# If num is greater than 0, check if num is even by checking if the remainder when num is divided by 2 is 0.
# If the remainder is 0, execute the code block that prints the message “The number is positive and even.”
# If the remainder is not 0, execute the code block that prints the message “The number is positive but odd.”
# If num is not greater than 0, execute the code block that prints the 



number=int(input("Enter Number : "))

if number>0:
    if number % 2==0:
        print("The number is positive and even")
    else:
        print("The number is positive but odd.")
else:
     print("Enter Positive Number")