#server
import socket
import threading

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f"Client: {message}")
                response = input("You: ")
                client_socket.send(response.encode('utf-8'))
            else:
                break
        except ConnectionResetError:
            break
    
    client_socket.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 9999))
    server.listen(1)
    print("Server listening on port 9999...")

    client_socket, addr = server.accept()
    print(f"Accepted connection from {addr}")

    client_handler = threading.Thread(target=handle_client, args=(client_socket,))
    client_handler.start()

if __name__ == "__main__":
    main()
