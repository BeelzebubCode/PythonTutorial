data = input().split()


step = int(data[1])
new_data = []
index = 0
for i in range(len(data[0])//step + 1):
    new_data.append(data[0][index:index+step])
    index += step

print(' '.join(new_data))
new_data = list(map(int, new_data))
print(sum(new_data))
    