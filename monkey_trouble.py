def monkey_trouble(a_smile, b_smile):
	if a_smile == b_smile:
		return True
	else:
		return False
#solucion alternativa
def monkey_trouble(a_smile, b_smile):
	if a_smile and b_smile:
		return True
	elif a_smile==False and b_smile == False:
		return True
	else:
		return False
