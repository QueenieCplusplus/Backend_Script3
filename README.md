# Backend_Script3
後端腳本語言 Python

軟體開發設計流程
其中 SA <-> SD <-> PG 完成 IPO，輸入 -> 流程 -> 輸出的目標。 
SA 注重 IPO >>> SD 注重元件拼圖 >>> PG 注重功能性實作與單元測試 >>> QA 注重掃除 Bug >>> Deploy 注重 軟體能被安裝在所有實體機上。



          Spec  
              ｜＿

                SA
                  ｜＿

                      SD
                        ｜＿

                           PG
                             ｜＿

                                TEST/QA
                                       ｜＿

                                        Deploy & Publish
                                                     ｜＿

                                                        Maintain


plz see code.

特殊運算符號 =>

double *   指數

// 整數除法

E (或是 e)  10的次方數

內建方法 =>

https://github.com/QueenieCplusplus/Backend_Script3/blob/master/eval_input.py

https://github.com/QueenieCplusplus/Backend_Script3/blob/master/variables.py

https://github.com/QueenieCplusplus/Backend_Script3/blob/master/constants.py

https://github.com/QueenieCplusplus/Backend_Script3/blob/master/type_cast.py

https://github.com/QueenieCplusplus/Backend_Script3/blob/master/check_type.py

https://github.com/QueenieCplusplus/Backend_Script3/blob/master/strip.py

https://github.com/QueenieCplusplus/Backend_Script3/blob/master/format.py

https://github.com/QueenieCplusplus/Backend_Script3/blob/master/random.randint.py


選擇邏輯 =>

https://github.com/QueenieCplusplus/Backend_Script3/blob/master/logics.py

重複迴圈 =>

https://github.com/QueenieCplusplus/Py_Loop (project)

https://github.com/QueenieCplusplus/Backend_Script3/blob/master/loop.py

https://github.com/QueenieCplusplus/Backend_Script3/blob/master/for.py

方法呼叫 =>

https://github.com/QueenieCplusplus/Backend_Script3/blob/master/main.py


          def method(x, y): # x & y are param in concept as placeholder
             body
             return caller
             
          
          method(n1, n2) # n1 & n2 are actual param called arg
          
類別實例:設計物件的資料欄位(項目)和行為的樣板或是契約抑或是藍圖 =>

https://github.com/QueenieCplusplus/Backend_Script3/blob/master/class.py

隱藏資訊:封裝資訊和萃取出資訊 =>

https://github.com/QueenieCplusplus/Backend_Script3/blob/master/info_hide.py

動態鏈結: 多型 polymorphics 又稱 多載 overload =>

https://github.com/QueenieCplusplus/Backend_Script3/blob/master/overload.py

覆寫 =>

https://github.com/QueenieCplusplus/Backend_Script3/blob/master/override.py

導入(模組) =>

https://github.com/QueenieCplusplus/PyPkgModuleFunc

工具管理 =>

https://github.com/QueenieCplusplus/pip_4_py

其他應用 =>

Time tool

> datetime

    import datetime as d 

    y_d =d.date.today() + d.timedelta(-1) # arg of timedelta is days
    print('yesterday is', y_d)

    # using .strftime()
    y_Y, y_M, y_D = y_d.strftime("%Y"), y_d.strftime("%m"), y_d.strftime("%d")
    print(y_Y, y_M, y_D)

    target_url_y = 'https://www.....//{y_y}/{y_y}{y_m}/{name}.{y_y}{y_m}{y_d}-C.xls'.format(name=query_sheet_subtract_1day, y_y=y_Y, y_m=y_M, y_d=y_D)

    res = req.get(url=target_url_y, timeout=600)
    print(res.url, res.status_code)
    print(res.headers['Content-Type'], res.headers['Date'])
    
    # application/vnd.ms-excel Wed, 26 Feb 2020 02:10:56 GMT

    return res.content
    
 > time
 
     import time as t 
 
     lt = t.localtime()
     zero = 0

    target_url = 'https://www......//{t[0]}/{t[0]}{zero}{t[1]}/{name}.{t[0]}{zero}{t[1]}{t[2]}-C.xls'.format(name=query_sheet, zero=zero, t=lt)

    #req.headers['Accept'] = 'application/vnd.ms-excel'

    res = req.get(url=target_url, timeout=500)

    print(res.url, res.status_code)
    print(res.headers['Content-Type'], res.headers['Date'])

    return res.content
    
Time & Requests & datetime https://github.com/QueenieCplusplus/Backend_Script3/tree/master/url_parser (auto_parser)
    
Parser https://github.com/QueenieCplusplus/Py_Parser (Requests tool)

Crawler https://github.com/QueenieCplusplus/Backend_Script3/blob/master/Crawler.py

Scrapy https://github.com/QueenieCplusplus/Py_Scrapy

Firebase https://github.com/QueenieCplusplus/Backend_Script3/blob/master/FirebaseDB.md

GCP
https://github.com/QueenieCplusplus/Backend_Script3/blob/master/GoogleAPI.py

Graphic
https://github.com/QueenieCplusplus/Backend_Script3/blob/master/Turtle.py

Eazy Used in Bank
https://github.com/QueenieCplusplus/Backend_Script3/blob/master/LoanCaculator.py

BMI for Health
https://github.com/QueenieCplusplus/Backend_Script3/blob/master/BMI.py

Form & Post 留言版 =>
https://github.com/QueenieCplusplus/Backend_Script3/blob/master/PostForm.py

https://github.com/QueenieCplusplus/Backend_Script3/blob/master/Post.py

SMTP 寄信 =>
https://github.com/QueenieCplusplus/Backend_Script3/blob/master/SendMail.py

SMB 寄信 =>
(1) smb

爬蟲專案、自動登入、猜測驗證碼、表單填寫、上傳圖片、編碼、檔案格式、運算、圖片修改、光學文字辨識=>

https://github.com/QueenieCplusplus/API_getter (argparser 參數化和自動化的爬蟲)

https://github.com/QueenieCplusplus/Backend_Script3/tree/master/captchas_crack (破解驗證 using pytesseract)

(2)selenium (selenium)
https://github.com/QueenieCplusplus/ITsec_BypassSOP/blob/master/selenium.py

(3)jwt (token generator)
https://github.com/QueenieCplusplus/SSCP_AccessControl#token-generator

https://github.com/QueenieCplusplus/CrawlerByUsingPython

https://github.com/QueenieCplusplus/Pandas_4_xls

https://github.com/QueenieCplusplus/IPython (real-time data analysis)

通訊端 Socket =>
https://github.com/QueenieCplusplus/Backend_Script3/tree/master/socket

Vsphere 虛擬環境套件 =>
https://github.com/QueenieCplusplus/Backend_Script3/blob/master/socket_service.py

資料庫驅動程式 =>
https://github.com/QueenieCplusplus/Backend_Script3/blob/master/post_data.py (post)

          post_a_data = requests.post("http://user:pwd@ip:port", json=data)

https://github.com/QueenieCplusplus/PyMySQL (pymysql)

https://github.com/QueenieCplusplus/SQLAlchemy_app (sqlalchemy)

羽量級網站 =>
https://github.com/QueenieCplusplus/apiscraper (flask)

網站框架 =>
https://github.com/QueenieCplusplus/Py_Django (django)

NLTK tool 自然語言套件組 =>
TBD...

Python
https://www.python.org/downloads/

file:///Library/Frameworks/Python.framework/Versions/3.8/Resources/English.lproj/Documentation/index.html

other resources =>
https://github.com/QueenieCplusplus/python-cheatsheet




