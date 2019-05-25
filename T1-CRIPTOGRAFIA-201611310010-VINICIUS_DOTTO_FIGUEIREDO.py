"""
Aluno: VINICIUS DOTTO DE ARRUDA FIGUEIREDO
RGA:   201611310010
"""

#coding=UTF-8

def chaveInvalida(chave):	#Funçao logica para vaalidaçao de chave
	if (len(chave) != 8 and len(chave) != 16):
		print ("Chave invalida, por favor insira APENAS 8 ou 16 caracteres")
		return 0
	else: 
		return 1

def stringPbin (text):	#Transforma o texto em binario
	textoBin = ""
	tam = len(text)
	for i in range (tam):
		textoBin = textoBin + str(bin(ord(text[i]))[2:].zfill(8))
	return textoBin

def completaZero(text, key):	#Completa o ultimo conjunto com zeros se necessario
	if (len(text) % len(key) != 0):
		if(len(text) < len(key)):
			y = (len(key)) - (len(text))
		else:
			y = (len(text) % len(key))
		for x in range (y):
			text = text + "0"		
	return text

	
def xor (text, key):	#realiza a operaçao de exclusivo ou
	text = completaZero(text, key)
	tamChave = len(key)
	textoC = ""	
	k = int(len(text)/tamChave)
	for p in range (k):
		for j in range (tamChave):
			result = int(text[j+(tamChave*p)]) ^ int(key[j])
			textoC = textoC + str(result)	
	return textoC

def binPstr(text):	#realiza a conversao de binario para uma string
	text  = ''.join(str(e) for e in text)
	string_blocks = (text[i:i+8] for i in range(0, len(text), 8))
	texto = ''.join(chr(int(char, 2)) for char in string_blocks)
	return texto



if __name__ == '__main__':

	chave = input("Insira uma chave alfanumerica de 8 ou 16 caracteres:")
	path = input('Informe o caminho do arquivo: ')
	modo = input('Digite c para criptografar ou d para descriptografar: ')
	if (chaveInvalida(chave)):
		arq = open(path, 'r')	
		texto = arq.read()
		if (modo == "c" or modo == "C"):
			retorno = xor(stringPbin(texto), stringPbin(chave))
			print (retorno)
			arquivo = open(path, 'w')
			arquivo.write(retorno)												
			arq.close()
		if (modo == "d" or modo == "D"):
			texto = xor(texto, stringPbin(chave))
			texto = binPstr(texto)
			print (texto)
			arquivo = open(path, 'w')
			arquivo.write(texto)												
			arq.close()
		if (modo != c and modo != d):
			print ("Modo Invalido!")

	#/home/vinicius/Documents/MEUS_CODIGOS/exemplo.txt






