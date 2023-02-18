#se importa la libreria system para usar comandos de la consola
from os import system
#se importa la clase pila
from Pila import Pila

#Funcion que contiene el menu con el que interactua el usuario
def menu():
    continuar = ""
    numero = ""
    pila = Pila()

    while(True):
        system("cls")
        pila.vaciarPila()
        print("============== NUMEROS =============")
        while(True):
            try:
                numero = int(input("- Ingrese un numero: "))
            except:
                print("Ingrese numeros enteros!!")
                continue
                
            if(numero == 0):
                pila.apilar(numero)
                break
            else:
                pila.apilar(numero)

        print("\n============ RESULTADO ============")
        print(f"- Valores de la pila: {pila.getPila()}")
        print(f"- Promedio de los valores de la pila: {pila.promedio()}")

        while(True):
            continuar = input("\n¿Desea continuar?(si/no): ")

            if(continuar != "si" and continuar != "no"):
                print("Ingrese 'si' o 'no'!!")
            else:
                break

        if(continuar == "no"):
            print("Hasta pronto!!")
            break

#Se invoca la funcion menu para iniciar el programa
menu()