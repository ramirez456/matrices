for i in range(1, 7):
    for j in range(1, 7):
        if i > j or i == j:
            if(j%2 == 0):
                print('B', end='\t')
            else:
                print('A', end='\t')
        else:
            print('0', end='\t')
    print('')