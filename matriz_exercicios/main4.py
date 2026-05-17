import numpy as np
matriz = np.array([[1, 2],
                   [3, 4]])
matriz[[0,1]] = matriz[[1,0]]
print(matriz)