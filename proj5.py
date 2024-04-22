import mysql.connector
mydb=mysql.connector.connect(
  host="localhost",
  user="root",
  password=" ",
  database="my_database"
)
mycursor=mydb.cursor()

'''mycursor.execute("create table Emp(id int(10)primary key auto_increment,name varchar(120),address varchar(115),mail varchar(10),department varchar(100))")'''
print("Table cfreated successfully")

sql="insert into Emp(id,name,address,mail,phone,department) values(%s,%s,%s,%s,%s,%s)"
val=[
  ('',"Mr.Dev","Mungpoo","dev9980@gmail.com","2685419066","security"),
  ('',"Mrs.Roy","Sukna","roy886@gmail.com","3096158388","accounts"),
  ('',"Mr.Rohit","Darjeeling","rohit33876@gmail.com","7755248518","customercare"),
  ('',"Mr.Minj","Siliguri","minj2244@gmail.com","22851673890","sales"),
  ('',"Mr.Pradhan","Badamtam","pradhan9977@gmail.com","9907435411","finance"),
  ('',"Mrs.Subba","Lebong","subba7904@gmail.com","7908953856","electrical"),
]

'''mycursor.executemany(sql,val)
mydb.commit()
print(mycursor.rowcount,"row/s added successfully.")'''
'''mycursor.execute("select* from Emp")
result=mycursor.fetchall()
for t in result:
  print(t)'''

'''sql="update Emp set name=%s where name=%s"
val=("Mr.Rohit","Mr.Raj")
mycursor.execute(sql,val)
print(mycursor.rowcount,"row/s affected.")
'''