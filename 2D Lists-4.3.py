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

#  Task 1: Create 2 lists and then add them to a list:
letters1 = ["a", "b", "c"]
letters2 = ["d", "e", "f"]
letters = [letters1, letters2]
#  Task 2: Prints all elements in both lists:


def letters_printer():
    for f in letters:
        for g in f:
            print(g)


letters_printer()

#  Task 3: The sum of one column:

def column_add():
    sum1 = 0
    for y in new_list:
        sum1 += y[0]
    return sum1
print(column_add())

def row_add():
    sum1 = 0
    for x in a1:
        for n in x:
            sum1 += [0]x
    return sum1
print(row_add()