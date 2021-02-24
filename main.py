import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import *
from kivy.clock import Clock
from datetime import datetime
from math import *

class AnalogueClock(FloatLayout):
	def __init__(self, **kwargs):
		super(AnalogueClock, self).__init__(**kwargs)
		with self.canvas:
			Color(rgb=(0, 0, 0))
			Rectangle(pos=(0, 0), size=(800, 1400))
			
		self.min_x, self.min_y = 350, 840
		self.hour_x, self.hour_y = 350, 770
		self.second_x, self.second_y = 350, 850

		with self.canvas:
			Color(rgb=(0, 0.7, 1))
			Ellipse(size=(400, 400), pos=(150, 500))
			
		with self.canvas:
			Color(rgb=(0.2, 0.2, 0.2))
			Ellipse(size=(380, 380), pos=(160, 510))
		
		with self.canvas:
			Color(rgb=(0, 0.7, 1))
			Ellipse(size=(10, 10), pos=(345, 695))
			Line(points=[(350, 895), (350, 875)], width=4)
			Line(points=[(545, 700), (525, 700)], width=4)
			Line(points=[(155, 700), (175, 700)], width=4)
			Line(points=[(350, 505), (350, 525)], width=4)
			
		with self.canvas:
			Color(rgb=(1, 0, 0))
			self.minute_hand = Line(points=[(350, 700), (self.min_x, self.min_y)], width=4)
			
		with self.canvas:
			Color(rgb=(0, 1, 0))
			self.hour_hand = Line(points=[(350, 700), (self.hour_x, self.hour_y)], width=4)
		
		with self.canvas:
			Color(rgb=(0, 0, 1))
			self.second_hand = Line(points=[(350, 700), (self.second_x, self.second_y)], width=2)
			
		Clock.schedule_interval(self.time, 1)

	def time(self, dt):
		self.minutes = int(datetime.now().strftime("%M"))
		self.hours = int(datetime.now().strftime("%H")) + (self.minutes/60)
		self.seconds = int(datetime.now().strftime("%S"))
		
		if self.hours >= 12:
			self.hours -= 12
			
		self.hour_x = 350 + (70*sin(radians(30*self.hours)))
		self.hour_y = 700 + (70*cos(radians(30*self.hours)))
			
		self.hour_hand.points =[(350, 700), (self.hour_x, self.hour_y)]
		
		self.min_x = 350 + (140*sin(radians(6*self.minutes)))
		self.min_y = 700 + (140*cos(radians(6*self.minutes)))
			
		self.minute_hand.points =[(350, 700), (self.min_x, self.min_y)]
		
		self.second_x = 350 + (150*sin(radians(6*self.seconds)))
		self.second_y = 700 + (150*cos(radians(6*self.seconds)))
			
		self.second_hand.points =[(350, 700), (self.second_x, self.second_y)]
		

class MyApp(App):
	def build(self):
		return AnalogueClock()
	
if __name__ == "__main__":
	MyApp().run()
