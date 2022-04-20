from kivy.uix.gridlayout import GridLayout
from kivy.properties import NumericProperty

class SquareMapWidget(GridLayout):
    
    NumColumns = NumericProperty(1)
    NumRows = NumericProperty(1)
    
    def __init__(self,cols=1, rows=1, **kwargs):
        super().__init__(cols=cols, rows = rows, size_hint=(None, None), padding=[20, 20, 20, 20], **kwargs)
        self.NumColumns = cols
        self.NumRows = rows
        self.bind(minimum_height=self.setter("height"))
        self.bind(minimum_width=self.setter("width"))