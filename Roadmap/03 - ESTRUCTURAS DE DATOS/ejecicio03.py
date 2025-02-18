# Estructuras de datos

# Listas
print("\nListas")
lista = [1, 2, 3]
print(f'Elementos de la lista: {lista}')

# Insercion de elementos
print("Insercion de elementos")
lista.append(4)
lista.insert(0, 0)

print(f'Nuevos elementos de la lista: {lista}')

# Modificacion de elementos
print("Modificacion de elementos")
lista[0] = 10
print(f'Nuevos elementos de la lista: {lista}')

# Eliminacion de elementos
print("Eliminacion de elementos")
lista.remove(10)
lista.pop()
print(f'Nuevos elementos de la lista: {lista}')

# Ordenamiento
print("Ordenamiento de elementos")
lista.sort()
print(f'Lista ordenada: {lista}')
lista.reverse()
print(f'Lista invertida: {lista}')

# Tuplas
print("\nTuplas")
tupla = (1, 2, 3)
print(f'Elementos de la tupla: {tupla}')
print('Tuplas son inmutables')

# Diccionarios
print("\nDiccionarios")
diccionario = {'a': 1, 'b': 2, 'c': 3}
print(f'Elementos del diccionario: {diccionario}')

# Insercion de elementos
print("Insercion de elementos")
diccionario['d'] = 4
diccionario.update({'e': 5})
print(f'Nuevos elementos del diccionario: {diccionario}')

# Modificacion de elementos
print("Modificacion de elementos")
diccionario['a'] = 10
print(f'Nuevos elementos del diccionario: {diccionario}')

# Eliminacion de elementos
print("Eliminacion de elementos")
del diccionario['a']
diccionario.pop('b')
print(f'Nuevos elementos del diccionario: {diccionario}')

# Busqueda de elementos
print("Busqueda de elementos")
print(f'Elemento "a" del diccionario: {diccionario.get("a")}')
print(f'Elemento "c" del diccionario: {diccionario["c"]}')

# Sets
print("\nSets")
conjunto = {1, 2, 3}
print(f'Elementos del conjunto: {conjunto}')

# Insercion de elementos
print("Insercion de elementos")
conjunto.add(4)
conjunto.update([5, 6])
print(f'Nuevos elementos del conjunto: {conjunto}')

# Eliminacion de elementos
print("Eliminacion de elementos")
conjunto.remove(1) #arroja error si no existe
conjunto.discard(2) #no arroja error
conjunto.pop() #elimina un elemento aleatorio
print(f'Nuevos elementos del conjunto: {conjunto}')

# Busqueda de elementos
print("Busqueda de elementos")
print(f'Elemento 1 del conjunto: {1 in conjunto}')

# Conjuntos
conjunto_a = {1, 2, 3}
conjunto_b = {3, 4, 5}
conjunto_c = conjunto_a.union(conjunto_b)
conjunto_d = conjunto_a.intersection(conjunto_b)
conjunto_e = conjunto_a.difference(conjunto_b)
conjunto_f = conjunto_a.symmetric_difference(conjunto_b)
print(f'Conjunto A: {conjunto_a}')
print(f'Conjunto B: {conjunto_b}')
print(f'Conjunto C (union): {conjunto_c}')
print(f'Conjunto D (interseccion): {conjunto_d}')
print(f'Conjunto E (diferencia): {conjunto_e}')
print(f'Conjunto F (diferencia simetrica): {conjunto_f}')

# Extra
""" 
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
"""

from enum import Enum

MAX_LEN_NUMERO = 11

class Mensajes(Enum):
    NOMBRE = "Ingrese el nombre del contacto: "
    NUMERO = "Ingrese el telefono del contacto: "
    NOMBRE_EXISTE = "El contacto ya existe."
    NOMBRE_NO_VALIDO = "El nombre del contacto no es valido."
    NUMERO_NO_VALIDO = f"El telefono del contacto no es valido, debe ser numerico o con un maximo de {MAX_LEN_NUMERO} digitos."
    NUMERO_O_NOMBRE_NO_VALIDO = "El telefono o el nombre del contacto no es valido."
    EXITOSA = "Operacion exitosa."

    def __str__(self):
        return self.value


class Agenda:
    def __init__(self):
        self.agenda = {}

    def _buscar_contacto(self, nombre: str) -> str | None:
        return self.agenda.get(nombre)
    
    def _validar_numero(self, numero: str) -> bool:
        return numero.isnumeric() and len(numero) <= MAX_LEN_NUMERO

    def _agregar_contacto(self, nombre: str, telefono: str) -> None:
        if not self._validar_numero(telefono):
            print(Mensajes.NUMERO_NO_VALIDO)

        elif self._buscar_contacto(nombre):
            print(Mensajes.NOMBRE_EXISTE)

        else:
            self.agenda[nombre] = telefono
            print(Mensajes.EXITOSA)

    def _actualizar_contacto(self, nombre: str, telefono: str) -> None:
        if not self._validar_numero(telefono):
            print(Mensajes.NUMERO_NO_VALIDO)

        elif not self._buscar_contacto(nombre):
            print(Mensajes.NOMBRE_NO_VALIDO)

        else:
            self.agenda[nombre] = telefono
            print(Mensajes.EXITOSA)

    def _eliminar_contacto(self, nombre: str) -> None:
        if self._buscar_contacto(nombre):
            del self.agenda[nombre]
            print(Mensajes.EXITOSA)
        else:
            print(Mensajes.NOMBRE_NO_VALIDO)

    def mostrar_agenda(self) -> None:
        for nombre, telefono in self.agenda.items():
            print(f"Nombre: {nombre}, Telefono: {telefono}")

    def agregar_contacto(self) -> None:
        nombre = input(Mensajes.NOMBRE)
        telefono = input(Mensajes.NUMERO)
        self._agregar_contacto(nombre, telefono)

    def actualizar_contacto(self) -> None:
        nombre = input(Mensajes.NOMBRE)
        telefono = input(Mensajes.NUMERO)
        self._actualizar_contacto(nombre, telefono)

    def eliminar_contacto(self) -> None:
        nombre = input(Mensajes.NOMBRE)
        self._eliminar_contacto(nombre)

    def buscar_contacto(self) -> None:
        nombre = input(Mensajes.NOMBRE)
        telefono = self._buscar_contacto(nombre)
        if telefono:
            print(f"El contacto {nombre} tiene el siguiente telefono: {telefono}")
        else:
            print(Mensajes.NOMBRE_NO_VALIDO)

print("\n")
print('/'*15)
print("\n")

print("Agenda de contactos")
agenda = Agenda()

while True:
    print("\nMenu de opciones:")
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Actualizar contacto")
    print("4. Eliminar contacto")
    print("5. Mostrar agenda")
    print("6. Salir")

    opcion = input("Ingrese la opcion que desea realizar: ")

    match opcion:
        case "1":
            agenda.agregar_contacto()
        case "2":
            agenda.buscar_contacto()
        case "3":
            agenda.actualizar_contacto()
        case "4":
            agenda.eliminar_contacto()
        case "5":
            agenda.mostrar_agenda()
        case "6":
            print("Saliendo del programa...")
            break
        case _:
            print('Opcion no valida.\n')

