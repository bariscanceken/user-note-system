#Libraries
import sqlite3
import tkinter
import os

#Os
base_dir = os.path.dirname(os.path.abspath(__file__))
path_database = os.path.join(base_dir, 'userdatas.db')

#Connection
connect = sqlite3.connect(path_database)
query = connect.cursor()

#Value Adding
#query.execute("INSERT INTO users (birth_date, first_name, last_name, gender, register_date) VALUES ('2003-01-15', 'Barışcan', 'Çeken', 'M', '2025-01-01')")
#query.execute("INSERT INTO contact_details (user_id, contact_id, email, phone) VALUES (1 , 1 , 'bariscanceken@hotmail.com' , '05305792936')")
#query.execute("INSERT INTO notes (user_id , username , note_id  , note , level_importance ) VALUES (1,'bariscan',1,'Merhaba arkadaşlar hoşgeldiniz :)',1)")
#query.execute("INSERT INTO login (user_id , username , password ) VALUES (1,'bariscan','123456789')")
#connect.commit()
#^-- It has been committed so an error will be received 

#tkinter
window = tkinter.Tk()
window.title("User Note System")
text_username = tkinter.Label(text="Enter Your User Name: ")
text_username.pack()
input_username = tkinter.Entry(width=20)
input_username.pack()
text_password = tkinter.Label(text="Enter Your Password: ")
text_password.pack()
input_password = tkinter.Entry(width=20)
input_password.pack()

#Login Function Way 1
'''
def hello():
    username = []
    password = []

    for i in query.execute('SELECT user_id FROM login WHERE username = ?', (input_username.get() , )):
        username.append(i)
        print(username)

    for i in query.execute('SELECT user_id FROM login WHERE password = ?', (input_password.get() , )):
        password.append(i)

    if username == password:
        try :
            if username[0] == password[0]:
                print("you are in!")
        except : 
            print("Username and Password Incorrect.")
    else:
        print("Username or Password Incorrect")
'''

#Login Function Way 2
def hello():
    logindata = []

    for i in query.execute(f'SELECT username FROM login WHERE username = ? and password = ?',(input_username.get(),input_password.get())):
            logindata.append(i)

    try : 
        print(logindata[0])
        print("Welcome!")
    except : 
        print("Username or password is incorrect!")

#Buttons
button_login = tkinter.Button(text="Enter",command=hello)
button_login.pack()
button_register = tkinter.Button(text="Register")
button_register.pack()

window.mainloop()