# Ejercicio 11: Comparar tercer elemento de dos listas

def check_lists(lista1, lista2):
    """
    Verifica si ambas listas tienen el mismo elemento en la tercera posición.
    Si alguna de las listas no tiene un tercer elemento, retorna False.

    Args:
        lista1: Primera lista
        lista2: Segunda lista

    Returns:
        True si ambas listas tienen el mismo tercer elemento, False en caso contrario
    """
    if len(lista1)>3 and len(lista2)>3 and lista1[2] == lista2[2]:
        return True
    else:
        return False

print(check_lists(['Black', 'Pink', 'Yellow', 'Red', 'Green', 'White'], ['Red', 'Green', 'Yellow', 'White', 'Black', 'Pink']))
print(check_lists(['Black', 'Pink', 'Green', 'White'],['Red', 'Green', 'Yellow', 'Black', 'Pink']))
print(check_lists(['Black', 'Pink'], ['Red', 'Green', 'Yellow', 'Black', 'Pink']))