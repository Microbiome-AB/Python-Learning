### Aadd your electricity bill from Jan to Dec in Dictionary and find total and average"

electricity_bills = {
    "January": 160.50,
    "February": 110.75,
    "March": 100,
    "April": 105.25,
    "May": 115.00,
    "June": 125.00,
    "July": 500.75,
    "August": 160.25,
    "September": 110.50,
    "October": 145.75,
    "November": 118.00,
    "December": 165.50
}

# Total bill for a whole year
total_bill = sum(electricity_bills.values())

# Average monthly bill
average_bill = total_bill / len(electricity_bills)

# Print the results
print(f"Total electricity bill for the year: ${total_bill:.2f}")
print(f"Average monthly electricity bill: ${average_bill:.2f}")