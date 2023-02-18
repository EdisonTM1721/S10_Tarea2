class Lista:
    def __init__(self):
        self.lista = []

    def agregar(self,valor):
        self.lista.append(valor)
    
    def listaVacia(self):
        if(len(self.lista) == 0):
            return True
        else:
            return False

    def eliminarPosicion(self, posicion):
        if(self.listaVacia()):
            return False
        else:
            self.lista.pop(posicion)
            return True
    
    def eliminarElemento(self,valor):
        if(self.listaVacia()):
            return False
        else:
            self.lista.remove(valor)
            return True
        
    def vaciarLista(self):
        self.lista.clear()

    def getLista(self):
        return self.lista

    #Funcion para invertir la secuencia de caracteres
    def invertirSecuencia(self):
        for i in range(len(self.lista)-1,-1,-1):
            self.lista.append(self.lista[i])
            self.lista.pop(i)

    #Funcion para intecalar dos cadenas de texto
    def intercalar(self,cadena_1,cadena_2):

        for i in range(len(cadena_1)):
            self.lista.append(cadena_1[i])
            self.lista.append(cadena_2[i])
        
        return self.lista

    #Funcion para obtener una lista con las consonates de una cadena de texto
    def obtenerConsonantes(self,cadena):
        for a  in cadena:
            if a not in ['a','e','i','o','u']:
                self.lista.append(a)
        
        return self.lista