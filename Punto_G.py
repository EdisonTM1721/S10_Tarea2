#se importa la libreria system para usar comandos de la consola
from os import system
#se importa la clase cola
from Cola import Cola


#Funcion que contiene el menu con el que interactua el usuario
def menu():
    continuar = ""
    cola = Cola()
    letra = ''

    while(True):
        system("cls")
        cola.vaciarCola()
        print("================ LETRAS =============")
        while(True):
            letra = input("- Ingrese una letra: ")

            if(letra.isnumeric() or letra.isdecimal()):
                break
            elif(len(letra) > 1 or len(letra) == 0):
                print("Ingrese una sola letra!!!")
            
            else:
                cola.encolar(letra)


        print("\n============ RESULTADO =============")
        print(f"- Elementos de la cola: {cola.getCola()}")
        print(f"- La cola contiene {cola.ContarVocales()} vocales.")
        print(f"- La cola contiene {cola.ContarConsonantes()} consonantes.")

        while(True):
            continuar = input("\n¿Desea continuar?(si/no): ")

            if(continuar != "si" and continuar != "no"):
                print("Ingrese 'si' o 'no'!!")
            else:
                break

        if(continuar == "no"):
            print("Hasta pronto!!")
            break

#Se invoca la funcion menu para inciar la ejecucion del programa
menu()