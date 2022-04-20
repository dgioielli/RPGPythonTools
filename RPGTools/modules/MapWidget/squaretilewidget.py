from kivy.uix.widget import Widget
from kivy.properties import NumericProperty

class SquareTileWidget(Widget):
    NumSquare = NumericProperty(0)
    
    def __init__(self, num, height=50, width=50, **kwargs):
        super().__init__(height=height, width=width, **kwargs)
        self.NumSquare = num