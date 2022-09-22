import math
import winsound
import os

name = input('请输入姓名：')
weight = int(input('请输入体重：'))
speed = int(input('请输入速度：'))
armor = float(input('请输入盔甲值：'))

power_level = math.log(0.5 * weight * speed ** 2 * (1 + armor))
print(name, '的战斗力指数是：', power_level)
# winsound.Beep(int(200 * power_level), 1000)
if power_level <= 5:
    os.system('2.mp3')
else:
    os.system('1.mp3')
print('GAME OVER!')

