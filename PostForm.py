# 2019, 12/27, PM 9:30, by Queenie Chen
# 主要運用 forms 套件

from django import forms
from captcha.fields import CaptchaField

class PostForm(forms.Form):
    
    #圖形驗證碼，其屬性尚有大小，英文數字和圖案，逾時的方法
    captcha = CaptchaField()

    #留言板物件的各種屬性設定
    commentSubject = forms.CharField(max_length=100, initial='')
    commentName = forms.CharField(max_length=20, initial='')
    commentMailAddr = forms.EmailField(max_length=100, initial='', required=False)
    commentContent = forms.CharField(widget=forms.Textarea)





