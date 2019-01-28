#http://www.pibits.net/learning/python-pwm-gui-example.php
from Tkinter import *
import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
pwm = GPIO.PWM(17, 10)
pwm.start(0)
 
class App:
	def __init__(self, master):
		frame = Frame(master)
		frame.pack()		
		scale = Scale(frame, from_=0, to=100, orient=VERTICAL, length=500, command=self.update)
		scale.grid(row=0)
		scale.set(0)
		
		self.label = Label(text ="slower")
		self.label.pack() # pack arranges widgets vertically
		
	def update(self, duty):
		pwm.ChangeDutyCycle(float(duty))	
root = Tk()
root.wm_title('Motor Control')
app = App(root)
root.geometry("150x520+350+175") #w h		
		
root.mainloop()
 
#GPIO.cleanup() cleanup leaves the motor running
