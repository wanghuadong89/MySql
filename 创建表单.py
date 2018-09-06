import pymysql
db=pymysql.connect('localhost','root','w19891208','kairuide')
cursor=db.cursor()
sql='create table b3 (id int auto_increment primary key,name varchar(50)unique  not null)'
cursor.execute(sql)
cursor.close()
db.close()