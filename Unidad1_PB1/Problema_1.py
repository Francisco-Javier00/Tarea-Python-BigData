#Francisco Javier Martínez Fernández
"""  Problema 1. Procesamiento de una lista de enteros.
Crea una función que reciba una lista de enteros por parámetro y devuelva otra
lista, de acuerdo a las siguientes acciones:
1. Eliminar los números negaƟvos de la lista.
2. Eliminar los valores que están repeƟdos, quedándonos con uno de ellos.
3. Ordenar los números resultantes de menor a mayor.
Por ejemplo, si le pasara [4, -1, 2, 4, 3, -5, 2], debería retornar [2,3,4].
"""

#funcion la caul va a filtrar los negativos quitandolos
def filtro(num):
    numerosEntero={
        x for x in num if x>=0
    }
    return sorted(numerosEntero)

#introducir los numeros al array puse que ignore las letras para que sea mas limpia la pantalla asi no salen fallos 
listaNum=[]
for x in input("Numeros: ").split():
    try:
        listaNum.append(int(x))
    except ValueError:
        pass

resultado=filtro(listaNum)
print("Lista: ",resultado)