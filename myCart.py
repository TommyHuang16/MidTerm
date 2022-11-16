#!C:\Users\tommy\AppData\Local\Programs\Python\Python310\python.exe
# -*- coding: utf-8 -*-
# 處理stdio輸出編碼，以避免亂碼
import codecs, sys 
sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)
import cgi
import control as ctrl
#連線DB
from dbConfig import conn, cur

print("Content-Type: text/html; charset=utf-8\n")
print("""
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>我的購物車</title>
</head>
<body>
<form method="post" action="removeFromCart.py">
輸入要拿出的商品ID: <input type='text' name='i'><input type='submit'>
</form> <br>
</body>
""")

records = ctrl.getMyList()
for (id,name,price,amount) in records:
	print(f"<p>ID:{id} 名稱:{name} 價格:{price} 數量:{amount}</p>")
print("<a href='menu.py'>回商品列表</a>")
print("<br><a href='結帳.py'>結帳</a>")
print("</body></html>")