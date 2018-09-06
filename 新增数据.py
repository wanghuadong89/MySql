import pymysql
db=pymysql.connect('localhost','root','w19891208','kairuide')
cursor=db.cursor()
sql='insert into b3 VALUES (0,"C"),(0,"e")'
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
cursor.close()
db.close()