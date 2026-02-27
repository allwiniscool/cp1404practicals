from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label




class DynamicWidgetsLabel(App):
    """
    Main program
    """
    def __init__(self, **kwargs):
        """
        Construct main app
        """
        super().__init__(**kwargs)
        self.names= ["Bob Brown", "Cat Cyan", "Oren Ochre"]

    def build(self):
        """ Build the Kivy app from the kv file """
        self.title = " Names As Labels "
        self.root = Builder.load_file("dynamic_labels.kv")
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create labels from names."""
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)


DynamicWidgetsLabel().run()