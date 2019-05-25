"""
Aluno: VINICIUS DOTTO DE ARRUDA FIGUEIREDO
RGA:   201611310010
"""

#coding=UTF-8

from unicodedata import normalize

def remover_acentos(texto): #remove acentos
	return normalize('NFKD', texto).encode('ASCII', 'ignore').decode('ASCII')

def clearSpaces(texto): #tira caracteres e espaços indesejados
	texto = texto.replace(" ", "")
	texto = texto.replace("\n", "")
	texto = texto.replace(",", "")
	texto = texto.replace(".", "")
	texto = texto.replace("!", "")
	texto = texto.replace("?", "")
	return texto

def capsLock(texto): #deixa o texto todo em letras maiusculas
	texto = texto.upper()
	return texto

def addX(texto): #faz as correçoes
	i = 0	
	while i < (len(texto)):
		if (i+1) < len(texto):
			if texto[i] == texto[i+1]:
				texto = texto[:i] + texto[i] + 'X' + texto[i+1:]
		i = i+2
	if ((len(texto)) % 2) == 1:
		texto = texto + 'X'
	return texto

def arrumaChave(chave):
	for i in range (len(chave)):
		j = i+1
		while j < len(chave):
			if (chave[i]==chave[j]):
				if (j+1) < (len(chave)):
					chave = chave[:j] + chave[j+1:]
				else: 
					chave = chave[:j]
			j = j+1
	return chave


def criaMatriz (chave):
	alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXZ"
	for x in range (len(chave)):
		for y in range (len(alfabeto)-1):
			if (chave[x] == alfabeto[y]):
				if (y+1) < (len(alfabeto)):
					alfabeto = alfabeto[:y] + alfabeto[y+1:]
				else: 
					alfabeto = alfabeto[:y]
	mat = [[None for i in range(5)] for j in range(5)]
	k = 0
	a = 0
	for i in range (5):
		for j in range (5):
			if k < len(chave):
				mat[i][j] = chave[k]
				k= k+1
			else:
				mat[i][j] = alfabeto[a]
				a=a+1
	return mat

def encriPlayfair(mat, texto):
	k = 0
	cifrado = ""
	while k < (len(texto)):
		for i in range (5):
			for j in range (5):
				if (texto[k] == mat[i][j]):
					l1 = i
					c1 = j
				if (texto[k+1] == mat[i][j]):
					l2 = i
					c2 = j
		if (l1 == l2):
			if (c1 == 4):
				cifrado = cifrado + mat[l1][0]
			if (c1 < 4): 
				cifrado = cifrado + mat[l1][c1+1]
			if (c2 == 4):
				cifrado = cifrado + mat[l2][0]
			if (c2 < 4):
				cifrado = cifrado + mat[l2][c2+1]
		if (c1 == c2):
			if (l1 == 4):
				cifrado = cifrado + mat[0][c1]
			if (l1 < 4): 
				cifrado = cifrado + mat[l1+1][c1]
			if (l2 == 4):
				cifrado = cifrado + mat[0][c2]
			if (l2 < 4):
				cifrado = cifrado + mat[l2+1][c2]
		if (l1 != l2 and c1 != c2):
			cifrado = cifrado + mat[l1][c2] + mat[l2][c1]
		k = k+2
	return cifrado

def decriPlayfair(mat, texto):
	k = 0
	claro = ""
	while k < (len(texto)):
		for i in range (5):
			for j in range (5):
				if (texto[k] == mat[i][j]):
					l1 = i
					c1 = j
				if (texto[k+1] == mat[i][j]):
					l2 = i
					c2 = j
		if (l1 == l2):
			if (c1 == 0):
				claro = claro + mat[l1][4]
			if (c1 > 0): 
				claro = claro + mat[l1][c1-1]
			if (c2 == 0):
				claro = claro + mat[l2][4]
			if (c2 > 0):
				claro = claro + mat[l2][c2-1]
		if (c1 == c2):
			if (l1 == 0):
				claro = claro + mat[4][c1]
			if (l1 > 0): 
				claro = claro + mat[l1-1][c1]
			if (l2 == 0):
				claro = claro + mat[4][c2]
			if (l2 > 0):
				claro = claro + mat[l2-1][c2]
		if (l1 != l2 and c1 != c2):
			claro = claro + mat[l1][c2] + mat[l2][c1]
		k = k+2
	return claro


def main():
	chave = input("Insira uma chave:")
	pathe = input('Informe o caminho do arquivo de entrada: ')
	paths = input('Informe o caminho do arquivo de saida: ')
	modo = input('Digite c para criptografar ou d para descriptografar: ')
	chave = capsLock(chave)
	chave = clearSpaces(chave)
	chave = arrumaChave(chave)
	if (modo == "c" or modo == "C"):
		txt1 = open(pathe, 'r')	
		texto = txt1.read()
		txt1.close()
		texto = clearSpaces(texto)
		texto = remover_acentos(texto)
		texto = capsLock(texto)
		texto = addX(texto)
		mat = criaMatriz(chave)
		cifrado = encriPlayfair(mat, texto)
		txt2 = open(paths, 'w')
		txt2.write(cifrado)												
		txt2.close()
	if (modo == "d" or modo == "D"):
		txt1 = open(pathe, 'r')	
		texto = txt1.read()
		txt1.close()
		texto = clearSpaces(texto)
		mat = criaMatriz(chave)
		claro = decriPlayfair(mat, texto)
		txt2 = open(paths, 'w')
		txt2.write(claro)												
		txt2.close()
		if (modo != 'c' and modo != 'd'):
			print ("Modo Invalido!")
	#/home/vinicius/Documents/MEUS_CODIGOS/exemplo.txt
	#/home/vinicius/Documents/MEUS_CODIGOS/exemplo2.txt


main()