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

# ################################################################################
# import turtle

# # สร้างหน้าต่างและเต่า
# wn = turtle.Screen()
# wn.title("Cat Drawing")
# wn.bgcolor("white")

# t = turtle.Turtle()
# t.shape("turtle")
# t.speed(5)

# # วาดหัวแมว
# t.penup()
# t.goto(0, -50)
# t.pendown()
# t.circle(100)

# # วาดตาซ้าย
# t.penup()
# t.goto(-35, 35)
# t.pendown()
# t.circle(10)

# # วาดตาขวา
# t.penup()
# t.goto(35, 35)
# t.pendown()
# t.circle(10)

# # วาดจมูก
# t.penup()
# t.goto(0, 15)
# t.pendown()
# t.circle(5)

# # วาดปาก
# t.penup()
# t.goto(-25, 0)
# t.pendown()
# t.right(90)
# t.circle(25, 180)
# t.penup()
# t.goto(25, 0)
# t.pendown()
# t.circle(-25, 180)

# # วาดหูซ้าย
# t.penup()
# t.goto(-70, 75)
# t.pendown()
# t.goto(-100, 150)
# t.goto(-40, 120)
# t.goto(-70, 75)

# # วาดหูขวา
# t.penup()
# t.goto(70, 75)
# t.pendown()
# t.goto(100, 150)
# t.goto(40, 120)
# t.goto(70, 75)

# # วาดหนวดซ้าย
# t.penup()
# t.goto(-20, 10)
# t.pendown()
# t.goto(-80, 20)
# t.penup()
# t.goto(-20, 0)
# t.pendown()
# t.goto(-80, 0)
# t.penup()
# t.goto(-20, -10)
# t.pendown()
# t.goto(-80, -20)

# # วาดหนวดขวา
# t.penup()
# t.goto(20, 10)
# t.pendown()
# t.goto(80, 20)
# t.penup()
# t.goto(20, 0)
# t.pendown()
# t.goto(80, 0)
# t.penup()
# t.goto(20, -10)
# t.pendown()
# t.goto(80, -20)

# # ปิดหน้าต่างเมื่อคลิก
# wn.mainloop()
##########################################################################


#stack = []
#while True:
 #   word = input()
 #   if word == "quit": break

    #stack.append(word)

#for _ in range(len(stack)):
# 	print(stack.pop())


# def doubled(n):
#     if n == 1:
#         return 1
#     else:
#         return 2 * doubled(n-1)

# num = int(input())
# result = doubled(num)
# print(result)

# def recursive_sum(num, memory):
#     if num in memory:
#         return memory[num]
#     else :
#         memory[num] = recursive_sum(num-1, memory) + recursive_sum(num-2, memory)
#         return memory[num]

# a = int(input())
# memory = {0:1, 1:1}
# print(recursive_sum(a, memory))
####################################

# def check_password(pw_list):
#     passwords = []
#     for pw in pw_list:
#         pw = pw.replace(" ", "")
#         if check_str_lenght(pw) and check_str_low(pw) and check_str_up(pw) and check_str_character(pw):
#             passwords.append(pw)
#     return passwords

# def check_str_low(pw):
#     for char in pw:
#         if char.islower():
#             return True
#     return False

# def check_str_up(pw):
#     for char in pw:
#         if char.isupper():
#             return True
#     return False

# def check_str_character(pw):
#     character = set('#$@')
#     return bool(character & set(pw))
    
# def check_str_number(pw):
#     number = set('1234567890')
#     return bool(number & set(pw))

        
# def check_str_lenght(pw):
#     if len(pw) >= 6 and len(pw) <= 12:
#         return True
#     else:
#         return False

# password_list = input().split(',')
# passwords = check_password(password_list)
# print(','.join(passwords))

# name = ["name1", "name2", "name3"]
# for i in name:
#     print(i)


# def recursive_sum(num, memory):
#     if num in memory:
#         return memory[num]
#     else :
#         memory[num] = recursive_sum(num-1, memory) + recursive_sum(num-2, memory)
#         return memory[num]

# a = int(input())
# memory = {0:1, 1:1}
# print(recursive_sum(a, memory))

"""
rs(5, {0:1, 1:0})
rs(4) + re(3)
rs(3) + re(2) | rs(3) => rs(2) + rs(1) | 2 + 1 | 3 + 2 = 5
rs(1) + re(0) | rs(2) = 2
rs(1) = 1
rs(0) = 1

"""


input_str = input().split(';')

num = [group.split(',') for group in input_str]
num = list(map(lambda n : list(map(int, n)), num))
result = []

num.sort()
for i in range(len(num)):
    for j in range(min(num[i]), max(num[i])):
        result.append([j, j+1])

print(result)
