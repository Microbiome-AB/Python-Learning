import random


alphabet = 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z'
print(alphabet.upper)
alphabet_upper = alphabet.upper ()
numbers= '1,2,3,4,5,6,7,8,9,0'

all_combine= alphabet+alphabet_upper+numbers 
all_combine_to_list = all.combine.split(",")

random1=random.choice(all_combine_to_list)
random2=random.choice(all_combine_to_list)
random3=random.choice(all_combine_to_list)
random4=random.choice(all_combine_to_list)

pasword=random1+random2+random3+random4

print(all_combine_to_list)


#Type convert

number1 = input("Enter Number 1: ")
number2= input("Enter Number 2:  ")
sum=number1+number2
print(f"Total is {sum}")


####Create a program, that converts NRS to USD, Euro, Japanease




