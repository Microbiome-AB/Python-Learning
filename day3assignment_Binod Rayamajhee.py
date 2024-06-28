
# Add your 5 friend names to list, and their adress on another list and print all their name and address

friends_names = ["Alaka", "Jas", "Laxman", "David", "Aziz"]
friends_addresses = ["Banepa", "Pokhara", "Chitwan", "Butwal", "Lalitpur"]

## Check if both lists have the same length
if len(friends_names) != len(friends_addresses):
    print("The lists of names and addresses do not match in length!")
else:
    # Print each friend's name and address
    for i in range(len(friends_names)):
        print(f"{friends_names[i]} lives in {friends_addresses[i]}")