import pymysql
db=pymysql.connect('localhost','root','w19891208','kairuide')
cursor=db.cursor()
sql='update b3 set name="G" WHERE id =4'
try:
    cursor.execute(sql);
    db.commit()
except:
    db.rollback()
cursor.close()
db.close()