class suite1:
    def __init__(self, mic, coke, French_Fries):
        self.mic = mic
        self.coke = coke
        self.French_Fries= French_Fries
    def set_set(self):
        return (self.mic + self.coke + self.French_Fries) * 0.8
class bigmore(suite1):
    def __init__(self,big1 ):
        self.big1=big1
    def big_over(self):
        return self.big1 + s.set_set()
a = eval(input("input mic price : "))
b = eval(input("input coke price : "))
c = eval(input("input Frech Fries price : "))
s = suite1(a, b, c)
s.set_set()
print ("大麥克套餐：", s.set_set())
m = bigmore( 5 )
m.big_over()
print ("薯條可樂加大：", m.big_over())