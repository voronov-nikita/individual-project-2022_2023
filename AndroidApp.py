import socket
from pyautogui import size

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen


class MainScreen(Screen):
    def __init__(self):
        super().__init__()
        self.name = "Main"
        self.Init()

    def Init(self):
        bx = BoxLayout(orientation="vertical")
        btn = Button(text="Connect", )
        btn.bind(on_press=self.the_next_screen)
        bx.add_widget(btn)
        self.add_widget(bx)

    def the_next_screen(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = "Stream"
        return 0


class StreamScreen(Screen):
    def __init__(self):
        super().__init__()
        self.name = "Stream"
        x, y = map(int, size())
        self.fl = FloatLayout(size=(x, y))
        self.lbl = Label(text="Text")
        self.Init()

    def Init(self):
        # bxx = BoxLayout(orientation="vertical")

        self.fl.add_widget(self.lbl)
        self.fl.add_widget(Button(text="exit",
                                  # color="white",
                                  opacity=0.1,
                                  size_hint=(.1, .1),
                                  pos=(.5, .5),
                                  pos_hint={'x': 0, 'y': 0.9},
                                  on_press=self.exit))
        self.add_widget(self.fl)

    def exit(self, instance):
        self.manager.transition.direction = 'left'
        self.manager.current = "Main"
        return 0


class MainApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen())
        sm.add_widget(StreamScreen())

        return sm


if __name__ == "__main__":
    MainApp().run()
