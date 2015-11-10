from bibliopixel.animation import BaseStripAnim
from bibliopixel import LEDStrip
from bibliopixel.drivers.visualizer import DriverVisualizer
from bibliopixel import colors

from penner import OutBounce

speed = 16.0
led = LEDStrip(DriverVisualizer(32))
anim = OutBounce(led)

anim.run()

