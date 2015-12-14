from bibliopixel.animation import BaseStripAnim
from bibliopixel import LEDStrip
from bibliopixel.drivers.visualizer import DriverVisualizer
from bibliopixel import colors

from penner import OutBounce
import strip_animations as sa

speed = 16.0
led = LEDStrip(DriverVisualizer(32))
anim = sa.PingPong(led)

anim.run()
