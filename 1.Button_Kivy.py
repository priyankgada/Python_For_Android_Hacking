#qpy:kivy

#Qpython now knows that this is a kivy app.


from kivy.app import App #here we are importing app from kivy.app

from kivy.uix.button import Button #here we are importing button from kivy UI 


class TestApp(App): #  Base Class of our Kivy App
    def build(self):  # To start our app
        return Button(text='Hello World') # Here we are creating button
                                          # text = means the text on button

TestApp().run() # This will start the app.

#Please subsrcribe - www.youtube.com/priyankgada.com
