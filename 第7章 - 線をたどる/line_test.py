import gpiozero
import time

line_sensor = gpiozero.DigitalInputDevice(9)

while True:
	if line_sensor.is_active == False:
		print("線を見つけました")
	else:
		print("線を見つけられませんでした")

	time.sleep(0.2)
