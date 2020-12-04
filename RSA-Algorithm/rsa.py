import math
import random
def mcd(a, b):
   #Máximo común divisor de a y b
    if (b == 0):
        return a
    else:
        return mcd(b, a % b)

def xmcd(a, b):
   #Mcd más coeficiente de a y b
    x, x0 = 0, 1
    y, y0 = 1, 0
    while (b != 0):
        cociente = a // b
        a, b = b, a - cociente * b
        x0, x = x, x0 - cociente * x
        y0, y = y, y0 - cociente * y
    return a, x0, y0

def generarE(cociente):
  
    while (True):
        e = random.randrange(2, cociente)
        if (mcd(e, cociente) == 1):
            return e

def generarLlaves():
  
    rand1 = random.randint(100, 300)
    rand2 = random.randint(100, 300)
    
    archivo = open('num_prim.txt', 'r')
    linea = archivo.read().splitlines()
    archivo.close()
    
    prim1 = int(linea[rand1])
    prim2 = int(linea[rand2])
    
    #generar n, cociente y e
    n = prim1 * prim2
    cociente = (prim1 - 1) * (prim2 - 1)
    e = generarE(cociente)
    # generar d (mod cociente)
    # e y d son inversos (mod cociente)
    mcd, x, y = xmcd(e, cociente)
    # d tiene que ser positivo
    if (x < 0):
        d = x + cociente
    else:
        d = x
    
    f_publ = open('publ.txt', 'w')
    f_publ.write(str(n) + '\n')
    f_publ.write(str(e) + '\n')
    f_publ.close()
    f_priv = open('priv.txt', 'w')
    f_priv.write(str(n) + '\n')
    f_priv.write(str(d) + '\n')
    f_priv.close()

def encriptar(mensaje, file_name = 'publ.txt', block_size = 2):

    try:
      archivo = open(file_name, 'r')
    except FileNotFoundError:
        print('No se encuentra el archivo')
    else:
        n = int(archivo.readline())
        e = int(archivo.readline())
        archivo.close()
        encrypted_blocks = []
        ciphertext = -1
        if (len(mensaje) > 0):
        #Origina el ascii
            ciphertext = ord(mensaje[0])
        for i in range(1, len(mensaje)):
           #Agrega el texto ascii al arreglo y genera otra vez
            if (i % block_size == 0):
                encrypted_blocks.append(ciphertext)
                ciphertext = 0

            #X1000 para generar los 3 digitos del ascii
            ciphertext = ciphertext * 1000 + ord(mensaje[i])
        encrypted_blocks.append(ciphertext)

        #Número elevado a la "e" y mod "n"
        for i in range(len(encrypted_blocks)):
            #encrypted_blocks[i] = str((encrypted_blocks[i]**e) % n)
            encrypted_blocks[i]=str(pow(encrypted_blocks[i],e,n))

            #Crea el string y lo une con los números
        encrypted_message = " ".join(encrypted_blocks)

        return encrypted_message

def desencriptar(blocks, block_size = 2):

    archivo = open('priv.txt', 'r')
    n = int(archivo.readline())
    d = int(archivo.readline())
    archivo.close()

    #Hace el string un arreglo de int
    list_blocks = blocks.split(' ')
    int_blocks = []

    for s in list_blocks:
        int_blocks.append(int(s))

    mensaje = ""

    
    for i in range(len(int_blocks)):
       #desencripta a la potencia "d" y mod "n"
        int_blocks[i] =pow(int_blocks[i],d,n)
        
        tmp = ""
       #Separa cada caracter en su código ascii
        for c in range(block_size):
            tmp = chr(int_blocks[i] % 1000) + tmp
            int_blocks[i] //= 1000
        mensaje += tmp

    return mensaje

def main():
   
    genLlaves = input('Generar nuevas llaves? (s/n) ')
    if (genLlaves == 's'):
        generarLlaves()
    elif(genLlaves != 's' and genLlaves != 'n'):
        print ("Instruccion no valida")
        return
    instruccion = input('Encriptar o desencriptar? (e/d): ')
    if (instruccion == 'e'):
        mensaje = input('Ingrese el mensaje a encriptar\n')
        print('Encriptando')
        print(encriptar(mensaje))

    elif (instruccion == 'd'):
        mensaje = input('Ingrese lo que desea desencriptar\n')
        print('Desencriptando')
        print(desencriptar(mensaje))
    else:
        print('instruccion no valida')

main()