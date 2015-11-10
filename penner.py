from bibliopixel.animation import BaseStripAnim
from bibliopixel import colors

class OutBounce(BaseStripAnim):
    def __init__(self, led, duration=100, start=0, end=-1):
        # The base class MUST be initialized by calling super like this
        super(OutBounce, self).__init__(led, start, end)
        self.last_idx = None
        self.duration = duration

    def step(self, amt=1):
        #self._led.all_off()
        self._led.setOff(self.last_idx)
        t = self._step
        c = self._led.numLEDs
        b = 0
        t = float(t) / self.duration
        if t < 1 / 2.75:
            step_modifier = 7.5625 * t * t
        elif t < 2 / 2.75:
            t = t - (1.5 / 2.75)
            step_modifier = 7.5625 * t * t + 0.75
        elif t < 2.5 / 2.75:
            t = t - (2.25 / 2.75)
            step_modifier = 7.5625 * t * t + 0.9375
        else:
            t = t - (2.625 / 2.75)
            step_modifier = 7.5625 * t * t + 0.984375

        idx = c * step_modifier + b
        idx = int(idx)
        #print "step is", self._step, "idx is", idx
        self._led.set(idx, colors.Red)
        if idx > self._led.numLEDs:
            self._step = 0
        self._step += amt
        self.last_idx = idx
