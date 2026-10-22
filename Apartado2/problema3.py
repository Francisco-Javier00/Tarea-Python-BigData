#Francisco Javier Martínez Fernández
""" Escribe una función que reciba dos listas de enteros y devuelva un diccionario
con la siguiente información (ES OBLIGATORIO USAR CONJUNTOS PARA
CALCULARLOS)
1. La intersección de ambos conjuntos (elementos comunes).
2. La unión de ambos conjuntos (todos los elementos sin duplicados).
3. La diferencia simétrica (elementos que están en uno u otro conjunto,
pero no en ambos).  """

#funcion que analiza cual es el la union interseccion y diferencia
def conjuntos(listaNum1, listaNum2):
    lista1=set(listaNum1)
    lista2=set(listaNum2)
    #cada uno de estos tiene su propio metodo para calcularlo
    interseccion=lista1.intersection(lista2)
    if interseccion==set():
        interseccion="No existe interseccion"
    union=lista1.union(lista2)
    if union==set():
        union="No existe union"
    diferenciaSimetrica=lista1.symmetric_difference(lista2)
    if diferenciaSimetrica==set():
        diferenciaSimetrica="No existe diferencia simetrica"
    return interseccion,union,diferenciaSimetrica

#introduccion de la s listas
listaNum1=[]
for x in input("Numeros: ").split():
    try:
        listaNum1.append(int(x))
    except ValueError:
        pass

listaNum2=[]
for x in input("Numeros: ").split():
    try:
        listaNum2.append(int(x))
    except ValueError:
        pass

interseccion,union,diferenciaSimetrica=conjuntos(listaNum1, listaNum2)
print("interseccion: ",interseccion)
print("union: ",union)
print("diferencia_simetrica: ",diferenciaSimetrica)
