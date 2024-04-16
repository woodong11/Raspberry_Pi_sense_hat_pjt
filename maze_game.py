# 라즈베리파이를 기울이면서 점을 움직여 도착지점까지 이동합니다. 실시간으로 최단경로가 표시됩니다.
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
purple = (255, 0, 255)


def maze_init():
    sense.clear()
    sense.set_pixel(start_x, start_y, green)
    sense.set_pixel(end_x, end_y, green)

    for (y, x) in maze_wall:
        MAP[y][x] = 1
        sense.set_pixel(x, y, wall_color)


def bfs(start_y, start_x):
    q = deque()
    q.append((start_y, start_x, []))
    visited[start_y][start_x] = 1

    while q:
        y, x, path = q.popleft()

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if (ny < 0 or nx < 0 or ny >= 8 or nx >= 8):
                continue
            if (MAP[ny][nx] == 1 or visited[ny][nx] == 1):
                continue
            if (ny == end_y and nx == end_x):
                return path

            new_path = path + [(ny, nx)]
            q.append((ny, nx, new_path))
            visited[ny][nx] = 1
    
    return [(1,1)]


def path_show(path):
        
    global y, x

    # 모두 색칠
    maze_init()
    sense.set_pixel(x, y, purple)
    for (temp_y, temp_x) in path:
        sense.set_pixel(temp_x, temp_y, yellow)

def move_up():
    global y, x
    ny, nx = y + dy[0], x + dx[0]

    if (ny < 0 or nx < 0 or ny >= 8 or nx >= 8):
        return
    if (MAP[ny][nx] == 1):
        return

    sense.set_pixel(x, y, 0, 0, 0)
    sense.set_pixel(nx, ny, purple)
    y, x = ny, nx

def move_down():
    global y, x
    ny, nx = y + dy[1], x + dx[1]

    if (ny < 0 or nx < 0 or ny >= 8 or nx >= 8):
        return
    if (MAP[ny][nx] == 1):
        return

    sense.set_pixel(x, y, 0, 0, 0)
    sense.set_pixel(nx, ny, purple)
    y, x = ny, nx

def move_left():
    global y, x
    ny, nx = y + dy[2], x + dx[2]

    if (ny < 0 or nx < 0 or ny >= 8 or nx >= 8):
        return
    if (MAP[ny][nx] == 1):
        return

    sense.set_pixel(x, y, 0, 0, 0)
    sense.set_pixel(nx, ny, purple)
    y, x = ny, nx

def move_right():
    global y, x
    ny, nx = y + dy[3], x + dx[3]

    if (ny < 0 or nx < 0 or ny >= 8 or nx >= 8):
        return
    if (MAP[ny][nx] == 1):
        return

    sense.set_pixel(x, y, 0, 0, 0)
    sense.set_pixel(nx, ny, purple)
    y, x = ny, nx



maze_init()
sense.set_pixel(start_y, start_x, purple)

while True:
    ori = sense.get_orientation_degrees()
    angle_x = ori['pitch']
    angle_y = ori['roll']
    angle_z = ori['yaw']

    print(f"Degree : X:{angle_x}, Y:{angle_y}, Z:{angle_z} ")
    if ((260 <= angle_x < 350) and ((0 <= angle_y < 10) or (350 <= angle_y < 359))):
        move_right()
    elif ((10 <= angle_x < 120) and ((0 <= angle_y < 10) or (350 <= angle_y < 359))):
        move_left()
        print("dddddddddddddd")
    elif ((260 <= angle_y < 350) and ((0 <= angle_x < 10) or (350 <= angle_x < 359))):
        move_up()
    elif ((10 <= angle_y < 120) and ((0 <= angle_x < 10) or (350 <= angle_x < 359))):
        move_down()


    visited = [[0 for _ in range(8)] for _ in range(8)]
    path = bfs(y, x)
    print(path)
    path_show(path)

    # 도착했을때
    if (y == end_y and x == end_x):
        for _ in range(3):
            for i in range(8):
                for j in range(8):
                    sense.set_pixel(i, j, green)
            sleep(0.1)
            for i in range(8):
                for j in range(8):
                    sense.set_pixel(i, j, 0, 0, 0)
            sleep(0.1)
        exit(0)


    sleep(0.1)
