import psycopg2

connection = psycopg2.connect("dbname=learning_sql user=dbperson")
cursor = connection.cursor()


def search_player_name():
    player_search = input('Search: ')
    cursor.execute("select * from san_jacinto_baseball WHERE full_name = %s;", (player_search,))
    results = cursor.fetchall()
    for row in results:
        print(row[0], "#", row[2])
        print("Pos.", row[1])
        print("AVG:", row[3])
        print("HR:", row[4])
        print("RBI:", row[5])
        print("Runs:", row[6])
    else:   # not quite right
        print("1  ! No Match !")
# search_player_name()


def search_query():
    print("Search by: 1. Full Name 2. Number 3. Position 4. Average etc....")
    search_num = input('# to search by: ')
    search_string = input("Search Criteria: ")
    if search_num == "1":
        search("full_name", search_string)
    elif search_num == "2":
        search("number", search_string)


def search_display(row):
    print(row[0], "#", row[2])
    print("Pos.", row[1])
    print("AVG:", row[3])
    print("HR:", row[4])
    print("RBI:", row[5])
    print("Runs:", row[6])


def search(stat, search_critera):
    cursor.execute("select * from san_jacinto_baseball WHERE {} = %s;".format(stat), (search_critera,))
    results = cursor.fetchall()
    for row in results:
        # return row
        print(row[0], "#", row[2])
        print("Pos.", row[1])
        print("AVG:", row[3])
        print("HR:", row[4])
        print("RBI:", row[5])
        print("Runs:", row[6])
    else:
        print("2 ! No Match !")


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

search_query()

cursor.close()
connection.close()






