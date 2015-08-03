from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.progressbar import ProgressBar
from kivy.uix.screenmanager import ScreenManager, Screen
pb = ProgressBar(max=1000)

Builder.load_string("""
<StartScreen>:
    BoxLayout:
        Button:
            text: 'Play'
            
    
            
""")
            
class StartScreen(Screen):
    pass

sm = ScreenManager()
sm.add_widget(StartScreen(name='start'))

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