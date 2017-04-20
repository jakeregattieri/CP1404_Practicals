from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

MILES_TO_KILOMETRES = 1.609347


class MilesToKilometres(App):
    def build(self):
        Window.size = (500, 200)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('miles_to_kilometres.kv')
        return self.root

    def handle_miles_to_kilometres(self):
        miles = self.get_validated_miles()
        kilometres = miles * MILES_TO_KILOMETRES
        self.root.ids.output_kilometres.text = str(kilometres)

    def handle_increment(self, change):
        miles = self.get_validated_miles() + change
        self.root.ids.input_miles.text = str(miles)
        self.handle_miles_to_kilometres()

    def get_validated_miles(self):
        try:
            validated_miles = float(self.root.ids.input_miles.text)
            return validated_miles
        except ValueError:
            return 0



MilesToKilometres().run()
