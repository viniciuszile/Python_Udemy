#recaregando o modulo / import mais de uma vez

import importlib

import aula43_m


for i in range(10):
    importlib.reload(aula43_m)
    print(i)

print('Fim')