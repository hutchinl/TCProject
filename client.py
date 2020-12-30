import socket 
import threading 


nickname = input("Username: ")


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 65535))

def receive():
    while True: 
        try: 
            message = client.recv(1024).decode('ascii')
            if message == 'NICKNAME':
                client.send(nickname.encode('ascii'))
            else:
                print(message)

        except: 
            print('An error occurred')
            client.close()


def write():
    while True: 
        
        message = f'{nickname}: {input("")}'

        client.send(message.encode('ascii'))

receive_thread = threading.Thread(target = receive)
receive_thread.start()

write_thread = threading.Thread(target = write)
write_thread.start()

