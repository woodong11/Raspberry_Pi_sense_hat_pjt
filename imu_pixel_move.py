# 라즈베리파이를 기울여 점의 위치를 이동합니다. (IMU의 자이로스코프 센서 이용)
from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
from sense_hat import SenseHat
from signal import pause
from time import sleep

x = 3
y = 3
sense = SenseHat()

def clamp(value, min_value=0, max_value=7):
    return min(max_value, max(min_value, value))

def move_up():
    global y
    y = clamp(y - 1)

def move_down():
    global y
    y = clamp(y + 1)

def move_left():
    global x
    x = clamp(x - 1)

def move_right():
    global x
    x = clamp(x + 1)

def refresh():
    sense.clear()
    sense.set_pixel(x, y, 255, 255, 255)


while True:

    ori = sense.get_orientation_degrees()
    angle_x = ori['pitch']
    angle_y = ori['roll']
    angle_z = ori['yaw']
    
    
    print(f"Degree : X:{angle_x}, Y:{angle_y}, Z:{angle_z} ")
    if ((260 <= angle_x < 350) and  ((0 <= angle_y < 10) or  (350 <= angle_y < 359))):
    	move_right()
    elif ((10 <= angle_x < 120) and  ((0 <= angle_y < 10) or (350 <= angle_y < 359))):
    	move_left()
    elif ((260 <= angle_y < 350) and  ((0 <= angle_x < 10) or  (350 <= angle_x < 359))):
    	move_up()
    elif ((10 <= angle_y < 120) and ((0 <= angle_x < 10) or  (350 <= angle_x < 359))):
    	move_down()
    
    refresh()
    sleep(0.1)



pause()
