def executa(funcao, *args):
    return funcao(*args)


# duplica = cria_multiplicador(2)


print(
    executa(
        lambda x, y: x + y,
        2, 3
    ),
)

print(
    executa(
        lambda *args: sum(args),
        1, 2, 3, 4, 5, 6, 7
    )
)

duplica = executa(
    lambda m: lambda n: n * m,
    2
)
print(duplica(2))