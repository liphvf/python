class testando:
    x = 10
    def __init__(self):
        #Caso declare uma variavel no construtor é preciso colocar o self
        self.t = "aew"

#Obrigatoriamente tem que colocar o self para dizer que é uma metodo dessa classe
    def soma(self):
        print("hahaha")

class outra:

    #isso é criando um objeto testando()
    a = testando()
    print(a.x)

    a.soma()

