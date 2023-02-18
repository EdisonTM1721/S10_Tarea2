#se importa la libreria system para usar comandos de la consola
from os import system
#se importa la clase cola
from Cola import Cola

#Funcion que contiene el menu con el que interactua el usuario
def menu():
    continuar = ""
    cola = Cola()

    while(True):
        system("cls")
        cola.vaciarCola()
        print("============== NUMEROS =============")
        while(True):
            try:
                numero = int(input("- Ingrese un numero: "))
            except:
                print("Ingrese numeros enteros!!")
                continue
                
            if(numero == 0):
                cola.encolar(numero)
                break
            else:
                cola.encolar(numero)

        print("\n============ RESULTADO ============")
        print(f"- Valores de la cola: {cola.getCola()}")
        print(f"- Promedio de los valores de la cola: {cola.promedio()}")

        while(True):
            continuar = input("\n¿Desea continuar?(si/no): ")

            if(continuar != "si" and continuar != "no"):
                print("Ingrese 'si' o 'no'!!")
            else:
                break

        if(continuar == "no"):
            print("Hasta pronto!!")
            break

#se invoca la funcion menu oara inciar la ejecucion del programa
menu()