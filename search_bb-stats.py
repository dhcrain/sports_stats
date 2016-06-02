import psycopg2

connection = psycopg2.connect("dbname=learning_sql user=dbperson")
cursor = connection.cursor()

def search_player_name():
    search = input('Search: ')
    cursor.execute("select * from san_jacinto_baseball WHERE full_name = %s;", (search,))
    results = cursor.fetchall()
    for row in results:
        print(row[0], "#", row[2])
        print("Pos.", row[1])
        print("AVG:", row[3])
        print("HR:", row[4])
        print("RBI:", row[5])
        print("Runs:", row[6])
    else:
        print(" ! No Match !")
search_player_name()


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







