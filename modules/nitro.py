

def nitro():
    import os
    from os import remove
    import re
    import json
    import random
    import string
    import requests
    import webbrowser
    import time
    from time import sleep
    from requests import get 


    print("Recuerda borrar los codigos de  /Codes.txt/ despues de chekearlos (si los chekeaste ya claro esta, si no puedes dejarlos) ")
    sleep(2)
    print("""
    """)
    amount = int(input('Introduce la cantidad de codigos a generar: '))
    value = 1
    try:
        while value <= amount:
            code = "https://discord.gift/" + ('').join(random.choices(string.ascii_letters + string.digits, k=16))
            f = open('Codes.txt', "+a")
            f.write(f'{code}\n')
            f.close()
            print(f'[GENERADO] {code}')
            value += 1 
    except KeyboardInterrupt:
        print("Presionaste Ctrl + C")
        return
    
    sleep(2)
    print("Te gustaria chekear los codigos? ")
    sleep(2.5)
    eleccion = input("Si/No: ")
    try:
        if eleccion == "si" or "Si":
            with open("Codes.txt") as f:
                for line in f:
                    nitro = line.strip("\n")

                    url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

                    r = get(url)

                    if r.status_code == 200:
                        print(" Valido | {} ".format(line.strip("\n")))
                        f = open('Hits.txt', "+a")
                        f.write("{}\n".format(line.strip("\n")))
                        break
                    else:
                        print(" Invalido | {} ".format(line.strip("\n")))
                        f = open('Bad.txt', "+a")
                        f.write("{}\n".format(line.strip("\n")))
                        
        else:
            print("Okey")
    except KeyboardInterrupt:
        print("Presionaste Ctrl + C")
        exit()