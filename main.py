def capitalizar(aux):
    return aux.capitalize()


def concatenar(p1,p2,p3):
    return p1+" "+p2+" "+p3


def mitades(parte):
    tam = int (len(parte)/2)
    tam2 = parte[tam:]
    print("La primera mitad es:"+ parte[:tam])
    print("La segunda mitad es:"+ tam2[::-1])


def imprimir(x,nombrecom):
    cont = 0
    while cont<int(x):
        print(nombrecom)
        cont += 1


cad01="hola"
cad02=" "
cad03="Mundo"

nombre = input("Dame tu nombre:")
apellidoP = input("Apellido Paterno")
apellidoM = input("Apellido Materno")

nombre = capitalizar(nombre)
apellidoP = capitalizar(apellidoP)
apellidoM = capitalizar(apellidoM)

nombrecom = concatenar(nombre,apellidoP,apellidoM)

mitades(nombrecom)
rep = input("Veces a repetir: ")
imprimir(rep,nombrecom)
