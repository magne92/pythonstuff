import PySimpleGUI as sg
import mysql.connector
"""
  DESIGN PATTERN 2 - Multi-read window. Reads and updates fields in a window
"""

sg.theme('Dark Amber')    # Add some color for fun


mydb = mysql.connector.connect(
        user='root',
        password='',
        host='localhost',
        port='3306',
        database='cardb')

mycursor = mydb.cursor()


# 1- the layout
layout = [
         [sg.Text('Skriv inn din bils info under:')],
         [sg.Text('Merke :'), sg.Input(size=(21,1), key='-merke-'), sg.Text(size=(15,1), key='-omerke-')],
         [sg.Text('Modell :'), sg.Input(size=(21,1), key='-modell-'), sg.Text(size=(15,1), key='-omodell-')],
         [sg.Text('Årsmodell :'), sg.Input(size=(21,1), key='-års-'), sg.Text(size=(15,1), key='-oårs-')],
         [sg.Text('Reg. nummer :'), sg.Input(size=(21, 1), key='-reg-'), sg.Text(size=(15, 1), key='-oreg-')],
         [sg.Button('Legg til'), sg.Button('Exit')]
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
        # Update the "output" text element to be the value of "input" element

        sql = "INSERT INTO cars (merke, aarsmodell, regnr, modell) VALUES (%s, %s,%s, %s)"
        val = (values['-merke-'], values['-modell-'],values['-års-'],values['-reg-'])

        mycursor.execute(sql, val)
        mydb.commit()

# 4 - the close
mydb.close()
window.close()