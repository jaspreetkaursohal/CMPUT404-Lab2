import socket
from multiprocessing import Process

#define address & buffer size
HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
        #QUESTION 3
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        #bind socket to address
        s.bind((HOST, PORT))
        #set to listening mode
        s.listen(2)
        
        #continuously listen for connections
        while True:
            conn, addr = s.accept()
            p = Process(target = connect, args=(addr,conn))
            p.daemon = True
            p.start()
            print("Started process -", p)

def connect(address, connection):

    print("Connected by", address)
    full_data = connection.recv(BUFFER_SIZE)
    connection.sendall(full_data)
    connection.shutdown(socket.SHUT_RDWR)
    connection.close()

if __name__ == "__main__":
    main()
