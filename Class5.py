#Generate ramdom number in python
import random

random_number=random.randint(1,100)
print(random_number)

for i in range (1,50):
    random_number=random.randint(1,3)
print(random_number)


#Random number guess 
import random

random_num = random.randint(1,20)
user_input= int(input("Enter number between 1 to 20."))

print(f'Actual Random number is {random_num}')

#Random string generate 


perosn_names = ['Ram', 'Sita', 'Menuka']

winner_random=choice(perosn_names)
print(winner)

#create a program that find random number between -10 to -20

import random

def find_random_number():
    return random.randint(-20, -10)

if __name__ == "__main__":
    random_number = find_random_number()
    print(f"The random number between -20 and -10 is: {random_number}")








