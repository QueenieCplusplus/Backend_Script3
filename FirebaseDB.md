# Realtime DB, 即時資料庫

Firebase Realtime DB

https://github.com/QuinoaPy/MongoDB#nosql-不只是-sql

# Data Structure in Colletion using K/V pairs, 資料結構(鍵值對的資料集合)

https://github.com/QuinoaPy/MongoDB#intro-簡介

# DB setup, 資料庫設定

https://github.com/QuinoaPy/MongoDB#cloud-data-storage-雲端存儲

# add SDK, 注入模組

  // ios
  
    Pod 'Firebase/Core'
    Pod 'Firebase/Auth'
    Pod 'Firebase/Database'
  
  // android
  
    implementation 'com.google.firebase:firebase-core:11.0.4'
    implementation 'com.google.firebase:firebase-auth:11.0.4'
    implementation 'com.google.firebase:firebase-database:11.0.4'

# write in Row, 寫入資料

      1. policy to retrieve (建立私有變數容器)

      2. retrieve the DB obj, then retrieve the reference of obj.

      3. ref location || k/v reference

      4. write in data
      
# code
      
    import pyrebase
    import GooPy
    import pyrebase

    config = {
      "apiKey": "AIzaSyClr4KhSkUVy0kMipcXCYMCMpDCFgBEXKY",
      "authDomain": "pattys-goopy-1527579295440.firebaseapp.com",
      "databaseURL": "https://pattys-goopy-1527579295440.firebaseio.com",
      "storageBucket": "pattys-goopy-1527579295440.appspot.com",
      "messagingSenderId": "557738520788"
    }

    firebase = pyrebase.initialize_app(config)

    db = firebase.database()
    db.child("users").child("Pattys Lab")

    data = {"distance":GooPy.distances}
    db.child("How far now").push(data)

# import & export, 資料匯出入

  https://pattyappier.blog/2018/06/01/goopy-firpy-2-google-apis-with-python/#more-1286
  
   https://gist.githubusercontent.com/PattyAppier/d335be50c761ea5914806fd1104689ff/raw/f086cb973bd95016dc9dd78d6244a5c56da4f35d/FirPy.py

