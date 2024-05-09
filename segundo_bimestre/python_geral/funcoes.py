def print_quadrado(n):
    print(n ** 2)


print_quadrado(10)
print_quadrado(22 / 7)
print_quadrado(10_000)
print_quadrado(2.0)

x = 10
y = 20


def fun(a, b):
    x = 32

    def g(k):
        return k + a

    return g(a), x


z, x = fun(x, y)
print(x)
