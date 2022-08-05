from operator import le
from this import s

len = 6
suma = 0
for i in range(1, 7):
    for j in range(1, 7):
        if j == 1:
            suma = i
        else:
            suma = suma + len
        print((suma), end='\t')
        
    suma = 0
    print('')