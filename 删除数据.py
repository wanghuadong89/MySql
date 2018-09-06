import pymysql
db=pymysql.connect('localhost','root','w19891208','kairuide')
cursor=db.cursor()
sql='delete from b3 WHERE id=3'
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
