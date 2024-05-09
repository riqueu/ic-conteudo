# Strings:

string_1 = "ola!"
string_2 = 'tchau'
string_3 = """
texto
legal
"""

string_4 = string_1 + string_1[::-1]
print(string_4)

print()
# Listas:

lista_1 = [1, 2, 3]
lista_2 = ["ola", string_2, 10, [20, [30, 40], 50], 60, (70, 80, 90)]

for elemento in lista_2:
    print(elemento)

print()
# Tuplas:

for n, e in enumerate("casa"):
    print(f"Letra {n + 1}: {e}")

print(list(enumerate("massa")))

tupla_1 = 1, 2, 3
tupla_2 = (10, 20, 30, [1, 2, 3])

for el in tupla_2:
    print(el)

print(f"Tupla antes: {tupla_2}")
tupla_2[3][2] = "três"
print(f"Tupla dps: {tupla_2}")

print()
# Sets/Conjuntos:

print(set("casa"))
set_1 = {1, 1, 2, 1, 0, 12}
set_2 = {1, 1, 2, 1, 0, 15}
set_3 = set_1 | set_2  # União
set_4 = set_1 & set_2  # Intersec
set_5 = set_1 - set_2  # Dif
set_6 = set_2.difference(set_1)  # Dif
print(set_3)
print(set_4)
print(set_5)
print(set_6)

print()
# Dicionários:

dicio_1 = {"a": 1,
           "b": 2,
           "c": 3}

for k in dicio_1:
    print(dicio_1[k])

print(list(dicio_1.items()))

print(dicio_1.keys())
print(dicio_1.values())

lista_chaves = ["d", "e", "f"]
lista_valores = [4, 5, 6]
dicio_2 = dict(zip(lista_chaves, lista_valores))
dicio_3 = dicio_1 | dicio_2
print(dicio_3)

print()
# Comprehension:

lista_nova = [i.upper() if i == "a" else i for i in "casa"]
print(lista_nova)

set_novo = {i.upper() if i == "a" else i for i in "casa"}
print(set_novo)

dicio_novo = {x: y for x, y in zip([1, 2, 3], [4, 5, 6])}
print(dicio_novo)
