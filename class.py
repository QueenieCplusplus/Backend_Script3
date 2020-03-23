# class & obj, 2020, 1/08, by Queenie Chen

import math

# 類別如同契約，很多實例
# 類別有初始器 ＋ 資料欄位(隱藏訊息) ＋ 行為方法
# 類別依靠建構器完成實例生成
# self 變數參考到物件
# 任何變數都是一參考，指定到一物件！

# UML 語言如下
# class ClassName:
#      fields
#      initializer
#      methods = fileds with operators

class QsTemplate:

    def __init__(self, appCount=1):
        self.appCount = appCount

    def get_Apple_total_price(self):
        return self.appCount * 100

    def set_Apple_count(self, appCount):
        self.appCount = appCount

def main():
   qt = QsTemplate(20)
   amount = qt.appCount
   price = qt.get_Apple_total_price
   print(amount)
   print(price)

main()
