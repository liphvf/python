#Uma ótimo ultilidade do for pode ser a estrutura for else

#Na estrutura normal ele repetirar essa menssagem 10 vezes
paes = [1,2,3,4,5]
comer = 0
for x in paes:
	print("Come +1 Pão")
	comer+=1
else:
	print("Ainda to com fome")

#Já com else funciona um pouco diferente, quando ele vê o break, ele ÑÃÕ IMPRIME O ELSE. 
#Em cima temos um esfomiado que meso comendo 5 paes não está satisfeito
#Abaixo tenho um que se comer 3 paes se sente bem
#Resumindo, se tiver um break, ele não executa o else. 

print("\n"+"\n")
paes = [1,2,3,4,5,6,7,8,9,10]
comer = 0
for x in paes:
	if comer == 3:
		print("Ufa, Comi D+!!, Vou parar")
		break
	else:
		print("Come +1 Pão")
	comer+=1
else:
	print("Terminei de jantar")


#próxim for é com idx, x in enumerate(algumacoisa)