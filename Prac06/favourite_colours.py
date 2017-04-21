from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty


class FavouriteColours(App):
    text_output = StringProperty()

    def __init__(self):
        super().__init__()
        self.favourite_colours = {"Bill Bingo": "red", "Gavin Cross": "green", "Sara Ringo": "blue"}

    def build(self):
        self.title = "Favourite Colours"
        self.root = Builder.load_file("favourite_colours.kv")
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for name in self.favourite_colours:
            temp_button = Button(text=name)
            temp_button.bind(on_release=self.press_entry)
            self.root.ids.entriesBox.add_widget(temp_button)

    def press_entry(self, instance):
        name = instance.text
        self.text_output = "{} favourite colour is {}.".format(name, self.favourite_colours[name])

    def clear_widgets(self):
        self.root.ids.entriesBox.clear_widgets()
        self.root.ids.text_output.text = ""


FavouriteColours().run()
