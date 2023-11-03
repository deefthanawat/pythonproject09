def sumNumber():
    pass 

# สร้าง Class ใน python
class IoTSAU :
    # data/attribute/file/property member เหมือนกับตัวแปล
    info1 =  20 
    info2 = ''

    # method member เหมือนกับฟังก์ชั่น
    def showHi(self):
        print('Hi....')
    
    def showInfo(self):
        print(self.info1, self.info1)
        self.showHi

# สร้าง Object
obA = IoTSAU()
obB = IoTSAU ()
obC = IoTSAU()

obA.info1 = 100
print(obA.info1 + obB.info1) # = 120
obC.showInfo()
obA.showInfo()