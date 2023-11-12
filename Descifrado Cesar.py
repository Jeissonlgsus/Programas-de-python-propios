texto = input("ingrese texto en español: ")
residuo = int(input("Ingrese código de cifrado: "))
consonantesm = ['B','C','D','F','G',
                'H','J','K','L','M',
                'N','Ñ','P','Q','R',
                'S','T','V','W','X',
                'Y','Z']
vocalesm = ['A','E','I','O','U']
consonantes = ['b','c','d','f','g',
               'h','j','k','l','m',
               'n','ñ','p','q','r',
               's','t','v','w','x',
               'y','z']
vocales = ['a','e','i','o','u']
simbolos = ['.',',',':',';','(',
            ')'," "]
for letra in texto:
    if letra in consonantes:
        valor = consonantes.index(letra)
        #print(letra + " es una consonante y su valor es " + str(valor)) 
        valor = valor - residuo
        #print(letra + " es una consonante y su nuevo valor es " + str(valor))
        if valor < 0:
            valor = valor % 22
            #print("El valor modular de " + letra + " es "+ str(valor))
        text = consonantes[valor]
    elif letra in consonantesm:
        valor = consonantesm.index(letra)
        #print(letra + " es una consonante y su valor es " + str(valor)) 
        valor = valor - residuo
        #print(letra + " es una consonante y su nuevo valor es " + str(valor))
        if valor < 0:
            valor = valor % 22
            #print("El valor modular de " + letra + " es "+ str(valor))
        text = consonantesm[valor]
    elif letra in vocalesm:
        valor = vocalesm.index(letra)
        #print(letra + " es una vocal y su valor es " + str(valor))
        valor = valor - residuo
        #print(letra + " es una vocal y su nuevo valor es " + str(valor))
        if valor < 0:
            valor = valor % 5
            #print("El valor modular de " + letra + " es "+ str(valor))
        text = vocalesm[valor]
    elif letra in vocales:
        valor = vocales.index(letra)
        #print(letra + " es una vocal y su valor es " + str(valor))
        valor = valor - residuo
        #print(letra + " es una vocal y su nuevo valor es " + str(valor))
        if valor < 0 :
            valor = valor % 5
            #print("El valor modular de " + letra + " es "+ str(valor))
        text = vocales[valor]
    else:
        valor = simbolos.index(letra)
        #print(letra + " es un simbolo y su valor es " + str(valor))
        #print(letra + " es un simbolo y su nuevo valor es " + str(valor))
        text = simbolos[valor]
    print(text,end="")