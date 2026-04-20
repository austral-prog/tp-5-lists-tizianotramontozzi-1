# Ejercicio 8: Invertir una lista

def reverse_list(lista):
    """
    Retorna una nueva lista con los elementos en orden inverso.

    Args:
        lista: Una lista de elementos

    Returns:
        Una nueva lista con los elementos en orden inverso
    """
    if len(lista) <= 0:
        return []
    else:
        return lista[::-1]

print(reverse_list([1, 2, 3, 4, 5]))
print(reverse_list(['a', 'b', 'c', 'd']))
print(reverse_list([]))

