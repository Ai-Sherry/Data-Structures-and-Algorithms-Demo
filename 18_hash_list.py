#在Pyhon中散列表即为字典
voted={}
def check_voted(name):
    if voted.get(name):
        print('kich them out')
    else:
        voted[name]=True
        print('let them vote')
