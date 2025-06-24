'''def ชื่อฟังก์ชั่น(parameter):
        return value, value2
'''
# ไม่รับ parameter
def greeting_eng():
    print("Hello world!!!!")
    print("Hi")
    
def greeting_th():
    print("ว่าไง!!!!")
    print("สวัสดีชาวโลก")
    
def get_time():
    from datetime import datetime
    now = datetime.now()
    print(now)
    
get_time()