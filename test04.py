# คุณสมบัคิเด่น OOP : Inheritance
# คุณสมบัคิเด่น OOP : Polymorphism
class TestA: 
    data1 = 10 
    data2 = 20 

    def showSAU() :
        print('Hi....SAU')

class TestB(TestA) :
    data = 30 
    
    def showWow() : 
        print('wow wow wow')

class TestC(TestA) :
    data4 = 40

class TestD(TestB) :
    data5 = 50

o1 = TestA()
o2 = TestB()
o2 = TestD()

class Test2( TestA ) :
    data6 = 60

    def showSAU():
        print('wildl.....SSAAWW')

o4 = Test2()



