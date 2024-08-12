number = sorted(list(map(int, input().split())), reverse=True)
# number = input().split()
# number = list(map(int, number))
# number = sorted(number, reverse=True)

if len(number) < 5:
    print("Too few input")
else:
    for i in range(3):
        print(number[i], end=" ")