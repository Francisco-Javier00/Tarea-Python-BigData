#Francisco Javier Martínez Fernández
""" Problema 2. Frecuencia de palabras en un texto.
Escribe una función que reciba por parámetro una lista de palabras y la ruta a
un fichero de texto y devuelva un diccionario que muestre cuantas veces
aparecen las disƟntas palabras de la lista en el fichero de texto. Haz un pequeño
programa que la ponga a prueba.
Requisitos:
1. Eliminar signos de puntuación y converƟr todo a minúsculas.
2. Usar un diccionario donde la clave sea la palabra y el valor su frecuencia.
3. Mostrar las palabras y sus frecuencias de forma ordenada por la palabra.  """

# funcion que cuenta las veces que aparece una palabra en un fichero
def conteoPalabras(ruta, listaPalabras):
    fichero=open(ruta,"r")
    texto=fichero.read()
    fichero.close()
    #poner minuscalas se usa .lower
    texto=texto.lower()
    #quitar parentesis y signos de puntuacion
    signos=['.',',',';',':','!','?','(',')']
    for x in signos:
        texto=texto.replace(x,'')

    palabras=texto.split()
    numeroVeces={}
    for x in listaPalabras:
        numeroVeces[x]=palabras.count(x.lower())
    return numeroVeces


# Llamada a la funcion
listaPalabras=["numero","2","prueba","abecedario"]
numeroVeces=conteoPalabras("texto.txt", listaPalabras)
for palabra in sorted(numeroVeces):
    print(palabra,":",numeroVeces[palabra])

