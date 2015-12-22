import strip_animations as sa

def test_rgb2hsv_gray():
    sa.rgb2hsv((0,0,0))

def test_rgb2hsv_gray2():
    sa.rgb2hsv((255,255,255))
