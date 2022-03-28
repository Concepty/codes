import socket

if 0:
	help(socket)

if 1:
	HOST = '127.0.0.1'
	PORT = 7777
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.bind((HOST, PORT))
		s.listen()
		conn, addr = s.accept()
		print('type of conn', type(conn))
		print('type of addr', type(addr))
		
