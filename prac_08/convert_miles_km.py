from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
CONVERTOR_FOR_MILES_TO_KM = 1.60934


class Convertor(App):
    """ SquareNumberApp is a Kivy App for squaring a number """
    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (200, 100)
        self.title = " convert miles to km "
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def convert_miles_to_km(self):
        try:
            mile_to_km = float(self.root.ids.input_mile.text) * CONVERTOR_FOR_MILES_TO_KM
            self.root.ids.km_output.text = str(mile_to_km)
        except ValueError:
            mile_to_km = 0
            self.root.ids.km_output.text = str(mile_to_km)
    def up_or_down(self, up_or_down = 0):
        try:
            mile = float(self.root.ids.input_mile.text) + up_or_down
            self.root.ids.input_mile.text = str(mile)
        except ValueError:
            mile = 0
            mile = mile + up_or_down
            self.root.ids.input_mile.text = str(mile)
Convertor().run()