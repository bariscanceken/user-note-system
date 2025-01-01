#Libraries
import sqlite3
import os

#Os
base_dir = os.path.dirname(os.path.abspath(__file__))
path_database = os.path.join(base_dir, 'userdatas.db')

#Connection
connect = sqlite3.connect(path_database)
query = connect.cursor()

#Value Adding
query.execute("INSERT INTO users (birth_date, first_name, last_name, gender, register_date) VALUES ('2003-01-15', 'Barışcan', 'Çeken', 'M', '2025-01-01')")
query.execute("INSERT INTO contact_details (user_id, contact_id, email, phone) VALUES (1 , 1 , 'bariscanceken@hotmail.com' , '05305792936')")
query.execute("INSERT INTO notes (note_id , user_id , note , level_importance ) VALUES (1,1,'Merhaba arkadaşlar hoşgeldiniz :)',1)")

#Value Printing
query.execute('select * from notes')
for i in query:
    print(i)
