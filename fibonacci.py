sucesion = input("Ingrese (S) para límite máximo de la sucesión \
[por omisión número de términos]? ")

if sucesion == 'S':
    def fib(n):
        a, b = 0,1
        while a < n:
            print(a, end=' ')
            a, b = b, a + b
    m = int(input("Límite máximo~> "))   
    fib(1000000)

else:
    n = int(input("Número de términos~> "))
    a, b = 0,1
    for i in range(n):
        print(a, end=' ')
        a, b = b, a + b