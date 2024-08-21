from socket  import *
from constCS import * #-

s = socket(AF_INET, SOCK_STREAM) 
s.bind((HOST, PORT))  #-
s.listen(1)           #-
print("Aguardando o recebimento de mensagens...", flush=True)
(conn, addr) = s.accept()  # returns new socket and addr. client 
while True:                # forever
  data = conn.recv(1024)   # receive data from client
  if not data: break       # stop if client stopped
  msg = data.decode()+"*"  # process the incoming data into a response
  print("Mensagem recebida:", data.decode())
  conn.send(msg.encode())  # return the response
  print("Mensagem enviada", msg)
conn.close()               # close the connection
