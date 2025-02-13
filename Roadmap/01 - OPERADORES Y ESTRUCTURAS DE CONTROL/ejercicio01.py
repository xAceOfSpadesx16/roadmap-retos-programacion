# Operadores aritmeticos
print("Operadores aritmeticos")
print(1 + 1) # Suma
print(2 - 1) # Resta
print(2 * 2) # Multiplicacion
print(2 / 2) # Division
print(2 % 2) # Modulo
print(2 ** 2) # Exponente
print(2 // 2) # Cociente

# Operadores de comparación
print("Operadores de comparación")
print(1 == 1) # Igual
print(1 != 1) # Distinto
print(1 > 1) # Mayor
print(1 < 1) # Menor
print(1 >= 1) # Mayor o igual
print(1 <= 1) # Menor o igual

#Operadores bit a bit
print("Operadores bit a bit")
print(1 & 1) # Bitwise AND
print(1 | 1) # Bitwise OR
print(1 ^ 1) # Bitwise XOR
print(1 << 1) # Bitwise Left Shift
print(1 >> 1) # Bitwise Right Shift

# Operadores lógicos
print("Operadores lógicos")
print(1 and 1) # Y
print(1 or 1) # O
print(not 1) # Negación

# Operadores de asignación
print("Operadores de asignación")

a = 1
b = 2

x=a # Asignacion
x=a; x+=b; print(x) # Suma
x=a; x-=b; print(x) # Resta
x=a; x*=b; print(x) # Multiplicacion
x=a; x/=b; print(x) # Division
x=a; x%=b; print(x) # Modulo
x=a; x**=b; print(x) # Exponente
x=a; x//=b; print(x) # Cociente
x=a; x&=b; print(x) # Bitwise AND
x=a; x|=b; print(x) # Bitwise OR
x=a; x^=b; print(x) # Bitwise XOR
x=a; x<<=b; print(x) # Bitwise Left Shift
x=a; x>>=b; print(x) # Bitwise Right Shift

# Operadores de identidad
print("Operadores de identidad")
print(1 is 1) # Identidad
print(1 is not 2) # No identidad

# Operadores de pertenencia
print("Operadores de pertenencia")
print(1 in [1,2,3,4]) # Pertenece
print(1 not in [2,3,4,5]) # No pertenece

# ESTRUCTURAS DE CONTROL

# Condicionales

print("Estructuras de control condicionales")

print('IF statement')
lenguaje = "Python"
if lenguaje == "Java":
    print("Mi lenguaje es Java")
elif lenguaje == "Python":
    print("Mi lenguaje es Python")
else:
    print("Mi lenguaje es otro")


print('MATCH statement')
match lenguaje:
    case "Java":
        print("Mi lenguaje es Java")
    case "Python":
        print("Mi lenguaje es Python")
    case _:
        print("Mi lenguaje es otro")

# Bucles

# Bucle for
print("Bucle for")
for i in range(10):
    print(i, end=" ")

# Bucle while
print("\nBucle while")
i = 0
while i < 10:
    i += 1
    print(i, end=" ")

print('\n')

# Bucle while con break
print("Bucle while con break")
i = 0
while True:
    i += 1
    print(i, end=" ")
    if i == 10:
        break

print('\n')

# Manejo de errores
# Estructura try-except

print("Manejo de errores")

print('Try statement')
try:
    print(1/0)
except ZeroDivisionError:
    print("No se puede dividir por cero")

# Estructura try-except-else
print('Try statement con else')
try:
    print(1/1)
except ZeroDivisionError:
    print("No se puede dividir por cero")
else:
    print("No se ha producido ninguna excepcion")

# Estructura try-except-finally
print('Try statement con finally')
try:
    print(1/0)
except ZeroDivisionError:
    print("No se puede dividir por cero")
finally:
    print("Se ha ejecutado el bloque finally")

# EXTRA

for i in range(10, 55, 2):
    if i % 3 == 0 or i == 16:
        continue
    print(i, end=" ")