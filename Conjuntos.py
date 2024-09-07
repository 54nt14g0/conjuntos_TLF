
from typing import Set
import matplotlib as plt
from matplotlib_venn import venn3

def calcular_interseccion(conjunto_a, conjunto_b):
    """Calcula la intersección de dos conjuntos."""
    interseccion = set()
    for elemento in conjunto_a:
        if elemento in conjunto_b:
            interseccion.add(elemento)
    return interseccion

def main():

 # Obtener datos de los conjuntos del usuario
    conjunto_a = input("Introduce los elementos del conjunto A, separados por comas: ").split(',')
    conjunto_b = input("Introduce los elementos del conjunto B, separados por comas: ").split(',')
    conjunto_c = input("Introduce los elementos del conjunto C, separados por comas: ").split(',')
    
    # Limpiar espacios en blanco
    conjunto_a = set(item.strip() for item in conjunto_a)
    conjunto_b = set(item.strip() for item in conjunto_b)
    conjunto_c = set(item.strip() for item in conjunto_c)
    
    # Crear el conjunto universo (U)
    conjunto_universo = conjunto_a.union(conjunto_b).union(conjunto_c).union({'ElementoExtra1', 'ElementoExtra2'})
    
    # Encontrar intersecciones entre los conjuntos
    interseccion_ab = calcular_interseccion(conjunto_a, conjunto_b)
    interseccion_ac = calcular_interseccion(conjunto_a, conjunto_c)
    interseccion_bc = calcular_interseccion(conjunto_b, conjunto_c)
    interseccion_abc = conjunto_a.intersection(conjunto_b).intersection(conjunto_c)
    
    # Imprimir resultados
    print("Conjunto A:", conjunto_a)
    print("Conjunto B:", conjunto_b)
    print("Conjunto C:", conjunto_c)
    print("Intersección de A y B:", interseccion_ab)
    print("Intersección de A y C:", interseccion_ac)
    print("Intersección de B y C:", interseccion_bc)
    print("Intersección de A, B y C:", interseccion_abc)
    print("Conjunto Universo:", conjunto_universo)
    
    # Crear etiquetas para el diagrama de Venn
    subset_sizes = {
        '100': len(conjunto_a - conjunto_b - conjunto_c),
        '010': len(conjunto_b - conjunto_a - conjunto_c),
        '001': len(conjunto_c - conjunto_a - conjunto_b),
        '110': len(interseccion_ab - conjunto_c),
        '101': len(interseccion_ac - conjunto_b),
        '011': len(interseccion_bc - conjunto_a),
        '111': len(interseccion_abc)
    }
    
    labels = {
        '100': ', '.join(conjunto_a - conjunto_b - conjunto_c),
        '010': ', '.join(conjunto_b - conjunto_a - conjunto_c),
        '001': ', '.join(conjunto_c - conjunto_a - conjunto_b),
        '110': ', '.join(interseccion_ab - conjunto_c),
        '101': ', '.join(interseccion_ac - conjunto_b),
        '011': ', '.join(interseccion_bc - conjunto_a),
        '111': ', '.join(interseccion_abc)
    }
    
    # Crear el diagrama de Venn
    plt.figure(figsize=(12, 8))
    venn = venn3(subsets=subset_sizes, set_labels=('Conjunto A', 'Conjunto B', 'Conjunto C'))
    
    # Personalizar etiquetas del diagrama
    for subset, label in labels.items():
        if venn.get_label_by_id(subset):
            venn.get_label_by_id(subset).set_text(label)
    
    plt.title("Diagrama de Venn de los Conjuntos A, B y C")
    plt.show()



    # Código principal del programa
    print("¡Hola, mundo!")

    lista1 = [1,2,3]
    lista2 = [2,3,4,5]


    conjuntoUnion = union (lista1,lista2)
    print(conjuntoUnion)

    conjuntoInterseccion = interseccion (lista1, lista2)
    print(conjuntoInterseccion)

    conjuntoDiferencia = diferencia (lista1,lista2)
    print (conjuntoDiferencia)

    conjuntoDiferenciaSimetrica = diferenciaSimetrica (lista1,lista2)
    print (conjuntoDiferenciaSimetrica)


def union (lista1,  lista2):

    conjuntoFinal = set()
    contador = 0
    contador2 = 0
    
    while contador < len(lista1):

        conjuntoFinal.add(lista1[contador])
        contador +=1    

    while contador2 < len(lista2):
        conjuntoFinal.add(lista2[contador2])
        contador2 +=1

    return conjuntoFinal



def interseccion(lista1, lista2):
    i = 0
    conjuntoFinal = set()
    
    while i < len(lista1):
        j = 0  # Reiniciar j para cada elemento de lista1
        while j < len(lista2):
            if lista1[i] == lista2[j]:
                conjuntoFinal.add(lista1[i])
            j += 1
        i += 1

    return conjuntoFinal

def diferencia (lista1, lista2):
    conjuntoFinal = set()
    i=0
    conjuntoInterseccion = convertirSetALista(interseccion (lista1, lista2))
    bandera = True

    while i< len(lista1):
        j=0
        while j< len(conjuntoInterseccion):
            
            if (conjuntoInterseccion[j] ==lista1[i]) and (bandera==True):
                bandera = False

            j+=1

        if (bandera == True):

            conjuntoFinal.add(lista1[i])
        bandera = True
        i+=1


    return conjuntoFinal


def convertirSetALista(conjunto):
    # Convertir el set a una lista
    lista = list(conjunto)
    return lista



def diferenciaSimetrica (lista1, lista2):
    conjuntoFinal = set()

    conjuntoA = diferencia(lista1,lista2)
    conjuntoB = diferencia(lista2,lista1)



    conjuntoFinal = union (convertirSetALista(conjuntoA),convertirSetALista( conjuntoB))


    return conjuntoFinal



def es_subconjunto(conjunto1: Set, conjunto2: Set) -> bool:
  
    return conjunto1 <= conjunto2


#métodos pero con tres conjuntos de entrada

def unionTres(conjunto1, conjunto2, conjunto3):
    """
    Calcula la unión de tres conjuntos usando ciclos.

    Args:
        conjunto1 (list): Primer conjunto como lista.
        conjunto2 (list): Segundo conjunto como lista.
        conjunto3 (list): Tercer conjunto como lista.

    Returns:
        set: La unión de los tres conjuntos.
    """
    conjuntoFinal = set()

    for item in conjunto1:
        conjuntoFinal.add(item)
    
    for item in conjunto2:
        conjuntoFinal.add(item)
    
    for item in conjunto3:
        conjuntoFinal.add(item)
    
    return conjuntoFinal

def interseccionTres(conjunto1, conjunto2, conjunto3):
    """
    Calcula la intersección de tres conjuntos usando ciclos.

    Args:
        conjunto1 (list): Primer conjunto como lista.
        conjunto2 (list): Segundo conjunto como lista.
        conjunto3 (list): Tercer conjunto como lista.

    Returns:
        set: La intersección de los tres conjuntos.
    """
    conjuntoFinal = set()

    for item in conjunto1:
        if item in conjunto2 and item in conjunto3:
            conjuntoFinal.add(item)
    
    return conjuntoFinal

def diferenciaTres(conjunto1, conjunto2, conjunto3):
    """
    Calcula la diferencia entre el primer conjunto y la unión de los otros dos conjuntos usando ciclos.

    Args:
        conjunto1 (list): Primer conjunto como lista.
        conjunto2 (list): Segundo conjunto como lista.
        conjunto3 (list): Tercer conjunto como lista.

    Returns:
        set: La diferencia entre el primer conjunto y la unión de los otros dos conjuntos.
    """
    conjuntoFinal = set()

    # Convertir conjuntos 2 y 3 a un conjunto para usar en la unión
    conjuntoUnion = set(conjunto2)
    conjuntoUnion.update(conjunto3)

    for item in conjunto1:
        if item not in conjuntoUnion:
            conjuntoFinal.add(item)
    
    return conjuntoFinal

def diferenciaSimetricaTres(conjunto1, conjunto2, conjunto3):
    """
    Calcula la diferencia simétrica entre tres conjuntos usando ciclos.

    Args:
        conjunto1 (list): Primer conjunto como lista.
        conjunto2 (list): Segundo conjunto como lista.
        conjunto3 (list): Tercer conjunto como lista.

    Returns:
        set: La diferencia simétrica entre los tres conjuntos.
    """
    conjuntoFinal = set()
    unionConjuntos = set(conjunto1 + conjunto2 + conjunto3)

    for item in unionConjuntos:
        count = sum([item in conjunto1, item in conjunto2, item in conjunto3])
        if count == 1:
            conjuntoFinal.add(item)
    
    return conjuntoFinal

def es_subconjuntoTres(conjunto1, conjunto2):
    """
    Verifica si el primer conjunto es un subconjunto del segundo usando ciclos.

    Args:
        conjunto1 (list): Primer conjunto como lista.
        conjunto2 (list): Segundo conjunto como lista.

    Returns:
        bool: True si el primer conjunto es un subconjunto del segundo, False en caso contrario.
    """
    for item in conjunto1:
        if item not in conjunto2:
            return False
    return True





main()



