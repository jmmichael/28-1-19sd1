#http://www.pibits.net/learning/python-pwm-gui-example.php
from Tkinter import *
import RPi.GPIO as GPIO
import time
import platform
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
pwm = GPIO.PWM(17, 10)
pwm.start(50)

def on_closing():
    print("Clean up")
    pwm.stop()
    GPIO.cleanup()
    print("bye")
    root.destroy()

 
class App:
	def __init__(self, master):
		frame = Frame(master)
		frame.pack()		
		scale = Scale(frame, from_=0, to=100, orient=VERTICAL, length=500, command=self.update)
		scale.grid(row=0)
		scale.set(50)
	def update(self, duty):
		pwm.ChangeDutyCycle(float(duty))
		
		self.label = Label(text ="slower")
		#self.label.pack() # pack arranges widgets vertically	
root = Tk()
root.wm_title('Motor Control')
app = App(root)
root.geometry("550x520+350+100") #w h		

root.protocol("WM_DELETE_WINDOW", on_closing)		
root.mainloop()
 
#GPIO.cleanup()
