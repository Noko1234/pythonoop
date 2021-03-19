# import database
#
# print(database.insert())
# print(database.update())
# print(database.delete())
#
# from database import insert ,update,delete
# from model import insert as ins, update as up, delete as de
# print(insert())
# print(delete())
# print(update())
#
# import sys
# print(sys.platform)
# # print(os.getcwdb())

# from  lib  import  *
# print(db.test())
#
#
# ans = ()
# print(type(ans))

def get_value():
    p = int(input("enter p"))
    t = int(input("enter t"))
    r = int(input("enter r"))
    return p,t,r

def cal_value(p,t,r):
    get_value()
    result = (p * t * r/100)



def dis_value():
    cal_value()

dis_value()
print(dis_value)


