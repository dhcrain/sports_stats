import psycopg2

# scafolding - start fresh everytime

connection = psycopg2.connect("dbname=learning_sql user=dbperson")
cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS san_jacinto_baseball;")

table_create = """CREATE TABLE san_jacinto_baseball (
  full_name varchar(30),
  position varchar(6),
  number numeric(2),
  avg float(4),
  hr numeric(2),
  rbi numeric(2),
  runs numeric(2)
);"""

cursor.execute(table_create)

# http://stats.njcaa.org/sports/bsb/2015-16/div1/teams/sanjacintocollegenorth?view=lineup
cursor.execute("INSERT INTO san_jacinto_baseball VALUES"
               "('Tucker Cascadden', 'INF', 17, .268, 0, 3, 7),"
               "('Max Wood', 'OF', 33, .378, 7, 48, 42),"
               "('Aaron Bond', 'OF', 16, .348, 8, 22, 20),"
               "('Devin Wilson', 'INF', 12, .125, 0, 2, 2),"
               "('Chris Roberts', 'OF/RHP', 34, .200, 0, 0, 3),"
               "('Brandon Montgomery', 'INF', 7, .385, 6, 40, 40),"
               "('Donivan Lopez', 'INF/OF', 20, .346, 0, 35, 37),"
               "('Ryan January', 'C/OF', 8, .351, 10, 45, 45),"
               "('Liam Scafariello', 'INF/OF', 44, .314, 11, 33, 34),"
               "('Baine Schoenvogel', 'C/RHP', 10, .390, 2, 24, 22);")


connection.commit()

# cursor.execute("select * from san_jacinto_baseball")
# results = cursor.fetchall()
# for row in results:
#     print(row)

cursor.close()
connection.close()







