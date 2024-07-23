import math
pokemon = int(input())
candy = int(input())


score = 0
if(candy >= 12):
    numCandy = candy/12
    num = candy%12
    candyBonus = numCandy*2
    candy = candy+candyBonus+num
    score = math.ceil(candy/12)


print(score)
