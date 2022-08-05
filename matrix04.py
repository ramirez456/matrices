#matriz bidimensional vertical
len = 7
for i in range(1, 7):
    for j in range(1, 7):
        if j == len -1:
            print(1, end=' ')
            len = len -1
        else:
            print('0', end=' ')
    print('')