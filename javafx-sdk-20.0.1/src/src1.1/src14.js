let ledBrightness = 0

pins.analogWritePin(AnalogPin.P0, 0)

input.onButtonPressed(Button.A, function () {
    if (ledBrightness >= 1020){
        ledBrightness = 0
    } else {
        ledBrightness = ledBrightness + 20
    }
})

input.onButtonPressed(Button.B, function () {
    if (ledBrightness == 0) {
        ledBrightness = 1020
    } else {
        ledBrightness = ledBrightness - 20
    }
})

basic.forever(function () {
    led.plotBarGraph(ledBrightness, 1020)
    pins.analogWritePin(AnalogPin.P0, ledBrightness)
})
