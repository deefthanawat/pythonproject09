class ThailandNo1:
    #data 
    wow = 100
    wea = ''
    
    # constructor ไมใฃ่ member แล้วทำงานทุกครั้งที่มีการสร้าง  object
    def __init__(self, woo, wee, wea):
        self.woo = woo
        self.woe = wee
        self.wea = wea

    # method
    def showData(self) :
        print(self.wow * 20)

    # destructor ไม่ใช่ member แต่จะทำงานทุกครั้ง ที่ objrct ทำงานเสร็จ (ถูกทำลาย)
    def __del__(self):
        print('Good morning teacher.....')

o1 = ThailandNo1(10, 20, 10)
o2 = ThailandNo1(10, 20, 30)
o3 = ThailandNo1(5, 20, 10)
o4 = ThailandNo1(10, 20, 10)

print(o1.wea + o2.wea)
o3.showData()


