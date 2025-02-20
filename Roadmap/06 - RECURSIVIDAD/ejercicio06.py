"""
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
"""

def imprimir_numeros(n: int = 100) -> None:
    if n < 0:
        return
    print(n)
    imprimir_numeros(n - 1)

# imprimir_numeros()

"""
EXTRA
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la 
 *   sucesión de Fibonacci (la función recibe la posición).
"""

def factorial(n: int) -> int:
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
def fibonacci(n: int) -> int:
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
if __name__ == "__main__":
    print(factorial(5)) # 120
    print(fibonacci(7)) # 13