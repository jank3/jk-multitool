def udpportscan():
    import socket, threading


    def UDP_connect(ip, port_number, delay, output):
        UDPsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        UDPsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        UDPsock.settimeout(delay)
        try:
            UDPsock.connect((ip, port_number))
            output[port_number] = 'Abierto'
        except:
            output[port_number] = ''



    def scan_ports(host_ip, delay):

        threads = []        # To run UDP_connect concurrently
        output = {}         # For printing purposes

    # Spawning threads to scan ports
        for i in range(65536):
            t = threading.Thread(target=UDP_connect, args=(host_ip, i, delay, output))
            threads.append(t)

    # Starting threads
        for i in range(65536):
            threads[i].start()

    # Locking the main thread until all threads complete
        for i in range(65536):
            threads[i].join()

    # Printing listening ports from small to large
        for i in range(65536):
            if output[i] == 'Abierto':
                print(str(i) + ': ' + output[i])



    def main():
        host_ip = input("IP de la victima: ")
        delay = int(input("¿Cuantos segundos de espera va a tener el socket antes de finalizar?: "))   
        scan_ports(host_ip, delay)
    main()