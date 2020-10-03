from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty


class DynamicLabels(App):
    """Create a dynamic list"""
    status_text = StringProperty()

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        # basic data example - dictionary of names: phone numbers
        self.names = ["Steve Hyde", "Michael Kelso", "Donna Pinciotti", "Donna Pinciotti", "Eric Forman"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create buttons from dictionary entries and add them to the GUI."""
        for name in self.names:
            # create a button for each data entry, specifying the text and id
            # (although text and id are the same in this case, you should see how this works)
            temp_button = Button(text=name, id=name)
            temp_button.bind(on_release=self.press_entry)
            # add the button to the "entries_box" layout widget
            self.root.ids.entries_box.add_widget(temp_button)

    def press_entry(self, instance):
        """
        Handle pressing entry buttons.
        :param instance: the Kivy button instance that was clicked
        """
        # get name (dictionary key) from the id of Button we clicked on
        name = instance.id  # or name = instance.text
        # update status text
        self.status_text = "{}'s number is {}".format(name, self.names[name])

    def clear_all(self):
        """Clear all of the widgets that are children of the "entries_box" layout widget."""
        self.root.ids.entries_box.clear_widgets()