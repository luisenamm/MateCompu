#Luis Eduardo Núñez Altamirano
#A01633894
#Proyecto reemplazador de cadenas

original=input("Ingresa la cadena original\n")
entrada=input("Ingresa la expresión regular\n")
reemplazar=input("Ingresa la cadena a reemplazar\n")
nuevoVal=entrada.split('+')
#print(nuevoVal)
print ("Entrada: "+original)
val=len(nuevoVal)

#Caso con espacios
if " " in original:
    #Hay mínimo un + en la expresión
    if val>1:
      for i in range(0,val):
        size=len(nuevoVal[i])

        #Comprueba si hay cerradura intermedia
        if '*' in nuevoVal[i][:-1]:
          Ast= nuevoVal[i].split('*')
          numAst=len(Ast)
          busca2=""
          #print(Ast)

          for i in range(0,numAst):
            size=len(Ast[i])

            if size>1:
                #Le quitas el último elemento
              busca = Ast[i][:-1]
                #El último elemento, el que tiene la cerradura
              last = Ast[i][size-1]
            else:
              busca = Ast[i]
              last=busca

            #Concatenación de la parte de la cadena que se repite
            for j in original:
              if busca+last in original:
                busca=busca+last

            #Suma el elemento que sigue si es parte de la expresión
            if busca in original:
              busca2=busca2+busca

          salidaFinal=original.replace(busca2,reemplazar)
          original=salidaFinal

         #Cuando la cerradura es final
        else:
          if size>=3:
            last=nuevoVal[i][size-2]
            #print("last: "+last)
            busca=nuevoVal[i][:-2]
            #print("busca: "+busca)

            for j in original:
                if busca+last in original:
                    busca=busca+last
            salidaFinal=original.replace(busca,reemplazar)
            original=salidaFinal

          if size==2:
            busca=nuevoVal[i][:-1]
            if busca in original:
              salidaFinal=original.replace(busca,reemplazar)
              original=salidaFinal

    #Que no hubo un +
    else:
      Ast= entrada.split('*')
      numAst=len(Ast)

      busca2=""

      for i in range(0,numAst):
        size=len(Ast[i])

        if size>1:
            #Le quitas el último elemento (cerradura)
          busca = Ast[i][:-1]
          #El elemento con cerradura
          last = Ast[i][size-1]
        else:
          busca = Ast[i]
          last=busca

        for j in original:
              if busca+last in original:
                  busca=busca+last

        if busca in original:
          busca2=busca2+busca


      salidaFinal=original.replace(busca2,reemplazar)
      original=salidaFinal

    #Contador del número de espacios
    cont=0

    for i in original:
      if " " in original:
        cont=cont+1

    #Reduce todos los espacios que hay y deja solo uno
    for i in range(0,cont):
      salidaTemp=original.replace("  "," ")
      salidaFinal=salidaTemp
      original=salidaFinal

     #Última revisada por si hay espacios de más
    for i in range(0,val):
        busca=nuevoVal[i][:-2]
        if busca in salidaTemp:
          salidaFinal=salidaTemp.replace(busca,reemplazar)
          original=salidaFinal


#Caso sin espacios:
else:
    #Hay mínimo un + en la expresión
    if val>1:
      for i in range(0,val):
        size=len(nuevoVal[i])

        #Comprueba si hay cerradura intermedia
        if '*' in nuevoVal[i][:-1]:
          Ast= nuevoVal[i].split('*')
          numAst=len(Ast)
          busca2=""
          #print(Ast)

          for i in range(0,numAst):
            size=len(Ast[i])

            if size>1:
                #Quitas el último elemento
              busca = Ast[i][:-1]
                #Elemento con la cerradura
              last = Ast[i][size-1]
            else:
              busca = Ast[i]
              last=busca

              #Recorre la cadena para buscar si están los elementos
            for j in original:
              if busca+last in original:
                busca=busca+last

            if busca in original:
              busca2=busca2+busca

          salidaFinal=original.replace(busca2,reemplazar)
          original=salidaFinal

          #Cuando no hay cerradura intermedia
        else:
          if size>=3:
            last=nuevoVal[i][size-2]
            #print("last: "+last)
            busca=nuevoVal[i][:-2]
            #print("busca: "+busca)

            for j in original:
                if busca+last in original:
                    busca=busca+last
            salidaFinal=original.replace(busca,reemplazar)
            original=salidaFinal

          if size==2:
            busca=nuevoVal[i][:-1]
            if busca in original:
              salidaFinal=original.replace(busca,reemplazar)
              original=salidaFinal


    #Cuando no hay una unión
    else:
      Ast= entrada.split('*')
      numAst=len(Ast)

      busca2=""

      for i in range(0,numAst):
        size=len(Ast[i])

        if size>1:
          busca = Ast[i][:-1]
          last = Ast[i][size-1]
        else:
          busca = Ast[i]
          last=busca

        for j in original:
              if busca+last in original:
                  busca=busca+last

        if busca in original:
          busca2=busca2+busca


      salidaFinal=original.replace(busca2,reemplazar)
      original=salidaFinal




print ("Salida: "+salidaFinal)
