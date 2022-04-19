from kivy.app import App
from kivy.uix.widget import Widget

from modules.MapWidget.mapwidget import MapWidget

class RPGToolsApp(App):
    def build(self):
        root = MapWidget()
        return root

if (__name__ == "__main__"):
    RPGToolsApp().run()