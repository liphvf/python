
#Há 4 modos de criar strings

variavel1 =  'Alpha'
variavel2 =  "Bravo"
variavel3 = '''Delta '''
variavel4 = str(3)

print(variavel1, variavel2,variavel3,variavel4)



#len(): Consegui o tamanho da string(ou list ou coleção)

len("Charlie")

print('Tamanho da palavra Charlie é',len("Charlie"))

#upper(): Coloca toda a string em maiúscula
'delta'.upper()
print('delta upper é assim: ', 'delta'.upper())

#lower(): coloca toda a string em minúscula
'ECHO'.lower()
print('palavra ECHO minúscula é: ','ECHO'.lower())

#strip(): tira os espaços em branco do final
var = 'vem             '.strip()
print('Dividindo por string vazia:', var)

# "banana, morango, manga".split(",")
# #returna uma lista separando por virgula L=[banana,morango,manga]



# #Exibição de uma string:
# print "Foxtrot"

# #LEMBRANDO, posso escrever assim(ele não esta concatenando, esta exebindo junto):
# print("alguma coisa", string_1, "outra coisa")


# #Técnicas avançadas de exibição
# string_1 = "Camelot"
# string_2 = "lugar"

# print ("Nao vamos para %s. E um %s bobo." % (string_1, string_2))

# #Lembre do % que fica após fechar string.


# #ponto flutuante
# a = 3.1415

# print("com 2 casas decimais %.2f" %(a))
