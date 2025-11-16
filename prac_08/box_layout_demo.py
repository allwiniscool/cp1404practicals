from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    """
    Main program
    """
    def build(self):
        """ Build the Kivy app from the kv file """
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root
    def handle_greet(self):
        """Take input from the user and display the greeting."""
        self.root.ids.input_name.text = f"Hello {self.root.ids.input_name.text}"
    def clear(self):
        """Clear the screen."""
        if self.root.ids.input_name.text != "" or self.root.ids.output_label.text != "Enter your name":
            self.root.ids.input_name.text = ""
            self.root.ids.output_label.text = "Enter your name"



BoxLayoutDemo().run()
