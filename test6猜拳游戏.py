# 丽江大侠网络
# @时间 : 2022/10/12 21:43
# @作者：和志明
# @版本：1.0.0
# @项目名称：python_test2
import random
lst = ['石头', '剪刀', '布']

def start_window(): #打印游戏开始界面
    print('*' * 50)
    print('----------------1.进入游戏------------------')
    print('----------------0.退出游戏------------------')
    print('*' * 50)

def start_game(): # 进入猜拳游戏界面
    print('请进行猜拳：')
    print('*' * 50)
    print('-----------------1.石  头---------------------')
    print('-----------------2.剪  刀---------------------')
    print('-----------------3.  布-----------------------')
    print('-----------------0.退出游戏--------------------')

def print_results(m, n, result): #打印游戏结果
    """
    打印游戏结果
    :param m:用户输入的选择
    :param n:电脑的选择
    :param result: 结果字符串
    :return:
    """
    my_choice = lst[m - 1] # 将用户输入的数字转换成文字
    com_choice = lst[n - 1] # 将电脑选择的数字转换成文字
    print(f"您的选择是：{my_choice}")
    print(f"电脑的选择是：{com_choice}")
    print(result)

print('-------------欢迎来到我们的猜拳游戏！-------------------')
while True:
    start_window() #进入游戏开始界面
    i = int(input('您要开始猜拳游戏吗？（1 进入，0 退出）')) #接收用户输入，进入或退出游戏
    if i == 0:
        break #退出循环，退出游戏
    elif i == 1:
        start_game() #游戏开始
        m = int(input('请输入您的选择：（1、石头 2、剪刀 3、布 0、退出游戏）'))
        if m == 0:
            break #退出游戏
        if m < 1 or m > 3:
            print('您的输入有误，请按规则出拳，谢谢！')
            continue
        n = random.randint(1, 3) #电脑的选择
        if m == n:
            print_results(m, n, '平局')
        elif m - n == 1 or m - n == -2:
            print_results(m, n, '对不起，您输了！再接再厉！')
        else:
            print_results(m, n, '您获得了胜利，了不起！')

