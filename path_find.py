# 센스햇 조이스틱의 middle 버튼을 누를 때 마다 다른 경로가 출력됩니다.
from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
from sense_hat import SenseHat
from signal import pause
from time import sleep
from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
start_y, start_x = 0, 7
end_y, end_x = 7, 0
y = start_y
x = start_x

MAP = [[0 for _ in range(8)] for _ in range(8)]
visited = [[0 for _ in range(8)] for _ in range(8)]
maze_wall = [[1, 1], [1, 4], [1, 6], [1, 7],
             [2, 1], [2, 2], [2, 3], [2, 4], [2, 6],
             [3, 4], [3, 6],
             [4, 0], [4, 2], [4, 4], [4, 6],
             [5, 0], [5, 2],
             [6, 0], [6, 2], [6, 3], [6, 4], [6, 6]
             ]

path_list = []
show_num = 0

sense = SenseHat()
wall_color = (100, 150, 150)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
yellow = (200, 255, 0)


def maze_init():
    sense.clear()
    sense.set_pixel(start_x, start_y, green)
    sense.set_pixel(end_x, end_y, green)

    for (y, x) in maze_wall:
        MAP[y][x] = 1
        sense.set_pixel(x, y, wall_color)

def print_test():
    for path in path_list:
        print(path)


def dfs(y, x, path):
    if y == end_y and x == end_x:
        path.pop()
        path_list.append(path)
        return

    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if ny < 0 or nx < 0 or ny >= 8 or nx >= 8:
            continue
        if MAP[ny][nx] == 1 or visited[ny][nx] == 1:
            continue

        new_path = path + [(ny, nx)]
        visited[ny][nx] = 1
        dfs(ny, nx, new_path)
        visited[ny][nx] = 0



def path_show(event):
    global show_num

    if event.action != ACTION_RELEASED:
        cnt = len(path_list)
        show_num = (show_num + 1) % cnt

        # 모두 색칠
        maze_init()
        for (y, x) in path_list[show_num]:
            sense.set_pixel(x, y, yellow)
        
        
        for (y, x) in path_list[show_num]:
            sense.set_pixel(x, y, 90, 90, 50)
            sleep(0.02)
            sense.set_pixel(x, y, yellow)
            sleep(0.02)



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




sense.stick.direction_middle = path_show

maze_init()
dfs(start_y, start_x, [])
print_test()


while True:
    ori = sense.get_orientation_degrees()
    angle_x = ori['pitch']
    angle_y = ori['roll']
    angle_z = ori['yaw']

    print(f"Degree : X:{angle_x}, Y:{angle_y}, Z:{angle_z} ")

    sleep(0.1)

pause()
