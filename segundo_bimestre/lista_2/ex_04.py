import sys

try:
    x, y = int(sys.argv[1]), int(sys.argv[2])
    print(x + y)
except ValueError:
    print("Escreva números inteiros para somar")
except IndexError:
    print("Escreva 2 números inteiros como argumentos para somar")
