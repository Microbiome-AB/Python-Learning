#Ask user to enter price, if price is >=500, it is expensive else price is okay.
## Ask user to enter number and find that number is odd or even 


# Ask the user to enter a price
price = float(input("Enter the price: "))

# Determine if the price is expensive or okay
if price >= 500:
    print("The price is expensive.")
else:
    print("The price is okay.")

#Ask user to enter number and find that number is odd or even

# Ask the user to enter a number
number = int(input("Enter a number: "))

# Determine if the number is odd or even
if number % 2 == 0:
    print(f"The number {number} is even.")
else:
    print(f"The number {number} is odd.")

#When we assign value we use =
# When we comapre value we use ==
i = 20
print(i==20)


#Odd or even 

number = int(input("Enter number: "))
if number%2==0:
    print(f"{number}is even number")
else:
    print(f"{number}is odd number")



