import datetime as time
import sqlite3
conn = sqlite3.connect('main.db')
c = conn.cursor()

now = time.datetime.now()
hour = now.hour
if hour < 12:
    print("Good morning")
elif hour > 12 and hour < 18:
    print("Good afternoon")
elif hour > 18 and hour < 19:
    print("Good evening")
else:
    print('Good night.')
for i in range(3):
        username = input("PLS enter your username: ")
        password = input("PLS enter your password: ")
        with sqlite3.connect('main.db') as db:
            cursour = db.cursor()
        find_user = ('SELECT * FROM login WHERE username = ? AND password = ?')
        cursour.execute(find_user,[(username), (password)])
        results = cursour.fetchall()
        
        if results:
            for i in results:
                buda = str(i)
                print("Welcome " +buda)
                def what_to_do_logic():
                    asking = input("""
                    What do you want to do:
                    a. Enter mew resident
                    b. View all Quali Estate residents
                    c. Exit system 
                    Enter your choice: 
                    """)
                    if asking == "a." or asking == "A." or asking == "a" or asking == "A":
                        def adding_new_resident():
                            asking2 = input("Enter new resident first name:  ")
                            asking1 = input("Enter new resident second name:  ")
                            c.execute('CREATE TABLE IF NOT EXISTS name_of_resident(fName TEXT, sName TEXT)')
                            c.execute('INSERT INTO name_of_resident(fName, sName) VALUES(?, ?)',(asking2, asking1))
                            conn.commit()
                            repeat = input("Do you want to add another resident? Yes(Y) or No(N): ")
                            if repeat == "Y" or repeat == "y":
                                adding_new_resident()
                            elif repeat == "N" or repeat == "n":
                                what_to_do_logic()
                            else:
                                print("You have inputed the wrong input")
                                adding_new_resident()

                        adding_new_resident()
                    elif asking == "b." or asking == "B." or asking == "b" or asking == "B":
                        c.execute('SELECT * FROM name_of_resident')
                        data = c.fetchall()
                        for dub in data:
                            print(dub)
                        def d_input():
                            d = input("Press e/E to go back to what to do:  ")
                            if d == "e" or d == "E  ":
                                what_to_do_logic()
                            else:
                                print("You have inputed the wrong input")
                                d_input()
                        d_input()

                    elif asking == "C." or asking == "c." or asking == "c" or asking == "C":
                        print("Good Bye. Thankyou "+ username)
                    else:
                        print("You did not put the write input above. Please try again.")
                        what_to_do_logic()    
                what_to_do_logic()
#            return('exist')
            break
        else:
            print("Username and password are not recognised")
            again = input("Do u want to try again?(y/n): ")
            if again.lower() == "n":
                print("Good Bye")
                time.sleep(1)
#                return('exit')
                break       
                