# Raspberry_Pi_sensehat_pjt
라즈베리파이와 센스햇을 활용한 미니 프로젝트입니다. (자이로센서 + bfs를 활용한 미로탈출게임)

[![Video Label](http://img.youtube.com/vi/Q_8mUl34uPM/0.jpg)](https://youtu.be/Q_8mUl34uPM)

## ready to sense hat
<h3>센스햇 설치 과정</h3> <br>

라즈베리파이의 전원을 끄고 케이블을 완전히 분리한 후, 센스햇을 연결합니다. <br>
![image](https://github.com/woodong11/Raspberry_Pi_sense_hat_pjt/assets/91379630/4c6780f6-2aba-47d0-b132-1c48c7088dc2)


$ `git clone https://github.com/astro-pi/python-sense-emu`

$ `cd ./python-sense-emu`

$ `sudo python3 [setup.py](http://setup.py/) install`


<h3>센스햇 정상 동작 확인 </h3> <br>
다음 파이썬 코드를 실행합니다. <br>

```

from sense_hat import SenseHat
sense = SenseHat()
sense.show_message("HELLO")

```
<h3>Trouble Shooting </h3> <br>
RPi-Sense를 찾을 수 없다는 에러가 뜨면, /boot/firmware/config.txt에 다음 내용을 추가합니다. <br>

`sudo vi /boot/firmware/config.txt`  <br>

`dtoverlay=rpi-sense` <br>
내용 추가 후 저장 <br>

<br>이후 재부팅하기<br>
`sudo reboot`





## imu_pixel_move.py
라즈베리파이를 기울여 점의 위치를 이동합니다. (센스햇에 부착된 IMU의 자이로스코프 센서 이용) <br>
 <br>
<img src = "https://github.com/woodong11/Raspberry_Pi_sense_hat_pjt/assets/91379630/6b261180-e0d5-4993-a7af-6171a6863cfc" width="40%" height="40%">
 <h3> run </h3> <br>
 
$ `python3 imu_pixel_move.py`





## maze_game.py
모든경로출력: 버튼을 누를 때 마다 시작지점에서 도착지점까지 모든 경로가 출력됩니다. <br>
dfs 알고리즘을 사용했습니다. <br>
<img src = "https://github.com/woodong11/Raspberry_Pi_sense_hat_pjt/assets/91379630/5d449d18-769d-419f-a44b-70ac6b5121de" width="40%" height="40%">

 <h3> run </h3> <br>
 
$ `python3 imu_pixel_move.py`






## path_find.py

점이 이동될 때 마다 목적지까지 최단 경로가 실시간으로 출력됩니다. (센스햇에 부착된 IMU의 자이로스코프 센서 이용) <br>
bfs 알고리즘을 사용했습니다. <br>
<img src = "https://github.com/woodong11/Raspberry_Pi_sense_hat_pjt/assets/91379630/2c8825ab-7ca2-414c-b50e-e67108391cb8" width="40%" height="40%">

 <h3> run </h3> <br>
 
$ `python3 imu_pixel_move.py`


