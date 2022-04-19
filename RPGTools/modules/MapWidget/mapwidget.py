from ctypes import sizeof
from turtle import width
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window

class MapWidget(ScrollView):
    
    def __init__(self, **kwargs):
        super().__init__(size_hint=(1, 1), **kwargs)
        layout = GridLayout(cols=12, spacing=10, size_hint=(None, None), padding=[20, 20, 20, 20])
        layout.bind(minimum_height=layout.setter("height"))
        layout.bind(minimum_width=layout.setter("width"))
        for i in range(144):
            btn = Button(text=str(i), size_hint=(None, None), height=80, width=80)
            layout.add_widget(btn)
        self.add_widget(layout)
        