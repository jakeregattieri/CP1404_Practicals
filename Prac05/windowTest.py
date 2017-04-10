from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class SquareNumberApp(App):
    def build(self):
        Window.size = (200, 100)
        self.title = "Square a Number"
        self.root = Builder.load_file('squaring_v2.kv')
        return self.root

    def handle_calculate(self, value):
        result = value ** 2
        self.root.ids.output_label.text = str(result)

SquareNumberApp().run()