import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
kivy.require('2.1.0')

class Prin(BoxLayout):
    Builder.load_string('.kv')

    def __init__(self, **kwargs):
        super(Prin, self).__init__(**kwargs)

    def start(self):
        self.ids.label.text += "\nNew line"


class MainApp(App):
    def build(self):
        return Prin()


if __name__ == "__main__":
    app = MainApp()
    app.run()