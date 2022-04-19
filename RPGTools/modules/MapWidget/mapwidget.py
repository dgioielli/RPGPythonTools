from turtle import width
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window

class MapWidget(ScrollView):
    
    def __init__(self, **kwargs):
        super().__init__(size_hint=(1, None), size=(Window.width, Window.height), **kwargs)
        layout = GridLayout(cols=10, spacing=10, size_hint=(None, None))
        layout.bind(minimum_height=layout.setter("height"))
        for i in range(100):
            btn = Button(text=str(i), size_hint=(None, None), height=40, width=40)
            layout.add_widget(btn)
        self.add_widget(layout)
        