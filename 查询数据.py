import pymysql
db=pymysql.connect('localhost','root','w19891208','kairuide')
cursor=db.cursor()
sql='select * from b1'
try:
    cursor.execute(sql)
    # resultData=cursor.fetchall()
    # # print(resultData)
    # for i in resultData:
    #     print(i)
    row1=cursor.fetchone()
    print(row1)

except:
    db.rollback()

cursor.close()
db.close()