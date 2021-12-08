import PySimpleGUI as sg
import mysql.connector
"""
  DESIGN PATTERN 2 - Multi-read window. Reads and updates fields in a window
"""

sg.theme('Dark Amber')    # Add some color for fun

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    passwd="",
    database="carreg"
)

databasepeker = mydb.cursor()

# 1- the layout
layout = [
         [sg.Text('Skriv inn din bils info under:')],
         [sg.Text('Merke :'), sg.Input(size=(21,1), key='-merke-'), sg.Text(size=(15,1), key='-omerke-')],
         [sg.Text('Modell :'), sg.Input(size=(21,1), key='-modell-'), sg.Text(size=(15,1), key='-omodell-')],
         [sg.Text('Årsmodell :'), sg.Input(size=(21,1), key='-års-'), sg.Text(size=(15,1), key='-oårs-')],
         [sg.Text('Reg. nummer :'), sg.Input(size=(21, 1), key='-reg-'), sg.Text(size=(15, 1), key='-oreg-')],
         [sg.Text('Eier:'), sg.Input(size=(21, 1), key='-owner-'), sg.Text(size=(15, 1), key='-oowner-')],
         [sg.Button('Legg til'), sg.Button('Exit')],
         [sg.Button('Vis alle biler')]
]

# 2 - the window
window = sg.Window('Bil info', layout)


# 3 - the event loop
while True:
    event, values = window.read()
    print(event, values)
    if event in (None, 'Exit'):
        break
    if event == 'Legg til':

        merke = values['-merke-']
        modell = values['-modell-']
        aars = values['-års-']
        regnr = values['-reg-']
        owner = values['-owner-']

        sql = "INSERT INTO car(regid, brand, model, year, owner) VALUES (%s, %s, %s, %s, %s)"
        val = (regnr, merke, modell, aars, owner)
        databasepeker.execute(sql, val)
        mydb.commit()

        sg.popup('The car was added to the database')

    if event == 'Vis alle biler':
        sql = "SELECT regid, brand, model, year, username FROM car JOIN users ON car.owner=users.userid"
        databasepeker.execute(sql)
        bilresultat = databasepeker.fetchall()

        carlayout = [
            [sg.Table(values=bilresultat,
                      key='_CARS_',
                      headings=['Regnr', 'brand', 'model', 'year', 'Owner'],
                      max_col_width=25,
                      auto_size_columns=True,
                      justification='left', )
             # alternating_row_color='lightblue',
             # num_rows=min(len(data), 20))
             ]

        ]

        carwindow = sg.Window('All cars', carlayout)
        event, values = carwindow.read()


# 4 - the close

window.close()