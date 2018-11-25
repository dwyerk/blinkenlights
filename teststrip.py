from bibliopixel.animation import BaseStripAnim
from bibliopixel import LEDStrip
from bibliopixel.drivers.LPD8806 import DriverLPD8806
from bibliopixel import colors

class StripTest(BaseStripAnim):
    def __init__(self, led, start=0, end=-1):
        #The base class MUST be initialized by calling super like this
        super(StripTest, self).__init__(led, start, end)
        #Create a color array to use in the animation
        self._colors = [colors.Red, colors.Orange, colors.Yellow, colors.Green, colors.Blue, colors.Indigo]

    def step(self, amt = 1):
        #Fill the strip, with each sucessive color 
        for i in range(self._led.numLEDs):
            self._led.set(i, self._colors[(self._step + i) % len(self._colors)])
        #Increment the internal step by the given amount
        self._step += amt

class Halloween1(BaseStripAnim):
    purple_on = 0
    purple_off = 1
    orange_on = 2
    orange_off = 3
    
    def __init__(self, led, start=0, end=-1):
        super(Halloween1, self).__init__(led, start, end)

        self._colors = [colors.Red, colors.Purple]
        self.state = self.purple_on

    def step(self, amt=1):
        idx = self._step % self._led.numLEDs
        if self._step and idx == 0:
            self.state = (self.state + 1) % 4

        # color seems to be b,r,g
        if self.state == self.purple_on:
            color = (130,75,0)
        elif self.state in (self.purple_off, self.orange_off):
            color = colors.Black
        elif self.state == self.orange_on:
            color = (0,255,69)
        self._led.set(idx, color)
        self._step += amt

purple = (130,75,0)
purple = (255,159,0)
orange = (0,255,69)
orange = (0,255,109)
red = (0,255,0)

blue = (255, 25, 127)
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 0, 255)

thanksgiving = [(00,102,51), (00,204,153), (00,204,102)]

class Kitt(BaseStripAnim):
    def __init__(self, led):
        super(Kitt, self).__init__(led)
        self.length = 32*5

    def step(self, amt=1):
        middle = self.length / 2
        self._led.set(middle, orange)
        self._step += amt

speed = 0.001
speed = 16.0
led = LEDStrip(DriverLPD8806(32*5, dev="/dev/spidev0.0", SPISpeed=speed))
#anim = StripTest(led)
#anim = Halloween1(led)

from strip_animations import *
#anim = RainbowCycle(led)
#anim = ColorPattern(led, [purple, orange], 10)
#anim = ColorPattern(led, thanksgiving, 32)
anim = ColorFade(led, [green, red], 2) # maybe?
#anim = ColorFade(led, thanksgiving, 3)
#anim = ColorChase(led, orange, 10)
#anim = FireFlies(led, [blue, red], width=3, count=2)
#anim = LarsonScanner(led, blue, 10) # cat toy
#anim = LarsonScanner(led, orange, 10) # cat toy
#anim = Kitt(led)
#anim = LarsonRainbow(led)
#anim = Wave(led, blue, 1)
#anim = WaveMove(led, blue, 1)
#anim = RGBClock(led, 0, 30, 51, 70, 90, 160)


import penner
import inspect
all_named_colors = [(x[1][2], x[1][0], x[1][1]) for x in inspect.getmembers(colors) if isinstance(x[1],tuple)]
#anim = penner.OutBounce(led, 2500, all_named_colors, alternating=False)

#anim = PingPong(led, 5)
#anim = BinarySearch(led)
#anim = BubbleSort(led)
anim = Christmas(led)

try:
    anim.run()
except:
    print("resetting")
    class Clear(BaseStripAnim):
        def step(self, amt=1):
            self._led.all_off()

    anim = Clear(led)
    anim.run(max_steps=1)

    raise
