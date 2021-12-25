import gpiozero

button = gpiozero.Button(17)

while True:
	if button.is_pressed:
		print("ボタンが押されました！")
	else:
		print("ボタンは押されていません！")
