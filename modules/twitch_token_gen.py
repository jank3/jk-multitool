def twitch_gen():
    try:
        import requests
        import random 
        import string
        import re
        import json
        import webbrowser
        from time import sleep


        
        print("1-Generar Codigos Random hasta encontrar uno valido")
        print("2-Generar una cantidad de codigos determinada (la eliges tu)")
        
        sleep(2)
        elc = int(input("¿Que deseas hacer? 1/2 :  "))
        
        if elc == 1:
            while True:
                token = "" + ('').join(random.choices(string.ascii_lowercase + string.digits, k=30))
                url = "https://id.twitch.tv/oauth2/validate" + token 
                r = requests.get(url)
                if r.status_code == 200:
                    print(" Valido |" + token)
                    f = open('token_twitch_valido.txt', "+a")
                    f.write(f'{token}\n')
                    f.close()
                    #break                                                                          --Activalo si quieres que cuando encuentre uno valido se pare
                else:
                    print(" Invalido | " + token)
                    f = open('token_twitch_invalido.txt', "+a")
                    f.write(f'{token}\n')
                    f.close()
        elif elc == 2:
            numero_de_veces = int(input("Cuantos codigos quieres generar: "))

            for i in range(numero_de_veces):
                token = "" + ('').join(random.choices(string.ascii_lowercase + string.digits, k=30))
                url = "https://id.twitch.tv/oauth2/validate" + token 
                r = requests.get(url)
                if r.status_code == 200:
                    print(" Valido |" + token)
                    f = open('token_twitch_valido.txt', "+a")
                    f.write(f'{token}\n')
                    f.close()
                    #break                                                                          --Activalo si quieres que cuando encuentre uno valido se pare
                else:
                    print(" Invalido | " + token)
                    f = open('token_twitch_invalido.txt', "+a")
                    f.write(f'{token}\n')
                    f.close()
    except KeyboardInterrupt:
        print("Presionaste Ctrl + C")

