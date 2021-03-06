# Backend_Script3
後端腳本語言 Python

# 開發流程 

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

# 程式設計基礎 

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

https://github.com/QueenieCplusplus/Backend_Script3/blob/master/type_checker.py (Type == isinstance)

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

# 運算的應用情境

Eazy Used in Bank 銀行貸款 =>
https://github.com/QueenieCplusplus/Backend_Script3/blob/master/LoanCaculator.py

BMI for Health 身體健康指標 =>
https://github.com/QueenieCplusplus/Backend_Script3/blob/master/BMI.py

位元與位元組和頻寬與流量, 網路底層運算 =>
https://github.com/QueenieCplusplus/Band_Width/blob/master/dvd_bandwidth_calculation.py

# 時間工具包、打 API、爬蟲、雲端、上傳、寄信 

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
    
Time & Requests & datetime 

(1) url_parser using requests
    
Parser https://github.com/QueenieCplusplus/Py_Parser (Requests tool)

Crawler https://github.com/QueenieCplusplus/Backend_Script3/blob/master/Crawler.py

https://github.com/QueenieCplusplus/API_getter (argparser 參數化和自動化的爬蟲)

https://github.com/QueenieCplusplus/CrawlerByUsingPython

https://github.com/QueenieCplusplus/Pandas_4_xls

Scrapy https://github.com/QueenieCplusplus/Py_Scrapy

Firebase https://github.com/QueenieCplusplus/Backend_Script3/blob/master/FirebaseDB.md

GCP
https://github.com/QueenieCplusplus/Backend_Script3/blob/master/GoogleAPI.py

Form & Post 留言版 =>
https://github.com/QueenieCplusplus/Backend_Script3/blob/master/PostForm.py

https://github.com/QueenieCplusplus/Backend_Script3/blob/master/Post.py

SMTP 寄信 =>
https://github.com/QueenieCplusplus/Backend_Script3/blob/master/SendMail.py

SMB 寄信 =>
(2) smb

# 自動登入與編解碼、光學文字辨識(圖片修改)與猜測驗證碼、資料庫、網站、雲端訊息罐頭

(3)selenium (proxy server using web driver)

https://github.com/QueenieCplusplus/ITsec_BypassSOP/blob/master/selenium.py

https://github.com/QueenieCplusplus/Crawler3

(4)jwt (token generator)
https://github.com/QueenieCplusplus/SSCP_AccessControl#token-generator

https://github.com/QueenieCplusplus/IAP/tree/main/Login_python_app

https://github.com/QueenieCplusplus/SSCP_AccessControl/tree/master/token_generator

(5)光學文字辨識 (using cv2 & pytesseract)
https://github.com/QueenieCplusplus/Backend_Script3/blob/master/pytesseract.py

(6)驗證碼 Captcha (using Keras, CV2, and pytesseract)
https://github.com/QueenieCplusplus/Backend_Script3/blob/master/captcha.py

(7)圖片處理 using imutils and call resize()
https://github.com/QueenieCplusplus/Backend_Script3/blob/master/image_converter.py

    (h, w) = image.shape[:2]

    # if the width > height, then resize along
    if w > h:
        image = imutils.resize(image, width=width)

    # otherwise, h > w
    else:
        image = imutils.resize(image, height=height)

Graphic 圖片修改 
https://github.com/QueenieCplusplus/Backend_Script3/blob/master/Turtle.py

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

雲端訊息罐頭 =>
https://github.com/QueenieCplusplus/PubSub_Python_App

# 人工智慧與大數據

資料分析 https://github.com/QueenieCplusplus/IPython (real-time data analysis)

NTP 套件 todo

(7) Keras 套件 todo

# 相關連結

Python
https://www.python.org/downloads/

file:///Library/Frameworks/Python.framework/Versions/3.8/Resources/English.lproj/Documentation/index.html

other resources =>
https://github.com/QueenieCplusplus/python-cheatsheet

https://github.com/QueenieCplusplus/Backend_Script3-private



