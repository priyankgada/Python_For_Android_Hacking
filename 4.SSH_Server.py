import socket #importing socket library 
import paramiko #importing paramiko . Please get paramiko library first
import threading #threading for running 2 tasks together
import sys #system

host_key = paramiko.RSAKey(filename='/root/Desktop/test_rsa.key') #location of the host key .


class Server (paramiko.ServerInterface):
    def __init__(self):
        self.event = threading.Event()
    def check_channel_request(self, kind, chanid):
        if kind == 'session':
            return paramiko.OPEN_SUCCEEDED
        return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED
    def check_auth_password(self, username, password):
        if (username == 'Priyank') and (password == '123'):
            return paramiko.AUTH_SUCCESSFUL #provide username and password.
        return paramiko.AUTH_FAILED



try:
    global sock
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('192.168.1.22', 22))
    sock.listen(1)
    print '[+] Listening for connection ...'
except Exception, e:
    print '[-] Listen/bind failed: ' + str(e)



  
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
    pass #if error occurs , connection terminated will be printed and pass.        
        
        




