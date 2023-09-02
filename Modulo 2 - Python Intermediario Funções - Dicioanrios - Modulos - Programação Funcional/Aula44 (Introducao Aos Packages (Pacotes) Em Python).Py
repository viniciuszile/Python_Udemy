from sys import path

import Aula44_package.modulo
from Aula44_package import modulo
from Aula44_package.modulo import *
from Aula44_package.modulo import soma_do_modulo


print(soma_do_modulo(1, 2))
print(Aula44_package.modulo.soma_do_modulo(1, 2))
print(modulo.soma_do_modulo(1, 2))
print(variavel)
print(nova_variavel)