
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
if wizard == "e":
    del wizard("e")
    wizard+"3"
elif wizard == "o":
    del wizard("o")
    wizard.append(0)
    elif wizard == "H":
        wizard.append ("H")
        wizard.append(4)
print(wizard)
# For loop loops through the string, adding onto the end of a new string. Possibly string find and replace
