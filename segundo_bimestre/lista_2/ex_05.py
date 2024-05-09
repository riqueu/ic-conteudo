from typing import Union

def soma_n(*args) -> Union[int, float]:
    print(locals())
    return sum(args)


# Exemplo:
print(soma_n(10, 15, 15, 25, 10, -5, -60))
