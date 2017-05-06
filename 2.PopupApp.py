#qpy:kivy

from kivy.app import App #here we are import app from kivy.app
from kivy.uix.boxlayout import BoxLayout #here we are importing boxlayout
from kivy.lang import Builder #here we are importing builder 
from kivy.uix.button import Button #here we are importing button from kivy UI
from kivy.uix.popup import Popup #popup imported from UI
from kivy.uix.label import Label #label imported from UI
from kivy.uix.progressbar import ProgressBar #progressbar imported


import time #Imported TIME to show time in progressbar
import threading #threading so more then 1 thing can run together.



Builder.load_string('''
<Myinterface>:
    orientation: 'vertical'

    Label:
        text: "Hi There"
        
    BoxLayout:
        orientation: 'vertical'   
        TextInput:
            id: variable
            hint_text: "Enter your username"
        MyButton:
            user_input: variable.text
            text: "Attack"
            on_release: self.do_action()

''')


class MyInterface(BoxLayout):
    pass

class MyButton(Button):

    def progbar(self):
        pb = ProgressBar()
        popup = Popup(title='Brute Forcing ...', content=pb, size_hint=(0.7, 0.3))
        popup.open()
        time.sleep(2)
        pb.value = 25
        time.sleep(4)
        pb.value = 50
        time.sleep(6)
        pb.value = 75
        time.sleep(8)
        pb.value = 100 #value becomes 100 of progressbar.

    def do_action(self, *args):
        threading.Thread(target=self.progbar).start()
        print 'We are here'
        return



    

class MyApp(App):
    def build(self):
        return MyInterface()



MyApp().run() #runs or starts our app.
#please subscribe www.youtube.com/priyankgada
