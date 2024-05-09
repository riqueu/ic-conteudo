import random

lista = [random.randint(0, 15000) for i in range(500)]

print(f"Valores únicos: {len(set(lista))}")
