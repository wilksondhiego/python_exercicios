import numpy as np
matriz = np.array([[1,2,3],
                   [2,5,6],
                   [3,6,9]])
if np.array_equal(matriz, matriz.T):
    print("Simétrica")
else:
    print("Não é simétrica")