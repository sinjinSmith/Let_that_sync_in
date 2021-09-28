import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class MyGrid(Widget):
    folderA = ObjectProperty(None)
    backup_path = ObjectProperty(None)
    
    def btn(self):
        print("folder: ", self.folderA.text, "backup: ", self.backup_path.text)
        self.folderA.text = ""
        self.backup_path.text = ""

class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == '__main__':
    MyApp().run()
