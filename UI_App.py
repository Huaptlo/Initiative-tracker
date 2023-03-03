# Initiative tracker project 2023
# Main code functionality
# Written by Max Creutz

import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
kivy.require('2.1.0')


class MyFloatLayout(FloatLayout):
    
    def __init__(self, **kwargs):
        super(MyFloatLayout, self).__init__(**kwargs)
        
        # Create input fields for name and value
        self.name_input = TextInput(hint_text='Enter Name', size_hint=(0.8, 0.1), pos_hint={'x': 0.1, 'y': 0.8})
        self.add_widget(self.name_input)
        
        self.value_input = TextInput(hint_text='Enter Value', size_hint=(0.8, 0.1), pos_hint={'x': 0.1, 'y': 0.6})
        self.add_widget(self.value_input)
        
        # Create a button to add name and value to list
        self.add_button = Button(text='Add to List', size_hint=(0.4, 0.1), pos_hint={'x': 0.3, 'y': 0.4})
        self.add_button.bind(on_press=self.add_to_list)
        self.add_widget(self.add_button)
        
        # Create a label to display the list of name-value pairs
        self.label = Label(text='', size_hint=(0.8, 0.4), pos_hint={'x': 0.1, 'y': 0})
        self.add_widget(self.label)
        
        # Create a button to close the app
        self.close_button = Button(text='X', size_hint=(0.1, 0.1), pos_hint={'x': 0.9, 'y': 0.9})
        self.close_button.bind(on_press=self.close_app)
        self.add_widget(self.close_button)
        
        # Create an empty list to store name-value pairs
        self.name_value_list = []
    
    def add_to_list(self, instance):
        # Get the name and value from input fields
        name = self.name_input.text
        value = self.value_input.text
        
        # Add the name-value pair to the list and clear the input fields
        self.name_value_list.append((name, value))
        self.name_value_list.sort(key=lambda x: x[1], reverse=True)
        self.name_input.text = ''
        self.value_input.text = ''
        
        # Update the label to display the list of name-value pairs
        self.label.text = '\n'.join(['{}: {}'.format(name, value) for name, value in self.name_value_list])

        # Add label to display current value
        self.value_label = Label(text=str(self.values[self.index]), size_hint=(0.5, 0.2), pos_hint={'x': 0.25, 'y': 0.4}, color=(0, 0, 0, 1),
                                 font_size=50, halign='center', valign='middle')
        self.add_widget(self.value_label)

        # Add button to cycle through values
        button = Button(text='Next',
                        size_hint=(0.2, 0.1),
                        pos_hint={'x': 0.4, 'y': 0.2})
        button.bind(on_press=self.next_value)
        self.add_widget(button)
    
    def next_value(self, instance):
        self.index = (self.index + 1) % len(self.values)
        self.value_label.text = str(self.values[self.index])
    
    def close_app(self, instance):
        # Close the app
        App.get_running_app().stop()
        

class MyApp(App):
    
    def build(self):
        # Set the app to full-screen
        # Window.fullscreen = True
        
        # Create a layout for the app
        layout = MyFloatLayout()
        
        return layout
    

if __name__ == '__main__':
    MyApp().run()