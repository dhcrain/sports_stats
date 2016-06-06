# ! ALL use of "{}".format() is hard coded and not available for user input !!!!!

import psycopg2

connection = psycopg2.connect("dbname=learning_sql user=dbperson")
cursor = connection.cursor()

print("\nWelcome to San Jacinto Baseball Stats")


def welcome():
    print("\nWhat would you like to do?")
    choice = input("1. Search for a player\n2. Add a Player\n3. Update Player\n4. See Top Players\n5. Show All\n6. Exit ")
    options = {"1": search_query,
               "2": add_player,
               "3": update_player,
               "4": top_players,
               "5": show_all,
               "6": exit}
    if choice not in "123456":
        print(" ! Not a valid choice ! \n")
    else:
        options[choice]()

    welcome()


def search_query():
    print("\nSearch by:\n1. Full Name\n2. Number\n3. Position\n4. Average\n5. HR\n6. RBI\n7. Runs")
    search_num = input('What would you like to search by: ')
    sq_options = {"1": "full_name",
                  "2": "number",
                  "3": "position",
                  "4": "avg",
                  "5": "hr",
                  "6": "rbi",
                  "7": "runs"}
    search_string = input("Search Criteria: ")
    if search_num not in "13":
        print("Would you like you search to be:")
        operator = input("1. Exact match\n"
                         "2. Less Than\n"
                         "3. Greater Than ")
        op_choice = {"1": "=", "2": "<", "3": ">"}
        search(sq_options[search_num], op_choice[operator], search_string)
    else:
        search(sq_options[search_num], "=", search_string)
    return search_string


def search(stat, operator, search_critera):
    cursor.execute("select * from san_jacinto_baseball WHERE {} {} %s;".format(stat, operator), (search_critera,))
    results = cursor.fetchall()
    if results == []:  # only way I could get it to work.
        if input("\n ! No Match !\nWould you like to add a player? Y/n ").lower() != "n":
            add_player()
        else:
            welcome()
    else:
        display_header()
        for row in results:
            search_display(row)
    return search_critera


def display_header():
    titles = ["Name", "#", "POS", "AVG", "HR", "RBI", "R"]
    print("{:^30}|{:^4}|{:^7}|{:^6}|{:^4}|{:^4}|{:^4}".format(titles[0], titles[1], titles[2], titles[3],
                                                              titles[4], titles[5], titles[6]))
    print("-" * 29, "+", "-" * 2, "+", "-" * 5, "+", "-" * 4, "+", "-" * 2, "+", "-" * 2, "+", "-" * 3)


def search_display(player):
    print("{:^30}|{:>4}|{:^7}|{:>6.3f}|{:>4}|{:>4}|{:>4}".format(player[0], player[2], player[1], player[3], player[4], player[5], player[6]))


def update_player():
    name = input("Which player to update? (Full Name): ")
    edit_palyer(name)


def edit_palyer(name):
    search("full_name", "=", name)
    update_num = input("\nWhat stat to update? \n1. Full Name\n2. Number\n3. Position\n4. Average\n5. HR\n6. RBI\n7. Runs ")
    update_options = {"1": "full_name",
                      "2": "number",
                      "3": "position",
                      "4": "avg",
                      "5": "hr",
                      "6": "rbi",
                      "7": "runs"}
    new_value = input("What is the new value? ")
    try:
        cursor.execute("UPDATE san_jacinto_baseball SET {} = %s WHERE full_name = %s;".format(update_options[update_num]), (new_value, name))
        connection.commit()
        print("\n * Player Updated *")
        search("full_name", "=", name)
        if input("Edit additional stats for this player? Y/n").lower() != "n":
            edit_palyer(name)
        else:
            welcome()
    except psycopg2.DataError:
        print(" ! Value too long for field, please try again. !")
        edit_palyer(name)


def add_player():
    print("\nEnter new player information (Max chars)")
    full_name = input("Full Name(30): ")
    position = input("Position(6) (ex.INF): ").upper()
    number = int(input("Number(2): "))
    avg = float(input("Batting Average(4): "))
    hr = int(input("HR(2): "))
    rbi = int(input("RBI(2): "))
    runs = int(input("Runs(2): "))
    try:
        cursor.execute("INSERT INTO san_jacinto_baseball VALUES (%s, %s, %s, %s, %s, %s, %s);", (
            full_name, position, number, avg, hr, rbi, runs))
        connection.commit()
        print("\n * Player Successfully Added *")
        search("full_name", "=", full_name)     # (string, oper, variable)
    except psycopg2.DataError:
        print(" ! Value too long for field, please try again. !")
        add_player()


def show_all():
    cursor.execute("select * from san_jacinto_baseball")
    results = cursor.fetchall()
    display_header()
    for row in results:
        search_display(row)


def top_players():
    print("\nSee the top 5 for?")
    top_choice = input("1. AVG\n2. HR\n3. RBI\n4. Runs ")
    top_options = {"1": "avg",
                   "2": "hr",
                   "3": "rbi",
                   "4": "runs"}
    cursor.execute("SELECT * FROM san_jacinto_baseball ORDER BY {} DESC;".format(top_options[top_choice]))
    results = cursor.fetchmany(5)
    display_header()
    for row in results:
        search_display(row)
    welcome()

connection.commit()

welcome()

cursor.close()
connection.close()
