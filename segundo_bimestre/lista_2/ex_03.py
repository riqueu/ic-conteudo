import random
from collections import defaultdict

lista = [random.randint(0, 15000) for i in range(500)]

counter = defaultdict(lambda: 0)
for n in lista:
    counter[n] += 1
print(counter)
