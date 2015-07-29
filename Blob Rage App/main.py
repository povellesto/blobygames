from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.vector import Vector
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.core.audio import SoundLoader
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.colorpicker import CBLColorWheel
from random import randint


# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.

Builder.load_string("""
<StartScreen>:
    BoxLayout:
        Button:
            text: 'Options'
            on_press: root.manager.current = 'options'
        Button:
            text: 'Play'
            on_press: root.manager.current = 'gameOptions'
        

<OptionsScreen>:
    BoxLayout:
        orientation: 'vertical'
        Button:
            text: 'Sound'
        Button:
            text:' Controls'
            on_press: root.manager.current = 'controls'
        Button:
            text: 'Back to Main Menu'
            on_press: root.manager.current = 'start'

<GameOptionsScreen>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Input Cammands to setup Game:'
        BoxLayout:
            orientation: 'horizontal'
            Button:
                text:'Back'
                on_press: root.manager.current = 'start'


<Blob>:
    size: 50, 50
    canvas:
        Ellipse:
            pos: self.pos
            size: self.size
  
<GameScreen>:
    Label:
        font_size: 70  
        center_x: root.width / 2
        top: root.top - 50
        text: "The Game"
        
<ControlsScreen>:
    BoxLayout:
        orientation: 'vertical'
        Button:
            text:'Forward'
            on_press: root.manager.current = 'forwardOptions'
        Button:
            text:'Right'
        Button:
            text:'Left'
        Button:
            text:'Back'
        Button:
            text:'Back to options'
            on_press: root.manager.current = 'options'
        Button:
            text:'Back to main menu'

<forwardOptionsScreen>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Input key Cammand to setup forward comand:'
        BoxLayout:
            orientation: 'vertical'
            Button:
                text:'Back'
                on_press: root.manager.current = 'options'

""")

class Blob(Widget):
    x = NumericProperty(0)
    y = NumericProperty(0)
    pos = ReferenceListProperty(x, y)
    x_velocity = NumericProperty(0)
    y_velocity = NumericProperty(0)
    velocity = ReferenceListProperty(x_velocity, y_velocity)
    velocity = Vector(randint(0, 4), 0).rotate(randint(0, 360))

    def move(self):
        self.pos = Vector(*self.velocity) + Vector(*self.pos)

class StartScreen(Screen):
    pass

class OptionsScreen(Screen):
    pass

class GameOptionsScreen(Screen):
    pass
class ControlsScreen (Screen):
    pass
class forwardOptionsScreen(Screen):
    pass
class GameScreen(Screen):
    #def __init__(self, **kwargs):
        #super(GameScreen, self).__init__(**kwargs)
        #self.blobs = []
        #for index in range(30):
            #blob = Blob()
            #blob.x = randint(0, self.width)
            #blob.y = randint(0, self.height)
            #self.blobs.append(blob)
            #self.add_widget(blob)

    def update(self, dt):
        self.blob.move()
        #for blob in self.blobs:
            #blob.move()
            #bounce off top and bottom
            #if (blob.y < 0) or (blob.top > self.height):
                #blob.velocity_y *= -1

            #bounce off left and right
            #if (blob.x < 0) or (blob.right > self.width):
                #blob.velocity_x *= -1

# Create the screen manager
sm = ScreenManager()
sm.add_widget(StartScreen(name='start'))
sm.add_widget(OptionsScreen(name='options'))
sm.add_widget(GameScreen(name='game'))
sm.add_widget(GameOptionsScreen(name='gameOptions'))
sm.add_widget(ControlsScreen(name='controls'))
sm.add_widget(forwardOptionsScreen(name='forwardOptions'))
class TestApp(App):
    sound = None
    def build(self):
       # self.sound = SoundLoader.load('Spewer - Main Theme.mp3')
        #self.sound.volume = 1
        #self.bind(on_stop=self.sound_replay)
        #self.sound.play()
        return sm

if __name__ == '__main__':
    TestApp().run()
