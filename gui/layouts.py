import PySimpleGUI as sg

def mainlayout():
    mlayout = [
        [sg.Button('Show cars')],
        [sg.Button('Registration')],
        [sg.Button('My cars')],
        [sg.Text('', key='_OUTPUT_')],
        [sg.Button('Logout', bind_return_key=True)]
    ]
    return mlayout

def regilayout():
    rlayout = [
        [sg.Text('Enter car information.')],
        [sg.Text('Registration number')],
        [sg.InputText(key='-reg-')],
        [sg.Text('Brand')],
        [sg.InputText(key='-brand-')],
        [sg.Text('Model')],
        [sg.InputText(key='-model-')],
        [sg.Text('Year')],
        [sg.InputText(key='-year-')],
        [sg.Text('Owner ID')],
        [sg.InputText(key='-ownerid-')],
        [sg.Button('Submit', bind_return_key=True), sg.Button('Exit')]
    ]
    return rlayout

def carlayout(data):
    clayout = [
    [sg.Table(values=data,
              key='_CARS_',
              headings=['Regnr', 'brand', 'model', 'year', 'owner'],
              max_col_width=25,
              auto_size_columns=True,
              justification='left',)
              #alternating_row_color='lightblue',
              #num_rows=min(len(data), 20))
         ],
    [sg.Button('Update'), sg.Button('Exit')] ]
    return clayout

def mycarlayout(data):
    clayout = [
    [sg.Table(values=data,
              key='_CARS_',
              headings=['Regnr', 'regid', 'brand', 'model', 'year'],
              max_col_width=25,
              auto_size_columns=True,)
              #justification='right',
              # alternating_row_color='lightblue',
              #num_rows=min(len(data), 20))
         ],
    [sg.Button('Exit')] ]
    return clayout

def loginlayout():
    llayout = [
        [sg.Text('LOGIN')],
        [sg.InputText(key='-username-')],
        [sg.InputText(key='-password-')],
        [sg.Button('Login', bind_return_key=True), sg.Button('Exitprogram')]]
    return llayout

def dbconnect():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="carreg"
    )
    mycursor = mydb.cursor()
    return mycursor

#def loginwindow():

    #return loginstate
#