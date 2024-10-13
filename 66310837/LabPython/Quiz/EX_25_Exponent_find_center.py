number, number_pow, number_center = map(int, input().split())
# print(number, number_pow, number_center)

data = str(number**number_pow)
print(data)
data_center = [data[i] for i in range(1, len(data)-1)]
# print(data_center)
if len(data_center) < number_center:
    data_center.insert(0, str(number_center))

print(''.join(data_center))

