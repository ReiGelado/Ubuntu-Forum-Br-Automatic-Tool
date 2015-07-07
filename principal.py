#!-*- conding: utf8 -*-
import urllib2
import urllib
import threading
import cookielib
import re

print '[+]v0.1\n'
print '[+]PoG is Life...\n'
print '[+]By Rei_Gelado...\n'

def acessa_retorna(login,senha):
	cabecalho_http = {
				"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.46 Safari/535.11",
				"Accept" : "text/xml,application/xml,application/xhtml+xml,text/html;q=0.9,text/plain;q=0.8,text/png,*/*;q=0.5",
				"Accept-Language" : "en-us,en;q=0.5",
				"Accept-Charset" : "UTF-8",
				"Content-type": "application/x-www-form-urlencoded",
				"Host" : "ubuntuforum-br.org",
				"Referer" : "http://google.com/"
				}
	valores_post = {'user' : login , 'passwrd' : senha , 'cookielength' : '-1' , 'hash_passwrd' : ''}

	cookie = urllib2.HTTPCookieProcessor(cookielib.CookieJar())

	opener = urllib2.build_opener(cookie)

	req = urllib2.Request('http://ubuntuforum-br.org/index.php?action=login2', urllib.urlencode(valores_post), cabecalho_http)

	res = opener.open(req)

	verifica = re.compile('unreadreplies">(.*?)respostas aos meus T')
	verifica_findall = re.findall(verifica,res.read())

	if verifica_findall[0] == 'Ver novas ':
		print '[+]Logado com sucesso!\n'
	else:
		print '[+]Password ou Senha Incorretos!\n[+]Tente novamente!\n'
		from sys import exit
		exit()

	cabecalho_http = {
				"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.46 Safari/535.11",
				"Accept" : "text/xml,application/xml,application/xhtml+xml,text/html;q=0.9,text/plain;q=0.8,text/png,*/*;q=0.5",
				"Accept-Language" : "en-us,en;q=0.5",
				"Accept-Charset" : "UTF-8",
				"Content-type": "application/x-www-form-urlencoded",
				"Host" : "ubuntuforum-br.org",
				"Referer" : "http://ubuntuforum-br.org/index.php"
				}

	valores_post = {}

	req = urllib2.Request('http://ubuntuforum-br.org/index.php?action=unreadreplies',urllib.urlencode(valores_post),cabecalho_http)

	res = opener.open(req)

	#A pog e algo que nao se pode explicar....
	verifica2 = re.compile('\\?action=unread;all;start=0">Clique aqui(.*?)todos os ')
	verifica2_findall = re.findall(verifica2,res.read())		

	if verifica2_findall[0] == ' para ver ':
		print '[+]Nao ha topicos seus respondidos....\n'
	else:
		print '[+]Existem topicos!'

	req = urllib2.Request('http://ubuntuforum-br.org/index.php?action=unread',urllib.urlencode(valores_post),cabecalho_http)
	
	res = opener.open(req)
	#Pog voce aqui de novo?rsrs
	verifica3 =  re.compile('\\?action=unread;all;start=0">Clique aqui(.*?)todos os ')
	verifica3_findall = re.findall(verifica3,res.read())

	if verifica3_findall[0] == 	' para ver ':
		print '[+]Nao ha topicos nao lidos desde a sua ultima visita....\n'
	else:
		print '[+]Existem topicos!'

login = raw_input('[+]Qual seu Login no forum :\n\nR:')
senha = raw_input('[+]Qual sua Senha no forum :\n\nR:')

try:
	print '[+]Iniciando a Thread.....\n'
	thread = threading.Thread(target=acessa_retorna, args=(login,senha))
	thread.start()
	thread.join()
except:
	print '[+]Ocorreu um erro ao iniciar a Thread...\n'
