import psycopg2

connection = psycopg2.connect("dbname=learning_sql user=dbperson")
cursor = connection.cursor()

def search_player():
    for row in results:
        print(row)

def add_player():
    pass
    # full_name = "Tucker Cascadden"
    # position = "INF"
    # number = 17
    # avg = .268
    # hr = 0
    # rbi = 3
    # runs = 7

    # cursor.execute("INSERT INTO san_jacinto_baseball VALUES (%s, %s, %s, %s, %s, %s, %s);", (full_name, position, number, avg, hr, rbi, runs))  # fixture data


connection.commit()

# cursor.execute("select * from san_jacinto_baseball")
# results = cursor.fetchall()
# for row in results:
#     print(row)

cursor.close()
connection.close()







