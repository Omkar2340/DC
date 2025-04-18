import socket

# Create client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 12345

client_socket.connect((host, port))

# Input operation and numbers
operation = input("Enter operation (add/sub/mul/div): ")
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

# Create message to send
message = f"{operation} {num1} {num2}"
client_socket.send(message.encode())

# Receive and print result
result = client_socket.recv(1024).decode()
print(f"Result from server: {result}")

client_socket.close()
