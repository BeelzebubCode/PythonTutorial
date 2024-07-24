# def insertionSort(alist):
#     for index in range(1, len(alist)):

#         currentvalue = alist[index]
#         position = index

#         while position > 0 and alist[position-1] > currentvalue:
#             alist[position] = alist[position-1] # เลื่อนไปทางขวา
#             position = position - 1

#         alist[position] = currentvalue

# alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# insertionSort(alist)
# print(alist)


# def factorial(numeric):
#     if numeric != 0:
#         return numeric * factorial(numeric-1)
#         # print(result)
#     else:
#         return 1

# num = int(input("Input numeric: "))
# result = factorial(num)
# print(f"The factorial of {num}! is {result}")

# เลขฐาน
# def toStr(number, base):
#     number_16 = "0123456789ABCDEF"
#     if number < base:
#         return number_16[number]
#     else:
#         return toStr(number//base, base) + number_16[number%base]
    
# number, number_base = input().split()
# number, number_base = int(number), int(number_base)
# print(toStr(number, number_base))

# Leap year
# year = int(input())

# if year % 4 == 0 and year % 100 != 0:
#     print("Leap year")
# elif year % 100 == 0 and year % 400 == 0:
#     print("Leap year")
# else:
#     print("Not leap year")

# num = [1, 2, 3, 4, 5, 6, 7]
# print(num[:])
# print(num[::-1])

# x = [1, 2, 3, 4, 5, 6]
# y = [8, 7, 6, 5, 4, 3, 2, 1, 0]
# z = x[1:4] + y[4:5]
# print(z)

# numbers = input().split()
# count_numbers = {}
# numbers = map(int, numbers)

# for num in numbers:
#     if num not in count_numbers.keys():
#         count_numbers[num] = 1
#     else:
#         count_numbers[num] += 1
# print(count_numbers)

# import random
# word_list = ["aardvark", "baboon", "camel"]
# chosen_word = random.choice(word_list)
# word_length = len(chosen_word)
# display = ["_"] * word_length

# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}")

# greet_with("Jirat", "Thai")
# greet_with("Jack Bauer", "Nowhere")


# def format_name(f_name, l_name):
#     full_name = (f_name + " " + l_name).title()
#     return f"full name: {full_name}"

# format_fullname = format_name("AnGELA", "YU")
# print(format_fullname)
##############################################################################
# students = [
#     {"name": "Z", "house": "ggg"},
#     {"name": "B", "house": "ggg"},
#     {"name": "A", "house": "ggg"},
# ]

# def get_name(student):
#     return student["name"]

# for student in sorted(students, key=get_name):
#     print(f"{student['name']} is in {student['house']}")

# numbers = input("Enter number :").split()
# numbers = list(map(int, numbers))
# print(numbers)
