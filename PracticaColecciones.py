dict1={}
dictVJ={"Juego1" : "DOOM",
        "juego2" : "Overwatch",
        "juego3" : "Warzone",
        "juego4" : "Smite",
        "juego5" : "Hollow N",
        "juego6" : "WoW",
        "juego7" : "Fortnite",
        "juego8" : "The Witcher",
        "juego9" : "Castle Crashers",
        "juego10" : "Kirby"}


def sacar(juego):
    if juego=="LoL":
        for k in dictVJ.keys():
            print(k)
    elif juego=="Mario Bros":
        for c in dictVJ:
            print(dictVJ[c])


res= int(input("1=Claves \n2=Valores\n"))
if res==1:
    sacar("LoL")
elif res==2:
    sacar("Mario Bros")


