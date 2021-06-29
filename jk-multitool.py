import os
import re
import json
import random
import string
from time import sleep
from urllib.request import Request, urlopen
import subprocess, colorama, requests, base64, os
from colorama import Fore, Style, init
import modules.anydeskresolver
import modules.nitro
from flask import Flask
from flask_restful import Resource, Api
from modules.nitro import nitro
from modules.tcpportscan import tcpportscan 
from modules.udpportscan import udpportscan
from modules.discord_bruteforce import main
from modules.twitch_token_gen import twitch_gen
from modules.discord_token_gen import main2
init()


def espera():
  sleep(1)
  print(".")
  sleep(1)
  print("·")
  sleep(1)

print(Fore.RED + """
       _             _           __  __       _ _   _ _              _ 
      | |           | |         |  \/  |     | | | (_) |            | |
      | | __ _ _ __ | | ________| \  / |_   _| | |_ _| |_ ___   ___ | |
  _   | |/ _` | '_ \| |/ /______| |\/| | | | | | __| | __/ _ \ / _ \| |
 | |__| | (_| | | | |   <       | |  | | |_| | | |_| | || (_) | (_) | |
  \____/ \__,_|_| |_|_|\_\      |_|  |_|\__,_|_|\__|_|\__\___/ \___/|_|
""" )                                                                                                                            

sleep(1)
print(Fore.RED + "1: Nitro Generator ")
sleep(1.5)
print(Fore.RED + "2: AnyDeskIPResolver ")
sleep(1)
print(Fore.RED + "3: Scan de Puertos TCP ")
sleep(1)
print(Fore.RED + "4: Scan de Puertos UDP ")
sleep(1)
print(Fore.RED + "5: Discord Token Bruteforcer ")
sleep(1)
print(Fore.RED + "6: Twitch Token Generator ")
sleep(1)
print(Fore.RED + "7: Discord Token Generator ")
sleep(1)
print(Fore.RED + """                                                                                                                                            """)

sleep(2.5)
eleccion = int(input("Introduce tu eleccion: "))
if eleccion == 1:
  espera()
  print("Elegiste el generador de nitro")
  espera()
  nitro()
elif eleccion == 2:
  espera()
  print("Elegiste el AnyDeskIPResolver")
  espera()
  anydeskresolver()
elif eleccion == 3:
  espera()
  print("Selecionaste el Scan de puertos TCP")
  espera()
  tcpportscan()
elif eleccion == 4:
  espera()
  print("Selecionaste el Scan de puertos UDP")
  espera()
  udpportscan()
elif eleccion == 5:
  espera()
  print("Selecionaste el Bruteforcer de Token de Discord")
  espera()
  main()
elif eleccion == 6:
  espera()
  print("Selecionaste el Generador de Tokens de Twitch")
  espera()
  twitch_gen()
elif eleccion == 7:
  espera()
  print("Selecionaste el Generador de Tokens de Discord")
  espera()
  main2()
else:
  print("Subnormal escoge una opcion valida")

