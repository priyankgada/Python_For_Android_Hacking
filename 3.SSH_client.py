import paramiko #importing paramiko library - Please install paramiko first.


def connect():


#SSHClient() class takes care of most aspects of authenticating and opening channels.
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#class automatically adds the hostname and server host key to the local ‘HostKeys‘ object and
#saves it, so we won’t worry about the notification message about recognizing the server key
#fingerprint that appears when you first connect to an SSH server.

   
    client.connect('192.168.1.22', username='Priyank', password='123') #change username , password and IP of the machine.
    chan = client.get_transport().open_session()

#client.get_transport().open_session()‘ requests a new channel of type ‘session‘ from
#the server (still remember ‘def check_channel_request’ from the server code?)

#we send a string saying to the server that we are connected and print the result back from the server
    chan.send('Hey i am connected :) ')
    print chan.recv(1024)

connect()
