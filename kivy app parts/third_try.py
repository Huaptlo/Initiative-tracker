import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
kivy.require('2.1.0')

class MyFloatLayout(FloatLayout):
    def __init__(self, **kwargs):
        super(MyFloatLayout, self).__init__(**kwargs)
        self.names = []
        self.values = []
        self.current_index = 0

        # Create input fields
        self.name_input = TextInput(hint_text='Name', size_hint=(0.4, 0.1), pos_hint={'x': 0.1, 'y': 0.85})
        self.add_widget(self.name_input)
        self.value_input = TextInput(hint_text='Value', size_hint=(0.2, 0.1), pos_hint={'x': 0.6, 'y': 0.85})
        self.add_widget(self.value_input)

        # Create add button
        self.add_button = Button(text='Add', size_hint=(0.2, 0.1), pos_hint={'x': 0.4, 'y': 0.8})
        self.add_button.bind(on_press=self.add_item)
        self.add_widget(self.add_button)

        # Create clear button
        self.clear_button = Button(text='Clear', size_hint=(0.2, 0.1), pos_hint={'x': 0.4, 'y': 0.1})
        self.clear_button.bind(on_press=self.clear_list)
        self.add_widget(self.clear_button)

        # Create cycle button
        self.cycle_button = Button(text='Cycle', size_hint=(0.2, 0.1), pos_hint={'x': 0.4, 'y': 0.4})
        self.cycle_button.bind(on_press=self.cycle_list)
        self.add_widget(self.cycle_button)

        # Create label to display sorted list
        self.list_label = Label(text='', size_hint=(0.6, 0.6), pos_hint={'x': 0.2, 'y': 0.2})
        self.add_widget(self.list_label)

        # Create label to display current name and value
        self.current_label = Label(text='', size_hint=(0.4, 0.1), pos_hint={'x': 0.3, 'y': 0.05}, markup=True)
        self.add_widget(self.current_label)

    def add_item(self, instance):
        name = self.name_input.text
        value = self.value_input.text
        if name and value:
            self.names.append(name)
            self.values.append(value)
            sorted_pairs = sorted(zip(self.names, self.values), reverse=True)
            self.names, self.values = zip(*sorted_pairs)
            self.list_label.text = '\n'.join([f'{n}: {v}' for n, v in zip(self.names, self.values)])
            self.current_index = 0
            self.highlight_current()

    def cycle_list(self, instance):
        if self.values:
            self.current_index = (self.current_index + 1) % len(self.values)
            self.highlight_current()

    def clear_list(self, instance):
        self.names = []
        self.values = []
        self.list_label.text = ''
        self.current_label.text = ''

    def highlight_current(self):
        self.current_label.text = ''
        if self.values:
            n = self.names[len(self.values) - self.current_index - 1]
            v = self.values[len(self.values) - self.current_index - 1]
            self.current_label.text = f'[b][color=FF0000]{n}: {v}[/color][/b]'

class MyApp(App):
    def build(self):
        layout = MyFloatLayout()
        return layout

if __name__ == '__main__':
    MyApp().run()
