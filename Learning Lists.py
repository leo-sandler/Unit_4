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

print("Lesson 4.2 More Lists:")
del numbers1[0]  # This deletes the element at index 0
print(numbers1)
numbers1.insert(0, "new")  # This adds the new value into the index spot 0
print(numbers1)
school = "Greenwood College School"
print(school[0])  # This prints G, so the most functions work with this(insert will work...# )
a = "Hello World"
b = "42"
c = 42
print(a.isdigit())  # This prints False
print(b.isdigit())  # This prints True
# print(c.isdigit()) This will error out due to the fact that 42 is already a number.
# The numbers do not have an isdigit function, as this is only for strings`

# Task 1: Create a list of 5 elements and delete the third one
brands = ["Nike", "Adidas", "Linux", "Reebok", "Puma"]
del brands[2]
print(brands)
# Task 2: Use random to create a list of 6 random numbers. Insert even or off to choose which number is added
nums = []
for num in range(0, 6):
    input_odd_or_even = str(input("Odd or Even: "))
    if input_odd_or_even == "Odd":
        odd = random.randrange(1, 100, 2)
        nums.append(odd)
    elif input_odd_or_even == "Even":
        even = random.randrange(2, 100, 2)
        nums.append(even)
    else:
        break
print(nums)
# Task 3: Write each letter of a string on a new line(use a for a loop)
for g in school:
    print(g)
# Task 4: Print a word backwards(print("Hello World!,end=""))
h = "Hello"
print(h[4], h[3], h[2], h[1], h[0])
# Use the sentence, You're a wizard Harry and change all e's to 3's, o's to 0's and h's to 4's.
wizard = "You're a wizard Harry"
# if wizard == "e":
# del wizard("e")
# wizard+"3"
# elif wizard == "o":
# del wizard("o")
# wizard.append(0)
# elif wizard == "H":
# wizard.append ("H")
# wizard.append(4)
# print(wizard)
# For loop loops through the string, adding onto the end of a new string. Possibly string find and replace

# This is the next lesson, 2D Lists:
a1 = [1, 2, 3]
b1 = [99, 98, 97]
c1 = [7, 8, 9]
new_list = [a1, b1, c1]
print(new_list[1][0])  # This prints from the second list(the 1) and the first item(the 0, second)
string_list = ["Hello", "World"]
print(string_list[1][2])  # This will print the r from world because it takes the second word and third letter
# Nested for Loop
for x in new_list:
    for y in x:  # The x represents each of the 3 lists, and the y represents the individual elements in each list
        print(y)

