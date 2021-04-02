a = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

# Here Grid has already has numbers. You can manipulate them and make some change in code.

grid = [['.', '.', '.', '.', '2', '.', '.', '9', '.'],
        ['.', '.', '.', '.', '6', '.', '.', '.', '.'],
        ['7', '.', '.', '.', '1', '5', '.', '.', '.'],
        ['.', '7', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '8', '3', '.', '.', '.'],
        ['.', '.', '8', '.', '.', '7', '.', '6', '.'],
        ['.', '.', '.', '.', '.', '2', '.', '.', '.'],
        ['.', '1', '.', '2', '.', '.', '.', '.', '.'],
        ['.', '2', '.', '.', '3', '.', '.', '.', '.']]
arr1 = []
for i in range(9):
    for j in range(9):
        if grid[i].count(a[j]) > 1 or grid[j][i].count(a[j]) > 1:
            k = 'False'
            arr1.append(k)
        else:
            k = 'True'
            arr1.append(k)

if 'False' in arr1:
    print(False)
else:
    print(True)
