#matriz bidimensional vertical
contadorPar = 0
contadorImpar = 7
for i in range(1, 7):
    for j in range(1, 7):
        if(i%2 == 0):
            print(contadorImpar-j, end='\t')
        else:
            print(contadorPar +j, end='\t')
    contadorPar = 0
    contadorImpar = 7
    print('')