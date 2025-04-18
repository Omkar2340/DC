import socket

# Create server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 12345
server_socket.bind((host, port))
server_socket.listen(1)

print(f"Server listening on {host}:{port}...")

client_socket, addr = server_socket.accept()
print(f"Connected to {addr}")

# Receive the request from client
data = client_socket.recv(1024).decode()
print(f"Received: {data}")

# Parse the request (e.g., "add 10 5")
parts = data.split()
operation = parts[0]
num1 = float(parts[1])
num2 = float(parts[2])

# Perform operation
result = "Invalid operation"
if operation == 'add':
    result = num1 + num2
elif operation == 'sub':
    result = num1 - num2
elif operation == 'mul':
    result = num1 * num2
elif operation == 'div':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero"

# Send result back
client_socket.send(str(result).encode())

# Close sockets
client_socket.close()
server_socket.close()
