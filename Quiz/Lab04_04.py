
def days_in_month(month, year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        return 29 if (year % 400 == 0 or (year % 100 != 0 and year % 4 == 0)) else 28
    else:
        return 0

def count_down_to_songkran(d, m, y):
    songkran_day = 13
    songkran_month = 4
    days_remaining = 0

    while m != songkran_month or d != songkran_day:
        days_remaining += 1

        d+=1
        if d > days_in_month(m, y):
            d = 1
            m += 1
            if m > 12:
                m = 1
                y += 1
    
    return days_remaining
    
day, month, year = map(int, input().split(' '))
print(count_down_to_songkran(day,month,year))