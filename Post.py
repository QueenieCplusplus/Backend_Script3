# 2019, 12/27, PM 9:35, by Queenie Chen
# 其實這文檔應該命名為 views.py 幫助路由找到

#注入套件如框架內的登入驗證和 render 渲染
#from django import forms
from 模組所在的資料夾目錄 import PostForm, models
import math # python 內建套件
from django.shortcut import render, redirect
from django.contrib.auth import authenticate
from django.contrib import auth

#先跳過作頁數的代碼實作
#這次先玩上傳的方法實作

def post(req): #當傳入上傳留言的事件參數時
    if req.method == "POST": #當方法為上傳時，方才執行如下
        pf = PostForm.PostForm() #建立留言板的物件
        if pf.is_valid(): #倘若通過驗證，則取得使用者上傳的輸入資料
            sub = pf.cleaned_data['commentSubject'] 
            nm = pf.cleaned_data['commentName']
            ml = pf.cleaned_data['commentMailAddr']
            ct = pf.cleaned_data['commentContent']

            #新增這筆上傳資料的紀錄
            data = models.CommentUnit.objects.create(
                cname=nm, csubject=sub, cmail = ml, ccontent = ct,
                cresponse=''
            )

            data.save() #存儲代表寫入資料庫

            msg = '儲存完成！'
            pf = PostForm.PostForm() #重新建立全新表單
            return redirect('/index')

        else:
            msg = '驗證錯誤，請重新嘗試。'
    
    else:
        msg = '請務必輸入主旨和郵件地址及內容'
        pf = PostForm.PostForm() #重新建立全新表單

    return render(request, "post.html", local()) #渲染畫面





