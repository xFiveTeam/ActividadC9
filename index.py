# Ingrese un numero N y muestre la tabla de multiplicar del numero. Muestre el multiplicando, multiplicador y producto.
# Tincke solution

n = int(input("Ingrese un numero: "))
for n in range(1,11):
    for i in range(1, 11):
        print(n, "x", i, "=", n*i)
        i += 1
        
# Dos aclaraciones, la primera, la variable va minuscula, la segunda, sos un crack ahr


# Liss Solution
# num = int(input("Ingrese un numero: "))

# for i in range(1, 11):
#     print (num, "*", i, "=", num*i)
#     i += 1