import socket

HOST = "127.0.0.1" 
PORT = 7777

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.connect((HOST, PORT))
	while True:
		msg = input()
		s.sendall(msg.encode('utf-8'))
		data = s.recv(1024)
		if data == b'': break
		print('echoed:', data.decode('utf-8'))
		
