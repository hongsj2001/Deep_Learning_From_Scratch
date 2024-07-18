#1.4.2 Class
class Man: #Man이라는 Class 생성
    def __init__(self, name): #생성자
        self.name = name
        print("Initialized!")
    def hello(self):
        print("Hello, " + self.name + "!")
    def goodbye(self):
        print("Good-Bye, " + self.name + "!")

m = Man("David") #David 라는 name을 갖는 객체 생성
m.hello()
m.goodbye()