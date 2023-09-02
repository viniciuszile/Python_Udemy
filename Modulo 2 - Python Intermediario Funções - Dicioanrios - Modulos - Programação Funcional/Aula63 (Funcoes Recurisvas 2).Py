# - Um caso base que para a recursão
# - fatorial - n! = 5! = 5 * 4 * 3 * 2 * 1 = 120
# https://brasilescola.uol.com.br/matematica/fatorial.htm

def factorial(n):
    if n <= 1:
        return 1

    return n * factorial(n - 1)


print(factorial(5))