import socket, sys
from multiprocessing import Process

HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

def get_ip_address(host):
    try:
        ip = socket.gethostbyname(host)
    except socket.gaierror:
        sys.exit()

    return ip

def main():

    host = "www.google.com"
    port = 80

    #initialize socket connection
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as start:
        print("starting server")
        start.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        start.bind((HOST, PORT))
        start.listen(1)

        while True:

            connection, address = start.accept()
            print("connection : ",address)
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as end:
                ip = get_ip_address(host)

                end.connect((ip, port))
                p = Process(target = connect, args=(connection, end))

            connection.close()

def connect(connection, end):
    data = connection.recv(BUFFER_SIZE)
    end.sendall(data)
    end.shutdown(socket.SHUT_WR)

    send_data = end.recv(BUFFER_SIZE)
    connection.send(send_data)
    
if __name__ == "__main__":
    main()