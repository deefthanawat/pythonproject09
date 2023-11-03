# คุณสมบัคิเด่น OOP : Encapsulation (ห่อหุ้ม ซ่อน)
# ห่อหุ้ม data โดยใส่ __ ไว้หน้าชื่อ Data เช่น __data
class MyTestA : 
    __data1 = 10 
    data2 = 20
   
   # เมื่อ data ถูก Encap. การกำหนดค่าหรือเอาค่ามาใช้
   # ให้ผ่านเมธอด get เอาค่ามาใช้/set กำหนดค่า
    def getData1(self) :
        return self.__data1

    def getData1(self, data1) :
        self.__data1 = data1

    def getData3(self) :
        return self.__data3
    
    def setData3(self, data3) :
        self.__data3 = data3


    def __init__(self, data3) :
        self.__data3 = data3

    def showData(self) : 
        print(f'__data1 มีค่า {self.__data1}')
        print(f'data2 มีค่า {self.data2}')
        print(f'__data3 มีค่า {self.__data3}')
        print('...................')

o1 = MyTestA(30)
o1.showData()
o1.data2 = 200
o1.setData1(100)
o1.__data1 = 100
o1.__data3 = 999
o1.showData()
print( o1.getData3() )