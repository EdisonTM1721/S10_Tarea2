#se importa la libreria system para usar comandos de la consola
from os import system
#se importa la clase lista
from Lista import Lista

#Funcion que contiene el menu para pedir y mostrar la secuencia 
def menu():
    continuar = ""
    secuencia = Lista()
    caracter = ""
    cantidad = 0
    while(True):
        system("cls")
        secuencia.vaciarLista()
        print("============== INVERTIR SECUENCIA =============")
        while(True):
            try:
                cantidad = int(input("- ¿Cuantos caracteres desea ingresar?: "))
            except:
                print("Ingrese solo numeros!!")
                continue
                
            break

        print("\n======== CARACTERES ========")
        for i in range(cantidad):
            while(True):
                caracter = input("- Ingrese un caracter: ")
                if(caracter.isnumeric() or caracter.isdecimal()):
                    print("Ingrese solo caracteres!!")
                elif(len(caracter) > 1):
                    print("Ingrese un solo caracter!!")
                else:
                    break
            secuencia.agregar(caracter)

        print("\n========== RESULTADO ===========")
        print(f"-Secuencia normal: {secuencia.getLista()}")
        secuencia.invertirSecuencia()
        print(f"- Secuencia invertida: {secuencia.getLista()}")

        while(True):
            continuar = input("\n¿Desea continuar?(si/no): ")

            if(continuar != "si" and continuar != "no"):
                print("Ingrese 'si' o 'no'!!")
            else:
                break

        if(continuar == "no"):
            print("Hasta pronto!!")
            break

#Se invoca la funcion menu()
menu()