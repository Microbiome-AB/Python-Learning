#create a program that find random number between -10 to -20

import random

def find_random_number():
    return random.randint(-20, -10)

if __name__ == "__main__":
    random_number = find_random_number()
    print(f"The random number between -20 and -10 is: {random_number}")
















