# field hidden, 2020, 1/08, by Queenie Chen
# 私有的資料欄位或是方法有兩個前導底線，而非名稱後面
# 私有欄位資料無法直接被存取
# 需要依靠方法

class HiddenInfo:

    def __init__(self, i="hi"):
        self.__i = i

    def get_hidden_i(self):
        return self.__i

    def set_hidden_i(self, i):
        self.__i = i

def main():
  hi = HiddenInfo("lalala")
  hi.get_hidden_i()
  hi.set_hidden_i(8)

main()
