led.plot(1, 0)
led.plot(0, 1)
def on_button_pressed_AB():
    x = 1
    y = 0
    while y < 4:
        basic.clear_screen()
        led.plot(x, y)
        led.plot(y, x)
        x += 1
        y += 1
        basic.pause(3000)
input.on_button_pressed(Button.AB, on_button_pressed_AB)