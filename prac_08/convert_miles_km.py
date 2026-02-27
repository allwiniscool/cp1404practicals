from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
CONVERSION_FACTOR_FOR_MILES_TO_KM = 1.60934


class Convertor(App):
    """
    Main program
    """
    def build(self):
        """ Build the Kivy app from the kv file """
        Window.size = (200, 100)
        self.title = " convert miles to km "
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def convert_miles_to_km(self):
        """ convert miles to km """
        try:
            mile_to_km = float(self.root.ids.input_mile.text) * CONVERSION_FACTOR_FOR_MILES_TO_KM
            self.root.ids.km_output.text = str(mile_to_km)
        except ValueError:
            mile_to_km = 0
            self.root.ids.km_output.text = str(mile_to_km)
    def up_or_down(self, up_or_down = 0):
        """Change mile by 1 or -1."""
        try:
            mile = float(self.root.ids.input_mile.text) + up_or_down
            self.root.ids.input_mile.text = str(mile)
        except ValueError:
            mile = 0
            mile = mile + up_or_down
            self.root.ids.input_mile.text = str(mile)

Convertor().run()