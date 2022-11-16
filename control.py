
#連線DB
from dbConfig import conn, cur
def getShopList():
    #查詢購物列表
    sql="select id, name,price,stock from shoplist order by id asc;"
    cur.execute(sql)
    records = cur.fetchall()
    return records

def getMyList():
    #查詢我的購物車
    sql="select id, name,price,amount from mylist order by id asc;"
    cur.execute(sql)
    records = cur.fetchall()
    return records
    
def removeFromCart(id):
    #從購物車中拿出，已經是0的不會有反應
    sql="UPDATE `mylist` SET `amount`= amount-1 WHERE id=%s and amount != 0;"
    cur.execute(sql,(id,))
    conn.commit()
    return True

def addIntoCart(id):
    #加入購物車
    sql="UPDATE `mylist` SET `amount`= amount+1 WHERE id=%s and stock != 0;"
    cur.execute(sql,(id,))
    conn.commit()
    return True

def updateStock1(id):
    #加入購物車後，購物列表存貨更新
    sql="UPDATE `shoplist` SET `stock`= stock-1 WHERE id=%s;"
    cur.execute(sql,(id,))
    conn.commit()
    return True
    
def updateStock2(id):
    #加入購物車後，我的購物車更新
    sql="UPDATE `shoplist` SET `stock`= stock+1 WHERE id=%s;"
    cur.execute(sql,(id,))
    conn.commit()
    return True
    
def addStock(id,stock):
    #進貨
    sql="UPDATE `shoplist` SET `stock`= stock+%s WHERE id=%s;"
    cur.execute(sql,(id,stock))
    conn.commit()
    return True

def addGood(name,price,stock):
    #增加商品項目
    sql="insert into shoplist (name,price,stock) values (%s,%s,%s);"
    cur.execute(sql,(name,price,stock))
    conn.commit()
    return True

def removeGood(id):
    #移除商品項目
    sql="DELETE FROM `shoplist` WHERE id = %s;"
    cur.execute(sql,(id,))
    conn.commit()
    return True