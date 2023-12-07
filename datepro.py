day = int(input("Enter the day: "))
month = int(input("Enter the month: "))
year = int(input("Enter the year: "))

if 1 <= day <= 31 and 1 <= month <= 12 and year > 0:
    print("The entered Date is correct.")
else:
    print("The entered Date is not correct.")
