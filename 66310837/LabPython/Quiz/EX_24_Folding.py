data = input().split()
# print(data)

step = int(data[1])
new_data = []
for index in range(0, len(data[0]), step):
    new_data.append(data[0][index:index+step])

# print(new_data)
print(' '.join(new_data))
new_data = list(map(int, new_data))
print(sum(new_data))
    