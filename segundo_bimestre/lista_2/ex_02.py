import random
from collections import Counter

lista = [random.randint(0, 15000) for i in range(500)]

print(f"Frequência: {Counter(lista)}")
