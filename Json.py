import json
# some JSON:

# {"Carne":64,"Garbanzo":88,"Fruta":54,"Lenteja":94,"Verdura":66}
# entrada de prueba 1 = entrada
# Fruta Leche Papa Huevos Carne
# entrada de prueba 2 = entrada2
entrada = input('') # ingresa un diccionario como str
entrada2 = input('') # ingresa palabras con espacio

#entrada = '{"Carne":64,"Garbanzo":88,"Fruta":54,"Lenteja":94,"Verdura":66}'
#entrada2 = 'Fruta Leche Papa Huevos Carne'
z = entrada2.split(' ') # separa los valores de la segunda entrada en elementos inidividuales por espacio
# parse x:
y = json.loads(entrada) # carga el str como un diccionario con metodo Json
listaproductos = list(z) # convierte los elementos separados del str en una lista
listapuntos = list(y)

lista2 = []
valores = []
ponderado = []

for i in listaproductos:
    if i in listapuntos:
        lista2.append(i)
# lista2 = [Fruta,Carne]

for j in lista2:
    x = listapuntos.index(j) #Fruta = 2 ; Carne = 0
    valores.append(x) # valores = [2,0]   
#print(valores)

for k in valores:
    a = y[listapuntos[k]]
    ponderado.append(a)
    
#print(ponderado)

total = sum(ponderado)
print (total)


 

listafinal = ' '.join(lista2) 

#print(listaproductos)
#print(listapuntos)
    # the result is a Python dictionary:
    #print(listapuntos[2])
    # la salida debe ser:
    # 118
    #Fruta Carne
print(listafinal) 

