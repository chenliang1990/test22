class BaBa():
    name = "马云"
    money = "500E"

    def make_money(self):
        print("{}可以赚钱".format(self.name))
        self.use_money()
    def use_money(self):
        print("马爸爸挥金如土")

# baba = BaBa()
# baba.make_money()

class Son(BaBa):
    name = "小马"
    money = "05.W"
    # 重写父类方法
    # def use_money(self):
    #     print("小马很会花钱")
print(Son().name)
Son().use_money()
