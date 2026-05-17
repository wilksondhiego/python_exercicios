import numpy as np
matriz = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9]])
transposta = matriz.T
rotacionada = np.array([linha[::-1] for linha in transposta])
print(rotacionada)