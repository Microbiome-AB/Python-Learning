#Create program that ask user to enter n no of todo and display it

todo = []

total_todo= int(input("Enter total number of todo: "))

for i in range(1, total_todo+1):
    todo = input(f"Enter todo {i}: ")
    todos.append(todo)

    print("\n------\n")

#Display all result
for todo in todos:
    print(todo)


#Ask user to enter n number of fruits 
#And display all fruits 

fruits = []

for i in range(n):
        fruit = input(f"Enter the name of fruit {i + 1}: ")
        fruits.append(fruit)
 
for fruit in fruits:
        print(fruit)

