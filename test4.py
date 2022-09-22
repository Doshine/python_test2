import os
import random
import time

i = 1
f_name = ''
while i <= 8:
    i = random.randint(1, 8)
    # f_name = 'audio_yj/{0}.mp3'.format(str(i)) ### 这里的相对路径不知道为什么不对
    f_name = 'C:/Users/和志明/PycharmProjects/pythonProject/audio_yj/{0}.mp3'.format(str(i))
    os.system(f_name)
    time.sleep(2 / random.randint(1, 3))
