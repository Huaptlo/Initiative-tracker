import kivy
kivy.require('2.1.0')

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label

InitiativeList = ['First', 'Second', 'Third', 'Fourth', 'Fifth']

class InitiativeApp(App):
    def build(self):
        layout = FloatLayout()

        # Create and add the display field label
        display_label = Label(text=InitiativeList[0], font_size='30sp',
                              pos_hint={'x': 0.25, 'y': 0.5})
        layout.add_widget(display_label)

        return layout

if __name__ == '__main__':
    InitiativeApp().run()
