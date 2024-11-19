from contextlib import nullcontext

from kivy.app import App
from kivy.core.window import android
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics.texture import Texture
from plyer import camera, orientation
import cv2

class TestApp(App):
    def build(self):
       # startPoint = (100,50)
       # endPoint = (215, 80)


        layout = BoxLayout(orientation='vertical')
        #cam = cv2.VideoCapture(0)
        cam = Camera(play=True, resolution=(800,800))

        layout.add_widget(cam)


        return layout


TestApp().run()