dict1={}
def ingresarElement():
    claves=input("Ingresa la clave: ")
    valor=input("Ingresa el valor de clave: ")
    dict1[claves]=valor


def Eliminar(eliclav):
    #eliclav=input("Ingresa la clave que queires eliminar: ")
    for k in dict1:
        if k==eliclav:
            del(dict1[k])
            print("Clave eliminada")
        else:
            print("No existe la clave")




while True:
    Imp = input("¿Quieres ingresar un nuevo atributo? S/N\n")
    if Imp.upper()=="S":
        ingresarElement()
    elif Imp.upper()=="N":
        break


#print(dict1)
for c in dict1:
    print(c + " : "+dict1[c])

while True:
    Imp = input("¿Quieres eliminar un nuevo atributo? S/N\n")
    if Imp.upper()=="S":
        
        Eliminar(input("Dame la clave"))
    elif Imp.upper()=="N":
        break

for c in dict1:
    print(c + " : "+dict1[c])