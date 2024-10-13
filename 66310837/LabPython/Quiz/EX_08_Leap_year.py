def leap_year(year):
    if year % 4 == 0 and year % 100 != 0:
        print("The year is a leap year!")
    elif year % 100 == 0 and year % 400 == 0:
        print("The year is a leap year!")
    else:
        print("The year isn't a leap year!")

year = int(input())
leap_year(year)

# number = int(input())
# if number == 2019:
#     print("The year isn't a leap year!")
# elif number == 2020:
#     print("The year is a leap year!")
# elif number == 2021:
#     print("The year isn't a leap year!")
# elif number == 2022:
#     print("The year isn't a leap year!")
# elif number == 2023:
#     print("The year isn't a leap year!")
# elif number == 2018:
#     print("The year isn't a leap year!")
# elif number == 2017:
#     print("The year isn't a leap year!")
# elif number == 2016:
#     print("The year is a leap year!")
# elif number == 2024:
#     print("The year is a leap year!")
# elif number == 2025:
#     print("The year isn't a leap year!")
# elif number == 2015:
#     print("The year isn't a leap year!")
# elif number == 2014:
#     print("The year isn't a leap year!")