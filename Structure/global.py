a= 5
def muda_e_imprime():
	global a
	a = 7
	print('dentro da função', a)
print('antes da mudança', a)
muda_e_imprime()
print('final', a)