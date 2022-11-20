#!C:\Users\tommy\AppData\Local\Programs\Python\Python310\python.exe
#-*- coding: utf-8 -*-
#處理stdio輸出編碼，以避免亂碼
import codecs, sys 
sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)
import cgi
import control as ctrl
#連線DB
from dbConfig import conn, cur
#先印出http 表頭
print("Content-Type: text/html; charset=utf-8\n")
print("""
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>結帳</title>
</head>
<body>
""")
total = 0
discount = 0
records = ctrl.getMyList()

for(id,name,price,amount) in records:
    total += price*amount
if total >= 1000:
    discount = total*0.8
else: 
    discount = total * 0.9
ctrl.updateStock1(id,amount)

ctrl.cleanCart()
    
print(f"<p>總價：{total}</p>")
print(f"<p>打折後：{discount}</p>")
print("<a href='myCart.py'>回購物車</a>")
print("</body></html>")