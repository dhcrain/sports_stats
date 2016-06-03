# ! ALL use of "{}".format() is hard coded and not available for user input !!!!!

import psycopg2

connection = psycopg2.connect("dbname=learning_sql user=dbperson")
cursor = connection.cursor()

print("\nWelcome to San Jacinto Baseball Stats")


def welcome():
    print("\nWhat would you like to do?")
    choice = input("1. Search for a player\n2. Add a Player\n3. Update Player\n4. Show All\n5. Exit ")
    options = {"1": search_query, "2": add_player, "3": update_player, "4": show_all, "5": exit}
    if choice not in "1234":
        print(" ! Not a valid choice ! \n")
    else:
        options[choice]()

    welcome()


def search_query():
    print("\nSearch by:\n"
          "1. Full Name\n"
          "2. Number\n"
          "3. Position\n"
          "4. Average\n"
          "5. HR\n"
          "6. RBI\n"
          "7. Runs")
    search_num = input('What would you like to search by: ')
    search_string = input("Search Criteria: ")
    sq_options = {"1": "full_name",
                  "2": "number",
                  "3": "position",
                  "4": "avg",
                  "5": "hr",
                  "6": "rbi",
                  "7": "runs"}
    if search_num not in "13":
        print("Would you like you search to be:")
        operator = input("1. Exact match\n"
                         "2. Less Than\n"
                         "3. Greater Than")
        op_choice = {"1": "=", "2": "<", "3": ">"}
        search(sq_options[search_num], op_choice[operator], search_string)
    else:
        search(sq_options[search_num], "=", search_string)
    if input("Would you like to edit this player? Y/n").lower() != "n"
        edit_palyer(search_string)
    else:
        welcome()
    return search_string


def search(stat, operator, search_critera):
    cursor.execute("select * from san_jacinto_baseball WHERE {} {} %s;".format(stat, operator), (search_critera,))
    results = cursor.fetchall()
    for row in results:
        search_display(row)
    else:   # funky, always displays.....
        print("2 ! No Match !")
    return search_critera


def search_display(player):
    print("-"*25)
    print(player[0], "#", player[2])
    print("Pos.", player[1])
    print("AVG:", player[3])
    print("HR:", player[4])
    print("RBI:", player[5])
    print("Runs:", player[6])


def update_player():
    return input("Which player to update? (Full Name): ")


def edit_palyer(name):
    search("full_name", "=", name)
    update_num = input("\nWhat stat update? \n"
                       "1. Full Name\n"
                       "2. Number\n"
                       "3. Position\n"
                       "4. Average\n"
                       "5. HR\n"
                       "6. RBI\n"
                       "7. Runs ")
    update_options = {"1": "full_name",
                      "2": "number",
                      "3": "position",
                      "4": "avg",
                      "5": "hr",
                      "6": "rbi",
                      "7": "runs"}
    new_value = input("What is the new value? ")
    cursor.execute("UPDATE san_jacinto_baseball SET {} = %s WHERE full_name = %s;".format(update_options[update_num]), (new_value, name))
    connection.commit()
    print(" * Player Updated *")
    search("full_name", "=", name)
    welcome()


def add_player():
    print("\nEnter new player information")
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


def show_all():
    cursor.execute("select * from san_jacinto_baseball")
    results = cursor.fetchall()
    for row in results:
        search_display(row)

connection.commit()


welcome()
# update_player()

cursor.close()
connection.close()
