"""
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
 *   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
"""

cadena = "Python es un lenguaje de programación"

print(f"Longitud de la cadena: {len(cadena)}")
print(f"Primera letra de la cadena: {cadena[0]}")
print(f"Ultima letra de la cadena: {cadena[-1]}")
print(f"Primera palabra de la cadena: {cadena.split()[0]}")
print(f"Primera palabra de la cadena: {cadena.split()[1]}")

print(f"Cadena en mayúsculas: {cadena.upper()}")
print(f"Cadena en minúsculas: {cadena.lower()}")

print(f"Cadena con primera letra en mayúscula: {cadena.capitalize()}")

print(f"Cadena con todas las primeras letras en mayúscula: {cadena.title()}")

print(f"Cadena sin espacios en blanco: {cadena.strip()}")

print(f"Reemplazar 'Python' por 'Java': {cadena.replace('Python', 'Java')}")

print(f'Concatenación de cadenas: {cadena + " y Java"}')

print(f"Subcadenas: {cadena[0:5]}")

print(f"Comprensión de cadenas: {cadena[::2]}")

print(f"Repetición de cadenas: {cadena * 2}")

print(f"Verificación de una palabra en cadenas: {'Python' in cadena}")

print(f'Unión de cadenas: {"-".join(cadena.split())}')

print(f' Cadena con mayúsculas y minúsculas invertidas: {cadena.swapcase()}')


"""
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
 */
"""

def es_palindromo(cadena:str) -> bool:
    return cadena.lower() == cadena.lower()[::-1]

def es_isograma(cadena:str) -> bool:
    return len(set(cadena.lower())) == len(cadena)

def es_anagrama(cadena1:str, cadena2:str) -> bool:
    return sorted(cadena1.lower()) == sorted(cadena2.lower())


if __name__ == "__main__":
    cadena1 = "radar"
    cadena2 = "mora"

    print(f"La primera palabra es un palíndromo: {es_palindromo(cadena1)}")
    print(f"La segunda palabra es un palíndromo: {es_palindromo(cadena2)}")

    print(f"La primera palabra es un isograma: {es_isograma(cadena1)}")
    print(f"La segunda palabra es un isograma: {es_isograma(cadena2)}")

    print(f"Las palabras son anagramas: {es_anagrama(cadena1, cadena2)}")