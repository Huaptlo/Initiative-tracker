import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.properties import ListProperty
kivy.require('2.1.0')


class MyFloatLayout(FloatLayout):
    data = ListProperty([])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.popup = None

    def on_data(self, instance, value):
        self.clear_widgets()
        highest_value = -1
        for i, (name, val) in enumerate(value):
            if val > highest_value:
                highest_value = val
            label = Label(text=f"{name}: {val}", font_size=30, size_hint=(1, None), height=50, pos_hint={'top': 1 - i / len(value)})
            self.add_widget(label)
            remove_button = Button(text='X', size_hint=(None, None), height=50, width=50, pos_hint={'right': 1}, background_color=(1, 0, 0, 1))
            remove_button.bind(on_press=lambda _, idx=i: self.remove_data(idx))
            label.add_widget(remove_button)
        self.highlight_highest_value(highest_value)

    def add_data(self, name, value):
        self.data.append((name, value))
        self.data = sorted(self.data, key=lambda x: x[1], reverse=True)
        self.popup.dismiss()

    def remove_data(self, idx):
        del self.data[idx]

    def highlight_highest_value(self, highest_value):
        for child in self.children:
            if isinstance(child, Label):
                name, val = child.text.split(': ')
                if int(val) == highest_value:
                    child.color = (1, 0, 0, 1)
                else:
                    child.color = (1, 1, 1, 1)

    def clear_data(self):
        self.data = []


class MyPopup(Popup):
    def __init__(self, add_data_callback, **kwargs):
        super().__init__(**kwargs)
        self.add_data_callback = add_data_callback

    def add_data(self):
        name = self.ids.name.text
        value = self.ids.value.text
        if name and value:
            self.add_data_callback(name, int(value))


class MyApp(App):
    def build(self):
        layout = MyFloatLayout()

        add_button = Button(text='Add data', font_size=30, size_hint=(None, None), height=50, width=200, pos_hint={'center_x': 0.5, 'center_y': 0.9})
        add_button.bind(on_press=lambda _: self.show_popup(layout))
        layout.add_widget(add_button)

        clear_button = Button(text='Clear data', font_size=30, size_hint=(None, None), height=50, width=200, pos_hint={'center_x': 0.5, 'center_y': 0.05}, background_color=(1, 0, 0, 1))
        clear_button.bind(on_press=lambda _: layout.clear_data())
        layout.add_widget(clear_button)

        return layout

    def show_popup(self, layout):
        if not layout.popup:
            layout.popup = MyPopup(layout.add_data)
        layout.popup.open()


if __name__ == '__main__':
    MyApp().run()
