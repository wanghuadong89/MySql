import pymysql
db=pymysql.connect('localhost','root','w19891208','kairuide')
cursor=db.cursor()
sql='select version()'
cursor.execute(sql)
data=cursor.fetchone()
print(data)
cursor.close()
db.close()