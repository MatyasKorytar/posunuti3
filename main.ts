led.plot(1, 0)
led.plot(0, 1)
input.onButtonPressed(Button.AB, function on_button_pressed_AB() {
    let x = 1
    let y = 0
    while (y < 4) {
        basic.clearScreen()
        led.plot(x, y)
        led.plot(y, x)
        x += 1
        y += 1
        basic.pause(3000)
    }
})
