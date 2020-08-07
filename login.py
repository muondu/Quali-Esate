import sqlite3
conn = sqlite3.connect('main.db') 
cursour = conn.cursor()
    
cursour.execute("CREATE TABLE IF NOT EXISTS login(username VARCHAR, password VARCHAR)")

cursour.execute("INSERT INTO login VALUES('Nesh', '12')")
                
cursour.execute("INSERT INTO login VALUES('Malli', '258')")
conn.commit()
                

