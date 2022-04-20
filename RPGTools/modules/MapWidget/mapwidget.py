from ctypes import sizeof
from turtle import width
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window

from .squaremapwidget import SquareMapWidget

class MapWidget(ScrollView):
    
    def __init__(self, **kwargs):
        super().__init__(size_hint=(1, 1), **kwargs)
        map = SquareMapWidget(cols=12, rows=12)
        
        for i in range(144):
            btn = Button(text=str(i), size_hint=(None, None), height=80, width=80)
            map.add_widget(btn)
        self.add_widget(map)
        