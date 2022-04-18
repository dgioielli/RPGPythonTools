from cgitb import text
from pickle import FALSE
import kivy
kivy.require("2.1.0")

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

class LoginScreen(GridLayout):
    def __init__(self, **kwargs) -> None:
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text="User name"))
        self.userName = TextInput(multiline=False)
        self.add_widget(self.userName)
        self.add_widget(Label(text="Password"))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)

class MyApp(App):
    def build(self):
        return LoginScreen()

if (__name__ == "__main__"):
    MyApp().run()