# -*- coding: UTF-8 -*-

####################################
# Algoritmo Insertion Sort
# 
# Algoritmo utilizado para fazer ordenação de array, semelhante a ordenação
# feita por nós ao ordenar as cartas de um baralho a mão.
#
# Referência: Algoritmos (Teoria e Prática) pág 11
#
# @author dobau
# since 25/05/2010
####################################

# Sem utilizar os recursos da linguagem
# Meu algoritmo
def sort1(datas):
	for i in range(len(datas)):
		for j in range(i + 1, len(datas)):
			if (datas[i] > datas[j]):		
				aux = datas[j]
				m = j
				while (m > i):
					datas[m] = datas[m-1]
					m = m - 1
				datas[i] = aux;

# Algoritmo do livro
def sort2(datas):
	for j in range(1, len(datas)):
		chave = datas[j]
		i = j - 1
		while (i >= 0 and datas[i] > chave):
			datas[i + 1] = datas[i]
			i = i - 1
		datas[i + 1] = chave

# Testando...
teste = [5, 2, 4, 6, 1, 3]
sort2(teste)
for i in range(len(teste)):
	print teste[i] 
