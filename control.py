
#連線DB
from dbConfig import conn, cur
def getShopList():
    #查詢購物列表(顧客端)
    sql="select id, name,price,stock from shoplist where stock != 0 order by id asc ;"
    cur.execute(sql)
    records = cur.fetchall()
    return records
    
def getShopListAdmin():
    #查詢購物列表(管理端)
    sql="select id, name,price,stock from shoplist order by id asc ;"
    cur.execute(sql)
    records = cur.fetchall()
    return records    

def getMyList():
    #查詢客戶的購物車
    sql="select id, name,price,amount from mylist order by id asc;"
    cur.execute(sql)
    records = cur.fetchall()
    return records
    
def removeFromCart(id,amount):
    #從購物車中拿出，已經是0的不會有反應
    if amount!=0:
        sql="UPDATE `mylist` SET `amount`= amount-%s WHERE id=%s;"
        cur.execute(sql,(amount,id))
        conn.commit()
        return True

def addIntoCart(id,amount):
    #加入購物車
    sql="UPDATE `mylist` SET `amount`= amount+%s WHERE id=%s;"
    cur.execute(sql,(amount,id))
    conn.commit()
    return True

def updateStock1(id,amount):
    #放入購物車後，購物列表存貨更新
    sql="UPDATE `shoplist` SET `stock`= stock-%s WHERE id=%s;"
    cur.execute(sql,(amount,id))
    conn.commit()
    return True
    
def updateStock2(id,amount):
    #拿出購物車後，購物列表存貨更新
    sql="UPDATE `shoplist` SET `stock`= stock+%s WHERE id=%s;"
    cur.execute(sql,(amount,id))
    conn.commit()
    return True
    
def addStock(id,stock):
    #進貨
    sql="UPDATE `shoplist` SET `stock`= stock+%s WHERE id=%s;"
    cur.execute(sql,(stock,id))
    conn.commit()
    return True

def addGoodInShopList(name,price,stock):
    #增加商品項目(商品列表)
    sql="insert into shoplist (name,price,stock) values (%s,%s,%s);"
    cur.execute(sql,(name,price,stock))
    conn.commit()
    return True

def addGoodInCart(name,price):
    #增加商品項目(商品列表)
    sql="insert into mylist (name,price) values (%s,%s);"
    cur.execute(sql,(name,price))
    conn.commit()
    return True

def removeGood1(id):
    #移除商品項目
    sql="DELETE FROM `shoplist` WHERE id = %s;"
    cur.execute(sql,(id,))
    conn.commit()
    return True
    
def removeGood2(id):
    #移除商品項目
    sql="DELETE FROM `mylist` WHERE id = %s;"
    cur.execute(sql,(id,))
    conn.commit()
    return True