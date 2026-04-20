# Ejercicio 7: Contar ocurrencias de un elemento

def count_occurrences(lista, elemento):
    """
    Cuenta cuántas veces aparece un elemento en la lista.

    Args:
        lista: Una lista de elementos
        elemento: El elemento a buscar

    Returns:
        Un entero con la cantidad de veces que aparece el elemento
    """
    if len(lista) <= 0:
        return 0
    else:
        return lista.count(elemento)

print(count_occurrences([1, 2, 2, 3, 2, 4], 2))
print(count_occurrences([1, 2, 3, 4, 5], 10))
print(count_occurrences(['red', 'blue', 'red', 'green', 'red'], 'red'))



