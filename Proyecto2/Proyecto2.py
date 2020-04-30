#Luis Eduardo Núñez Altamirano
#A01633894
#Proyecto algoritmo CYK


#Une los símbolos terminales con el producto cruz
def unir_car(a, b):
    res = set()
    if a == set() or b == set():
        return set()
    for a1 in a:
        for b1 in b:
            res.add(a1+b1)
    return res

def leer_gramatica():
    try:
        gramatica=open("gramatica6.txt")
        leer = gramatica.readlines()
        g = []
        t = []

        for l in leer:
            izq, der = l.split(" -> ")

            # cuando genera mas de una variable
            der = der[:-1].split(" | ")
            for d in der:

                # generador
                if str.isupper(d):
                    g.append([izq, d])

                # terminal
                else:
                    t.append([izq, d])
        return g,t
    except:
        print("Error al abrir archivo")

def leer_expresion():
    try:
        archivo=open("resp6.txt")
        exp=archivo.readlines()
        exp=exp[0][:-1]
        return exp
    except:
        print("Error al abrir archivo")

def cyk_alg(gen, ter, exp):

    largo = len(exp)
    gen0 = [ge[0] for ge in gen]
    gen1 = [ge[1] for ge in gen]

    tab = [[set() for _ in range(largo-i)] for i in range(largo)]

    #Se procesan los generadores
    for i in range(largo):
        for t in ter:
            if exp[i] == t[1]:
                tab[0][i].add(t[0])

    #Se procesan los terminales
    for i in range(1, largo):
        for j in range(largo - i):
            for k in range(i):
                fila = unir_car(tab[k][j], tab[i-k-1][j+k+1])
                for f in fila:
                    if f in gen1:
                        tab[i][j].add(gen0[gen1.index(f)])
    return tab


def imprimir_matriz(tab, exp):
    for c in exp:
        print("\t{}".format(c), end="\t")
    print()
    for i in range(len(exp)):
        print(i+1, end="")
        for c in tab[i]:
            if c == set():
                print("\t{}".format("0"), end="\t")
            else:
                print("\t{}".format(c), end="\t")
        print()

    if 'S' in tab[len(exp)-1][0]:
        print("Sí pertenece a la gramática")
    else:
        print("No pertenece a la gramática")

#----------------------------------------------------
g,t=leer_gramatica()
e = leer_expresion()
ta = cyk_alg(g, t, e)
imprimir_matriz(ta, e)
