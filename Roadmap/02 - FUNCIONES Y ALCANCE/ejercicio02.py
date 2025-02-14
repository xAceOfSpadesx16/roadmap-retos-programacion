# Funciones

# Funcion sin return ni parametros

def funcion():
    print("esta es una funcion sin parametros ni return")

funcion()

# Funcion con parametros y return
def funcion2(param1, param2):
    return param1 + param2

print(f"Funcion con parametros y return: {funcion2(1, 2)}")

# Funcion con parametros por defecto
def funcion3(param1, param2=2):
    return param1 + param2

print(f"Funcion con parametros por defecto: {funcion3(1)}")

# Funcion con *args
def funcion4(*args):
    return args

print(f'Funcion con *args: {funcion4(1, 2, 3, 4, 5)}')

# Funcion con **kwargs
def funcion5(**kwargs):
    return kwargs

print(f'Funcion con **kwargs: {funcion5(a=1, b=2, c=3)}')

# Funcion con *args y **kwargs
def funcion6(*args, **kwargs):
    return args, kwargs

print(f'Funcion con *args y **kwargs: {funcion6(1, 2, 3, a=1, b=2, c=3)}')

# Funcion recursiva
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(f"Funcion recursiva (factorial de 5): {factorial(5)}")

# Funcion lambda
suma = lambda x, y: x + y
print(f"Funcion lambda (suma de 2 y 3): {suma(2, 3)}")

# Funcion decoradora
def decoradora(funcion):
    def envoltura():
        print("Antes de la ejecucion de la funcion")
        funcion()
        print("Despues de la ejecucion de la funcion")
    return envoltura

@decoradora
def funcion_decorada():
    print("Funcion decorada")

funcion_decorada()

# Funcion anidada
def funcion_anidada():
    def funcion_interna():
        print("Funcion interna")
    return funcion_interna()

funcion_anidada()

# Funcion global
def funcion_global():
    global variable_global
    variable_global = "variable global"

funcion_global()
print(f"Variable global definida en funcion: {variable_global}")

# Funcion local
def funcion_local():
    variable_local = "variable local"
    print(f"Variable local definida en funcion: {variable_local}")

funcion_local()

# Funcion con variable global
variable_global = "variable global"
def funcion_no_local():
    print(f"Variable global definida fuera de la funcion: {variable_global}")

funcion_no_local()


# EXTRA

def extra_func(arg1: str, arg2:str) -> int:
    acumulador = 0
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(f'{i} {arg1} {arg2}')
        elif i % 3 == 0:
            print(f'{i} {arg1}')
        elif i % 5 == 0:
            print(f'{i} {arg2}')
        else:
            acumulador += 1
            print(i)
    print(f'Se han mostrado {acumulador} números')
    return acumulador

extra_func('Python', 'Java')