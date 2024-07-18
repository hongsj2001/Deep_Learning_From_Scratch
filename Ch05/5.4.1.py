#5.4.1 단순한 계층 구현하기 - 곱셈 계층

class Mullayer:
    def __init__(self):
        self.x = None
        self.y = None
    def forward(self,x,y):
        self.x = x
        self.y = y
        out = x*y

        return out
    def backward(self,dout):
        dx = dout*self.y
        dy = dout*self.x

        return dx,dy
    
apple = 100
apple_num = 2
tax = 1.1

mul_apple_layer = Mullayer()
mul_tax_layer = Mullayer()

apple_price = mul_apple_layer.forward(apple,apple_num)
price = mul_tax_layer.forward(apple_price,tax)

print(price)

dprice = 1
dapple_price,dtax = mul_tax_layer.backward(dprice)
dapple, dapple_num = mul_apple_layer.backward(dapple_price)

print(dapple,dapple_num,dtax)