#se importa la libreria system para usar comandos de la consola
from os import system
#se importa la clase lista
from Lista import Lista

#Funcion que contiene el menu con el cual interactua el usuario
def menu():
    continuar = ""
    cadena_1 = ""
    cadena_2 = ""
    intercalado = ""
    lista = Lista()

    while(True):
        system("cls")
        lista.vaciarLista()
        intercalado = ""

        print("=============== INTERCALAR ==============")
        cadena_1 = input("- Ingrese una cadena de texto: ")

        while(True):
            cadena_2 = input("- Ingrese otra cadena de texto: ")
            if(len(cadena_1) == len(cadena_2)):
                break
            else:
                print("\nIngrese una cadena con la misma longitud que la primera!!")

        print("\n============ RESULTADO ==========")
        print(f"- Cadena 1: {cadena_1}")
        print(f"- Cadena 2: {cadena_2}")

        for i in lista.intercalar(cadena_1,cadena_2):
            intercalado += i

        print(f"- cadena Intercalada: {intercalado}")

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