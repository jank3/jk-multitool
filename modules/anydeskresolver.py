def anydeskresolver():
	import subprocess, colorama, requests, base64, os

	os.system('@title Dead$quad | Anydesk IP Resolver && cls')

	from colorama import Fore, Style

	colorama.init()

	anydesk_pids = []
	anydesk_address = {}
	ip_addr = []
	old_port = 0
	old_ip = ''

	print("")
	print("Esperando conexión...", end='')

	while 1:
		try:
			if str(subprocess.check_output("tasklist")).count('AnyDesk') <= 3:
				pass
			else:
				for line in str(subprocess.check_output("tasklist")).replace('b"', '"').replace('\\r', '').replace('\\n', '\n').split('\n'):
					if 'AnyDesk' in line:
						try:
							anydesk_pids.append(line.split('.exe')[1].split()[0].replace(' ', ''))
						
						except Exception as e:
							pass
				nstats_output_lines = str(subprocess.check_output('netstat -p TCP -n -a -o')).replace('b"', '"').replace('\\r', '').replace('\\n', '\n').split('\n')
				for pid in anydesk_pids:
					for line in nstats_output_lines:
						if pid in line and not 'LISTENING' in line:
							try:
								parts = line.split()
								protocol = parts[0]
								local_addr = parts[1]
								remote_addr = parts[2].split(':')[0]
								remote_port = parts[2].split(':')[1]
								anydesk_address[remote_addr] = int(remote_port)
							except Exception as e:
								print(e)
				for ip, port in anydesk_address.items():
					if int(port) > old_port and not '169.254.' in ip:
						old_port = int(port)
						old_ip = ip
				remote_ip = old_ip
				remote_port = old_port
				print(f'{Fore.RED} Conexión Establecida')
				try:
					json_data = requests.get(f'http://extreme-ip-lookup.com/json/' + remote_ip).json()
					print(Style.BRIGHT + '''
	{13}IP{14}:{13} {0}{6}
	{13}País{14}:{13} {1}{7}
	{13}Ciudad{14}:{13} {2}{8}
	{13}Proveedor{14}:{13} {3}{9}
	{13}Latitud{14}:{13} {4}{10}
	{13}Longitud{14}:{13} {5}{11}

					'''.format(json_data['query'], json_data['country'], json_data['city'], json_data['isp'], json_data['lat'], json_data['lon'], (' ' * (38 - int(len(json_data['query'])))), (' ' * (33 - int(len(json_data['country'])))), (' ' * (36 - int(len(json_data['city'])))), (' ' * (37 - int(len(json_data['isp'])))), (' ' * (37 - int(len(json_data['lat'])))), (' ' * (37 - int(len(json_data['lon'])))),Fore.RED, Fore.WHITE, Fore.BLACK))
				except:
					print('Hmmm.')
				input('Presiona Enter Para Continuar')
				exit()
		except KeyboardInterrupt:
			print('ctrl+c'); exit()
	return	
