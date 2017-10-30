# Calculadora de fraccionarios

class Fraccionario:
    
    # constructor
    def __init__(self, n=0, d=1):
        self.__numerador = n
        self.__denominador = d
        
        
    """
    Metodo para sumar fracciones
    """
    def sumar(self, otra):
        neoNumerador = self.getNumerador() * otra.getDenominador() + self.getDenominador() * otra.getNumerador()
        # si son fracciones homogeneas
        if self.__denominador == otra.getDenominador():
            neoDenominador = otra.getDenominador()
        else:
            neoDenominador = self.__denominador * otra.getDenominador()

        nueva = Fraccionario(neoNumerador, neoDenominador)
        return nueva
    
    """
    Metodo para restar fracciones
    """
    def restar(self, otra):
        nueva = Fraccionario()
        
        neoNumerador = self.getNumerador() * otra.getDenominador() - self.getDenominador() * otra.getNumerador()
        # si son fracciones homogeneas
        if self.__denominador == otra.__denominador:
            neoDenominador = otra.getDenominador()
        else:
            neoDenominador = self.__denominador * otra.getDenominador()

        nueva.setNumerador(neoNumerador)
        nueva.setDenominador(neoDenominador)
        return nueva
        
    """
    Metodo para multiplicar fracciones
    """
    def multiplicar(self, otra):
        neoNumerador = self.getNumerador() * otra.getNumerador()
        neoDenominador = self.getDenominador() * otra.getDenominador()
        nueva = Fraccionario(neoNumerador, neoDenominador)
        return nueva
    
    """
    Metodo para dividir fracciones
    """
    def dividir(self, otra):
        neoNumerador = self.getNumerador() * otra.getDenominador()
        neoDenominador = self.getDenominador() * otra.getNumerador()
        nueva = Fraccionario(neoNumerador, neoDenominador)
        return nueva
    
    # metodos set
    def setNumerador(self, n):
        self.__numerador = n
    
    def setDenominador(self, d):
        self.__denominador = d
        
    # metodos get
    def getNumerador(self):
        return self.__numerador
    
    def getDenominador(self):
        return self.__denominador
    
    def toString(self):
        return str(self.getNumerador()) + "/" + str(self.getDenominador())


#esta parte serìa main 

f1 = Fraccionario(3, 4)
f2 = Fraccionario(2, 5)

print(f1.toString())
print(f2.toString())


print("sumar:")
rta = f1.sumar(f2)
print(rta.toString())

print("restar:")
rta = f1.restar(f2)
print(rta.toString())

print("producto:")
rta = f1.multiplicar(f2)
print(rta.toString())

print("dividir:")
rta = f1.dividir(f2)
print(rta.toString())


