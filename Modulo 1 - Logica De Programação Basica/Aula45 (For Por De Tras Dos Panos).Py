"""
    Iterável -> str, range, etc (__iter__)
    Iterador -> quem sabe entregar um valor por vez
    next -> me entregue o próximo valor
    iter -> me entregue seu iterador 10/07/2023
"""

texto = 'zile'  # iterável

iteratador = iter(texto)  # iterator

while True:
    try:
        letra = next(iteratador)
        print(letra)
    except StopIteration:
        break

for letra in texto:
    print(letra)