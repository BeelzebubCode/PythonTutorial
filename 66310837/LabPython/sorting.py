# Bubble sort
# เปรียบเทียบเป็นคู่ๆ **ช้า

# def bubbleSort(alist):
#     for passnum in range(len(alist)-1, 0, -1):
#         for i in range(passnum):
#             if alist[i] > alist[i+1]:
#                 temp = alist[i]
#                 alist[i] = alist[i+1]
#                 alist[i+1] = temp

# alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# bubbleSort(alist)
# print(alist)

count = 0
list_number = [ 29, 23, 75, 39, 64, 67, 87, 94, 14, 48, 10, 87, 0, 20, 74, 17]
for number in range(len(list_number)-1, 0, -1):
    for i in range(number):
        count += 1
        if list_number[i] > list_number[i+1]:
            temp = list_number[i]
            list_number[i] = list_number[i+1]
            list_number[i+1] = temp

print(list_number)
print(count)
################################################################


################################################################
# Short bubble sort
# def shortBubleSort(alist):
#     exchanges = True
#     passnum = len(alist)-1
#     while passnum > 0 and exchanges:
#         exchanges = False
#         for i in range(passnum):
#             if alist[i]>alist[i+1]:
#                 exchanges = True
#                 temp = alist[i]
#                 alist[i] = alist[i+1]
#                 alist[i+1] = temp
#         passnum-=1

# alist = [20, 30, 40, 90, 99, 60, 70, 80, 100, 110]
# shortBubleSort(alist)
# print(alist)
################################################################


################################################################
# Selection sort
# หาตัวที่มากสุดไปวางที่ตำแหน่งสุดท้าย
# ใช้ n - 1 รอบในการเรียงลำดับ n ตัว
def selectionSort(alist):
    for fillslot in range(len(alist)-1, 0, -1):
        positionMax = 0
        for location in range(1, fillslot+1):
            if alist[location]>alist[positionMax]:
                positionMax = location
        
        temp = alist[fillslot]
        alist[fillslot] = alist[positionMax]
        alist[positionMax] = temp

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
selectionSort(alist)
print(alist)
################################################################


################################################################
# Insertion sort
# ให้ตัวที่เรียงลำดับแล้วอยู่ด้านหน้า เริ่มที่ 1 ตัว
# ตัวถัดไปจะถูกใส่ในส่วนด้านหน้าให้ถูกตำแหน่ง

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
################################################################


################################################################
# Merge sort
# แบ่งเป็นปัญหาย่อยลงไปเรื่อยๆ
# รวมกลับขึ้นมาเป็นการแก้ปัญหาใหญ่ -เปรียบเทียบแล้วเลื่อนหมุด