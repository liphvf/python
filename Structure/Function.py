#voltar ao 91 para esutdar lista

#metodo de soma
##def soma ():
    ##a = int(input("Dgiite a: "))
    ##b = int(input("Dgiite b: "))
    ##print("a soma é: ", a+b)

##soma()



#Vamos retornar o valor agora

def soma(a,b):
    return(a+b)

print(soma(10,3))


def par(x):
    return(x % 2 == 0)
    
print(par(1))


def par_ou_impar(x):
    if par(x):
        print("É par")
    else:
        print("É impar")

par_ou_impar(10)