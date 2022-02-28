
class operacionesMatematicas:
    def __init__(self, op1, op2):
        self.op1 = op1
        self.op2 = op2

    def suma(self) :
        """
        Método de la suma, aplica al operador la suma de op1 + op2
        """

        res = self.op1+self.op2
        return res

    def producto(self) :
        """
        Método que multiplica op1 * op2

        """
        return self.op1*self.op2

    def division(self) :
        """
        Método que divide op1 / op2. Si op2 = 0, resultado es 0
        """
        resultado = 0
        if(self.op2 != 0):
            resultado = self.op1/self.op2
        return resultado

    def es_primo(self) :
        """
        Método para determinar si op1 es o no primo
        """
        primo = True
        for i in range (2,self.op1-1):
            if(self.op1%i==0):
                primo = False
        return primo