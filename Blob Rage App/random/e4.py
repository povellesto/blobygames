import math
def polygon (t, n, lenghth):
    angle = 36.0 / n
    for i in range(n):
        fd(t, length)
        lt(t, angle)

def polyline(t, n, length, angle):
    for i in range(n):
        fd(t, length)
        lt(t, angle)
        
def polygon(t, n, length):
    angle = 360.0 / n
    polyline (t, n, length, angle)
    
def arc(t, r, angle):
    arc_length = 2 * math.pi * r* angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, sept_length, step_angle)
    
    
