import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.config import Config
from kivy.base import runTouchApp
kivy.require('2.1.0')
Config.set('graphics', 'resizable', True)


class MyBoxLayout(BoxLayout):
    
    def __init__(self, **kwargs):
        super(MyBoxLayout, self).__init__(**kwargs)
        
        # Create input fields for name and value
        self.name_input = TextInput(hint_text='Enter Name')
        self.add_widget(self.name_input)
        
        self.value_input = TextInput(hint_text='Enter Value')
        self.add_widget(self.value_input)
        
        # Create a button to add name and value to list
        self.add_button = Button(text='Add to List')
        self.add_button.bind(on_press=self.add_to_list)
        self.add_widget(self.add_button)
        
        # Create a label to display the list of name-value pairs
        self.label = Label(text='', size_hint_y=None, height=Window.height)
        self.add_widget(self.label)
        
        # Create a button to close the app
        self.close_button = Button(text='X', size_hint=(None, None), size=(50, 50), pos_hint={'x': 0.95, 'y': 0.95})
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
        self.name_input.text = ''
        self.value_input.text = ''
        
        # Update the label to display the list of name-value pairs
        self.label.text = '\n'.join(['{}: {}'.format(name, value) for name, value in self.name_value_list])
    
    def close_app(self, instance):
        # Close the app
        App.get_running_app().stop()
        

class MyApp(App):
    
    def build(self):
        # Set the app to full-screen
        Window.fullscreen = True
        
        # Create a layout for the app
        layout = MyBoxLayout(orientation='vertical')
        
        return layout
    

if __name__ == '__main__':
    MyApp().run()
