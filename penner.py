from bibliopixel.animation import BaseStripAnim
import bibliopixel.colors

class OutBounce(BaseStripAnim):
    def __init__(self, led, duration=100, colors=None, alternating=True, start=0, end=-1):
        # The base class MUST be initialized by calling super like this
        super(OutBounce, self).__init__(led, start, end)
        self.last_idx = None
        self.duration = duration
        self.colors = colors if colors else [bibliopixel.colors.Red]
        self.alternating = alternating
        self.current_color = self.colors[0]
        self.iteration = 0

    def step(self, amt=1):
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
        #print "step is", self._step, "idx is", idx, 'color_idx is', idx % len(self.colors)
        if self.alternating:
            next_color = self.colors[idx % len(self.colors)]
        else:
            next_color = self.current_color

        self._led.set(idx, next_color)
        if idx > self._led.numLEDs:
            self._step = 0
            self.iteration += 1
            if not self.alternating:
                self.current_color = self.colors[self.iteration % len(self.colors)]

        self._step += amt
        self.last_idx = idx
