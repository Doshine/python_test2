import os
import random
import time

o = 0
note = 0
m = 3
while o < m :
    note = random.randint (1, 8)
    # f_name = 'audio_yj/{0}.mp3'.format(str(i)) ### 这里的相对路径不知道为什么不对
    f_name = 'E:/python/python_test2/audio_yj/{0}.mp3'.format (str (note))
    while True:
        os.system (f_name)
        # time.sleep(5)
        # b_name = int(i)
        guess = int (input ('请输入你所听到的音高是什么（1-8）8代表高音do：'))
        if guess > note:
            print ('实际音高比你听出的音高要低哦！')
            # continue
        elif guess < note:
            print ('实际音高比你听出的音高要高哦！')
            # continue
        else:
            print ('回答正确，VERY GOOD！')
            o += 1
            if m - o != 0:
                print ('再答对{0}次就可以过关了哦！'.format(str(m - o)))
            else:
                print ('恭喜你，顺利过关了！！！')
            break
