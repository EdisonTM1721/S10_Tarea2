class Pila:
    def __init__(self):
        self.valores = []

    def apilar(self,valor):
        self.valores.append(valor)
    
    def pilaVacia(self):
        if(len(self.valores) == 0):
            return True
        else:
            return False
    
    def desapilar(self):
        if(self.pilaVacia()):
            return False
        else:
            self.valores.pop()
    
    def vaciarPila(self):
        if(self.pilaVacia()):
            return False
        else:
            for i in range(len(self.valores)):
                self.desapilar()
            
            return True
    
    def promedio(self):
        total = 0

        for i in self.valores:
            total += i
    
        return total/len(self.valores)

    def getPila(self):
        return self.valores

    def ContarConsonantes(self):
        cant = 0
        for a  in self.valores:
            if a not in ['a','e','i','o','u']:
                cant += 1
    
        return cant

    def ContarVocales(self):
        cant = 0
        for a  in self.valores:
            if a in ['a','e','i','o','u']:
                cant += 1
    
        return cant

