import MySQLdb as sql

db = sql.connect('localhost','root','root','college')

cursor = db.cursor()


no_of_rows = cursor.execute("""select * from students""")
#cursor.execute("""insert into students values(21,'John cena')""")
#cursor.execute("""delete from students where ID=52""")

for i in range(no_of_rows):
     print(i)

db.commit()
db.close()




