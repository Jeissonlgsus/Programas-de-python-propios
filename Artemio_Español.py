texto = input("ingrese texto en español: ")
alfabeto = ['b','c','d','f','g','h','j','k','l',
'm','n','ñ','p','q','r','s','t','v','w','x','y',
'z','espacio','a','e','i','o','u',' ']
for letra in texto:
    valor = alfabeto.index(letra)
    #print(letra + " es igual a: "+str(valor))
    valor = valor-1
    if valor == 22:
        valor = 27    
        #print(letra + " vale ahora "+str(valor))
    elif valor == -1:
        valor = 21
    elif valor == 27:
        valor = 28
        #print(letra + " vale ahora "+str(valor))
    #else:
        #print(letra + " vale ahora "+str(valor))
    text = alfabeto[valor]
    print(text,end="")