import cwiid
import time

print("Wiiリモコンのボタン1とボタン2を同時に長押ししてください")
wii = cwiid.Wiimote()
print("接続しました")
wii.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_ACC

while True:
	print(wii.state['acc'])
	time.sleep(0.01)
