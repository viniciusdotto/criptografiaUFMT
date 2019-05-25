"""
Aluno: VINICIUS DOTTO DE ARRUDA FIGUEIREDO
RGA:   201611310010
"""

#coding=UTF-8

def stringPbin (text):	#Transforma o texto em binario
	textoBin = ""
	tam = len(text)
	for i in range (tam):
		textoBin = textoBin + str(bin(ord(text[i]))[2:].zfill(8))
	return textoBin

def completaZero(text):	#Completa o ultimo conjunto com zeros se necessario
	while (len(text)%64 != 0):
		text = text +'1'		
	return text

def xor (text1, text2):	#realiza a operaçao de exclusivo ou
	textoC = ""	
	for i in range (len(text1)):
		textoC = textoC + str(int(text1[i]) ^ int(text2[i]))
	return textoC

def rotacao(texto, index): #executa as rotaçoes conforme solicitado
	cont = 0
	while cont < index:
		texto = texto[1:] + texto[0]
		cont = cont + 1
	return texto


def main():
	path = input('Informe o caminho do arquivo: ')
	arq = open(path, 'r')	
	texto = arq.read()
	cifrado = texto[:8]
	cifrado = stringPbin(cifrado)
	cifrado = rotacao(cifrado,1)
	count=1
	while count < (len(texto) / 8):
		part = texto[((count*8)):(2*count*8)]
		part = stringPbin(part)
		part = completaZero(part)
		part = rotacao(part,count+1) 
		cifrado = xor(cifrado, part)
		count=count+1
	cifrado = int(cifrado, 2)
	cifrado = str(hex(cifrado))
	cifrado = cifrado[2:]
	print (cifrado)
main()
