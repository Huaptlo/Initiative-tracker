import kivy
kivy.require('2.1.0')
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class MyApp(App):
    def build(self):
        layout = FloatLayout()
        self.list = []
        
        # Create close button
        close_btn = Button(text='X', size_hint=(0.1, 0.1), pos_hint={'x':0.9, 'y':0.9})
        close_btn.bind(on_press=self.stop)
        layout.add_widget(close_btn)

        # Create input fields and add button
        self.name_input = TextInput(hint_text='Enter name', size_hint=(0.5, 0.1), pos_hint={'x':0.05, 'y':0.8})
        self.value_input = TextInput(hint_text='Enter value', size_hint=(0.15, 0.1), pos_hint={'x':0.55, 'y':0.8})
        add_btn = Button(text='Add', size_hint=(0.15, 0.1), pos_hint={'x':0.7, 'y':0.8})
        add_btn.bind(on_press=lambda x: self.add_to_list(self.name_input.text, self.value_input.text))
        layout.add_widget(self.name_input)
        layout.add_widget(self.value_input)
        layout.add_widget(add_btn)

        # Create list field and clear button
        self.list_label = Label(text='List', size_hint=(0.9, 0.5), pos_hint={'x':0.01, 'y':0.2}, color=(1,1,1,1), halign='center', valign='top')
        clear_btn = Button(text='Clear', size_hint=(0.2, 0.1), pos_hint={'x':0.37, 'y':0.1})
        clear_btn.bind(on_press=self.clear_list)
        layout.add_widget(self.list_label)
        layout.add_widget(clear_btn)

        # Create current value field and next button
        self.value_label = Label(text='Current turn', size_hint=(0.9, 0.1), pos_hint={'x':0.01, 'y':0.7}, color=(1,1,1,1), halign='center', valign='top')
        next_btn = Button(text='Next', size_hint=(0.2, 0.2), pos_hint={'x':0.75, 'y':0.5})
        next_btn.bind(on_press=self.show_next_value)
        layout.add_widget(self.value_label)
        layout.add_widget(next_btn)

        return layout

    # Function for adding name and value to the list and sort in reverse order
    # Only adds the name and value when the value is a integer
    # Also clears the input fields
    def add_to_list(self, name, value):
        try:
            if name and value:
                self.list.append((name, int(value)))
                self.list.sort(key=lambda x: x[1], reverse=True)
                self.update_list_label()
                self.name_input.text = ''
                self.value_input.text = ''
        except:
            pass

    # Function to clear the list
    def clear_list(self, instance):
        self.list = []
        self.list_label.text = ''
        self.value_label.text = ''

    # Function to show the next value
    def show_next_value(self, instance):
        if self.list:
            self.index = (self.index + 1) % len(self.list)
            name, value = self.list[self.index]
            self.value_label.text = f'{name}: {value}'

    # Function to update the list
    def update_list_label(self):
        self.list_label.text = '\n'.join([f'{name}: {value}' for name, value in self.list])
        if self.list:
            name, value = self.list[0]
            self.value_label.text = f'{name}: {value}'
        else:
            self.value_label.text = ''
        self.index = 0

if __name__ == '__main__':
    MyApp().run()
