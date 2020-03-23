# BankCal
小小貸款運算式的演算敘述

# Be Careful of the method called eval

引發資安疑慮的使用方式，讓駭客趁機執行腳本制令於網頁上

       import os

       eval("os.system('whoami')")

安全使用 eval 的聲明方式

eval 的後面两個參數来设置函數的白名單：


     eval(expression[, globals[, locals]])
     
>>>

     eval('os.system('whoami')',{},{})


