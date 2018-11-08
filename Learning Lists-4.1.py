import random
colours = ['red', 'blue', 'green']
print(colours[0])  # This prints red
print(colours[2])  # This prints green
print(len(colours))  # This prints the total amount of things in the list
colours1 = ['orange', 'yellow', 'purple']
b = colours+colours1
b.sort()  # Sort before using in a loop
for x in b:
    print(x)
    # This prints the list on multiple lines
colours[2] = 'magenta'  # This switches green to magenta
print(colours[2])  # This prints magenta
colours.append('new colour')
print(colours)

names = []  # This is an empty list
print(names)  # This prints out empty brackets
names.append("Liam")
names.append("Andrew")
print(names)  # This prints out the added name
print(names[0])  # This prints the list without brackers

for name in names:
    print(name)
    print(name[0])  # This prints the first letter of each

# Task 1: Create a list of 5 items then print the whole list at once
computers = ["Macbook Air", "Macbook Pro", "Microsoft Surface", "Lenovo ThinkPad", "Fujitsu"]
print(computers)
# Task 2: Create a list of 4 items them change the value of each item
colour_modes = ["Cyan", "Magenta", "Yellow", "Key"]
colour_modes[0] = "Red"
colour_modes[1] = "Green"
colour_modes[2] = "Blue"
colour_modes[3] = "White"
print(colour_modes)

# Task 3: Create a list of 10 numbers not in order and sort it(sort() function)
numbers = ["2", "1", "4", "3", "8", "5", "7", "6", "99", "9"]
numbers.sort()
print(numbers)
# Task 4: Find the highest value in two separate lists of numbers by using one (max() function)
numbers1 = ["2", "1", "4", "3"]
numbers2 = ["8", "5", "7", "6", "99", "9"]
print(max(numbers1 and numbers2))
# Task 5: Print out every value in a list
for number in numbers1:
    print(number)
# Task 6: Print out every second value in a list
print(numbers1[::2])
for number in range(0, len(numbers1), 2):
    print(numbers1[number])
