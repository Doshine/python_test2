while 1:
    gugong = input('请问您是住在故宫吗？')
    if gugong == '是':
        print('尊贵的VIP会员，您让本站蓬荜生辉啊！')
    else:
        house = int(input('你有几套房？'))

        if house > 5:
            print('尊贵的VIP会员，您让本站蓬荜生辉啊！')
        elif house > 2:
            print('您是我们的优质会员，欢迎加入！')
        elif house == 1:
            print('普通会员，典型单身狗啊！')
        else:
            print('凑数会员，不必当真！')