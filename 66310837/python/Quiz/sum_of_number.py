n = list(map(int, input().split()))
is_sum = int(input())

index_sum = []
for i in range(len(n)-4):
    sum_of_five = sum(n[i:i+5])
    if sum_of_five == is_sum:
        index_sum.append(i)

if index_sum:
    for i in index_sum:
        print(i)
else:
    print(-1)
