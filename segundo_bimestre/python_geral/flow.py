"""while True:
    try:
        idade = int(input("Digite sua idade: "))
        if idade < 0:
            print("Sua idade deve ser um número inteiro não negativo")
            continue
        break
    except ValueError:
        print("Digite um número inteiro não negativo")
print(f"Essa é sua idade: {idade}")"""

x = 10
while x:
    print(x, end=", ")
    x -= 1
print()

lista_1 = [i + 1 for i in range(10)]
for el in lista_1[::-1]:
    print(el, end=", ")
print()

lista_2 = [i + 1 for i in range(10)] + ["a"]
for el in lista_2:
    if isinstance(el, int):
        continue
    print("Há ao menos um não-inteiro")
    break
else:
    print("Todos elementos são inteiros")  # só é acionado caso o loop chegue em seu final.


def print_match(status: int = 404) -> None:
    match status:
        case 400:
            print("Bad request")
        case 404:  # | 403 | 401:
            print("Not found")
        case 418:
            print("I'm a teapot")
        case _:
            print("Something wrong with the internet")


def print_ifelif(status: int = 404) -> None:
    if status == 400:
        print("Bad request")
    elif status == 404:
        print("Not found")
    elif status == 418:
        print("I'm a teapot")
    else:
        print("Something wrong with the internet")
