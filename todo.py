#List uses []  

todo_list = ['Learn python', 'Read 1 Book', 'Meditation', 'Go to Gym']
print(todo_list[0])
print(todo_list[1])
print(todo_list[2])


for i in todo_list:
    print(i)

todo_list.pop() #remove the last item

#Tuple use () - oder and unchangeable

fruits = ('Apple', 'Mango', 'Orange', 'Apple')

for i in fruits:
    print(i)


##Set uses {}
##
fruits = {'Apple', 'Mango', 'Orange', 'Apple'}

for i in fruits:
    print(i)

#Dictionary
expenses = {
    'sunday': 1000,
    'monday': 2000, 
    'tuesday': 3000,
}

total= sum(expenses.values())

#Add your electricity bill from Jan to Dec in Dictionary and find total and average 

electricity_bills = {
    "January": 120.50,
    "February": 110.75,
    "March": 100.00,
    "April": 105.25,
    "May": 115.00,
    "June": 125.00,
    "July": 130.75,
    "August": 120.25,
    "September": 110.50,
    "October": 115.75,
    "November": 118.00,
    "December": 122.50
}
# Calculate the total bill for the year
total_bill = sum(electricity_bills.values())

# Calculate the average monthly bill
average_bill = total_bill / len(electricity_bills)

# Print the results
print(f"Total electricity bill for the year: ${total_bill:.2f}")
print(f"Average monthly electricity bill: ${average_bill:.2f}")


country_capital = {
    'nepal': 'Kathmanu',
    'us': 'WDC'
}

##List and Dictionary are mostly used 


#Loop: process of repeat something 
names= ['Ram', 'hari', 'Shyam', 'Menuka']

for i in names:
    print(i)

print(names[1])
print(names[2])

for i in range (10000):
    print(i+1)



for k in country_capital:
    print(k)


## Aadd your electricity bill from Jan to Dec in Dictionary and find total and average"
electricity_bills = {
    "January": 120.50,
    "February": 110.75,
    "March": 100.00,
    "April": 105.25,
    "May": 115.00,
    "June": 125.00,
    "July": 130.75,
    "August": 120.25,
    "September": 110.50,
    "October": 115.75,
    "November": 118.00,
    "December": 122.50
}

# Calculate the total bill for the year
total_bill = sum(electricity_bills.values())

# Calculate the average monthly bill
average_bill = total_bill / len(electricity_bills)

# Print the results
print(f"Total electricity bill for the year: ${total_bill:.2f}")
print(f"Average monthly electricity bill: ${average_bill:.2f}")







































