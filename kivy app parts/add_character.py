import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
kivy.require('2.1.0')


class InitiativeTracker(FloatLayout):
    initiative_list = []

    def open_popup(self, instance):
        content = FloatLayout()
        name_input = TextInput(text='Name', size_hint=(0.8, 0.2), pos_hint={'x': 0.1, 'y': 0.6})
        value_input = TextInput(text='Value', size_hint=(0.8, 0.2), pos_hint={'x': 0.1, 'y': 0.3})
        close_button = Button(text='Close', size_hint=(0.2, 0.2), pos_hint={'x': 0.8, 'y': 0.8})
        close_button.bind(on_press=self.close_popup)
        add_button = Button(text='Add', size_hint=(0.2, 0.2), pos_hint={'x': 0.8, 'y': 0.5})
        add_button.bind(on_press=lambda x: self.add_to_list(name_input.text, value_input.text))
        content.add_widget(name_input)
        content.add_widget(value_input)
        content.add_widget(close_button)
        content.add_widget(add_button)
        self.popup = Popup(title='Add Initiative', content=content, size_hint=(0.6, 0.6), auto_dismiss=False)
        self.popup.open()

    def close_popup(self, instance):
        self.popup.dismiss()

    def add_to_list(self, name, value):
        self.initiative_list.append({'name': name, 'value': value})
        self.popup.dismiss()

    def print_initiative_list(self, instance):
        for entry in self.initiative_list:
            print(f"{entry['name']}: {entry['value']}")

    def build(self):
        add_button = Button(text='Add Initiative', size_hint=(0.2, 0.1), pos_hint={'x': 0.4, 'y': 0.45})
        add_button.bind(on_press=self.open_popup)
        print_button = Button(text='Print Initiative List', size_hint=(0.2, 0.1), pos_hint={'x': 0.4, 'y': 0.35})
        print_button.bind(on_press=self.print_initiative_list)
        self.add_widget(add_button)
        self.add_widget(print_button)


class InitiativeTrackerApp(App):
    def build(self):
        return InitiativeTracker()


if __name__ == '__main__':
    InitiativeTrackerApp().run()
