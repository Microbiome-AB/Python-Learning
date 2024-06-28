#Write down your expenses for each day of the week (Sunday to Saturday).
#Find the total of all your expenses for the week.
#Calculate the average daily expenses.

expense_sun=50
expense_mon=70
expense_tues=35
expense_wed=97
expense_thur=75
expense_fri=20
expense_sat=105

expenses= [50, 70, 35, 97, 75, 20, 105]

total_expense=expense_sun+expense_mon+expense_tues+expense_thur+expense_wed+expense_fri+expense_sat
avg_expense=total_expense/7

print(f"Total expenses for the week: ${total_expense}")
print(f"Average daily expenses: ${avg_expense}")


