import psycopg2

connection = psycopg2.connect("dbname=learning_sql user=dbperson")
cursor = connection.cursor()


# Not Needed? redundat to search()?
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


def search_query():
    print("Search by:\n1.Full Name 2.Number 3.Position 4.Average 5.HR 6.RBI 7.Runs")
    search_num = input('# to search by: ')
    search_string = input("Search Criteria: ")
    if search_num == "1":
        search("full_name", search_string)
    elif search_num == "2":
        search("number", search_string)
    elif search_num == "3":
        search("position", search_string)
    elif search_num == "4":
        search("avg", search_string)
    elif search_num == "5":
        search("hr", search_string)
    elif search_num == "6":
        search("rbi", search_string)
    elif search_num == "7":
        search("runs", search_string)

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
        search_display(row)
        print(row[0], "#", row[2])
        print("Pos.", row[1])
        print("AVG:", row[3])
        print("HR:", row[4])
        print("RBI:", row[5])
        print("Runs:", row[6])
    else:   # funky
        print("2 ! No Match !")


def add_player():
    print("Enter new player information")
    full_name = input("Full Name: ")
    position = input("Position (ex.INF): ").upper()
    number = int(input("Number: "))
    avg = float(input("Batting Average: "))
    hr = int(input("HR: "))
    rbi = int(input("RBI: "))
    runs = int(input("Runs: "))

    cursor.execute("INSERT INTO san_jacinto_baseball VALUES (%s, %s, %s, %s, %s, %s, %s);", (
        full_name, position, number, avg, hr, rbi, runs))
    connection.commit()
    print(" * Player Successfully Added *")

connection.commit()

# cursor.execute("select * from san_jacinto_baseball")
# results = cursor.fetchall()
# for row in results:
#     print(row)

# search_query()
add_player()

cursor.close()
connection.close()





