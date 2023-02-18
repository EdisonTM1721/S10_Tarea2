#se importa la libreria system para usar comandos de la consola
from os import system
#se importa la clase lista
from Lista import Lista

#Funcion que contiene el menu con el que interactua el usuario
def menu():
    continuar = ""
    cadena = ""
    lista = Lista()

    while(True):
        system("cls")
        lista.vaciarLista()
        print("=========== CONSEGUIR CONSONANTES ============")
        cadena = input("- Ingrese una cadena de texto: ")

        print("\n=========== RESULTADO ===========")
        print(f"- La cadena '{cadena}' contiene la sigueintes consonantes: {lista.obtenerConsonantes(cadena)}")

        while(True):
            continuar = input("\n¿Desea continuar?(si/no): ")

            if(continuar != "si" and continuar != "no"):
                print("Ingrese 'si' o 'no'!!")
            else:
                break

        if(continuar == "no"):
            print("Hasta pronto!!")
            break

#Se invoca la funcion menu() para comenzar la ejecucion del programa
menu()