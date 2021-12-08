import mysql.connector
import PySimpleGUI as sg
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="carreg"
)

mycursor = mydb.cursor()
sql = "SELECT regid, brand, model, year FROM car"
mycursor.execute(sql)
myresult = mycursor.fetchall()



clayout = [
    [sg.Table(values=myresult,
              key='_CARS_',
              headings=['Regnr', 'brand', 'model', 'year'],
              max_col_width=25,
              auto_size_columns=True,)
              #justification='right',
              # alternating_row_color='lightblue',
              #num_rows=min(len(data), 20))

     ],
    [sg.Button('Update'), sg.Button('Exit')]
]
window = sg.Window('Tittel på programmer', clayout)

event, values = window.read()
print(event, values)