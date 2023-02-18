class Cola:
    def __init__(self):
        self.valores = []

    def encolar(self,valor):
        self.valores.append(valor)

    def colaVacia(self):
        if(len(self.valores) == 0):
            return True
        else:
            return False

    def desencolar(self):
        if(self.colaVacia()):
            return False
        else:
            self.valores.pop(0)
            return True

    def getCola(self):
        return self.valores

    def vaciarCola(self):
        if(self.colaVacia()):
            return False
        else:
            for i in range(len(self.valores)):
                self.desencolar()
            return True
            

    def promedio(self):
        total = 0

        for i in self.valores:
            total += i
    
        return total/len(self.valores)

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