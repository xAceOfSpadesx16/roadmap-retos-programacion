"""
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
"""

# Por valor
print("Por valor")
a = 1
b = a

print(f"a: {a}")
print(f"b: {b}")

a = 2
print(f"a: {a}")
print(f"b: {b}")

# Por referencia
print("Por referencia")

c = [1, 2, 3]
d = c

print(f"c: {c}")
print(f"d: {d}")

c.append(4)
print(f"c: {c}")
print(f"d: {d}")

print("Con copia para evitar referencia")
e = [1, 2, 3]
f = e.copy()
e.append(4)
print(f"e: {e}")
print(f"f: {f}")


# EXTRA

"""
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
"""


# Por valor
def intercambia_por_valor(a: int, b: int) -> tuple[int, int]:
    temp = a
    a = b
    b = temp
    return a, b

def intercambia_por_referencia(a: list, b: list) -> tuple[list, list]:
    temp = a.copy()
    a.clear()
    a.extend(b)
    b.clear()
    b.extend(temp)
    return a, b

if __name__ == "__main__":
    print("/"*15)
    print("Extra")
    a, b = intercambia_por_valor(1, 2)
    print(f"Por valor: a: {a}, b: {b}")

    c, d = intercambia_por_referencia([1, 2, 3], [4, 5, 6])
    print(f"Por referencia: c: {c}, d: {d}")