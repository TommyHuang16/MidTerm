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
<title>管理端首頁</title>
</head>
<body>
<p>歡迎，Admin! 以下為目前的商品清單~</p>
""")
records = ctrl.getShopListAdmin()
for (id,name,price,stock) in records:
	print(f"<p>ID:{id} 名稱:{name} 價格:{price} 庫存:{stock}</p> ")

print("<p><a href='edit.html'> 貨品編輯 </a></p>")
print("<p><a href='addStock.html'> 增加存貨 </a></p>")
print("<p><a href='addGood.html'> 新增商品項目 </a></p>")
print("<p><a href='removeGood.html'> 移除商品項目 </a></p>")

print("</body></html>")