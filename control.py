
#連線DB
from dbConfig import conn, cur
def getShopList():
    #查詢
    sql="select id, name,price,stock from shoplist order by id asc;"
    cur.execute(sql)
    records = cur.fetchall()
    return records

def getMyList():
    #查詢
    sql="select id, name,price,amount from mylist order by id asc;"
    cur.execute(sql)
    records = cur.fetchall()
    return records
    
def removeFromCart(id):
    sql="UPDATE `mylist` SET `amount`= amount-1 WHERE id=%s and amount != 0;"
    cur.execute(sql,(id,))
    conn.commit()
    return True

def addIntoCart(id):
    if (stock != 0):
        sql="UPDATE `mylist` SET `amount`= amount+1 WHERE id=%s;"
        cur.execute(sql,(id,))
        conn.commit()
        return True
        

def updateStock1(id):
    sql="UPDATE `shoplist` SET `stock`= stock-1 WHERE id=%s;"
    cur.execute(sql,(id,))
    conn.commit()
    return True
    
def updateStock2(id):
    sql="UPDATE `shoplist` SET `stock`= stock+1 WHERE id=%s;"
    cur.execute(sql,(id,))
    conn.commit()
    return True