###Create a program that ask user to enter no. of month and display 1 for Jan and 12 for Dec 

months = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

###Ask user to enter a number
month_number = int(input("Enter the number of the month (1-12): "))

###Check if the entered number is correct/valid
if 1 <= month_number <= 12:
    ##Show the corresponding month's name
    print(f"The month is {months[month_number]}")
else:
    print("Invalid number! Please enter a number between 1 and 12.")