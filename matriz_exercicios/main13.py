import numpy as np
matriz = np.arange(1,26).reshape(5,5)
diagonal_sec = np.fliplr(matriz).diagonal()
print(diagonal_sec)