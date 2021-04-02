arr1 = []
arr2 = []
arr3 = []
input1 = int(input('how much prices do you want to include: '))
for i in range(input1):
    a = float(input('write prices: '))
    arr1.append(a)

for i in range(2):
    b = float(input('type you percentage: '))
    arr2.append(b)

for i in range(len(arr1)):
    if i == 0:
        total = arr1[i] + arr1[i] * (arr2[i]/100)
        total2 = total - arr1[i]
    else:
        total = arr1[i] - arr1[i] * (arr2[i] / 100)
        total2 = arr1[i] - total
    arr3.append(total2)

ask = int(input('tell us price: '))
final_total = abs(arr3[0] - arr3[1])
if ask == final_total:
    print(True)
else:
    print(False)
