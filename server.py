import socket

s=socket.socket()
host=socket.gethostname()
port=12345
s.bind((host,port))

s.listen(5)
while True:
    c,addr=s.accept()
    print('Connection Received Form : {}'.format(addr))
    c.send('Thanks for connecting'.encode("utf-16"))
    c.close()
