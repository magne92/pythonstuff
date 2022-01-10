import PySimpleGUI as sg

# Design pattern 2 - First window remains active

def win1_layout():
    layout = [[ sg.Text('Window 1'),],
            [sg.Input(do_not_clear=True)],
            [sg.Text(size=(15,1), key='-OUTPUT-')],
            [sg.Button('Launch 2'), sg.Button('Exit')]]

    return layout

def win2_layout():
    layout = [[sg.Text('Window 2')],
              [sg.Input(do_not_clear=True)],
              [sg.Button('Exit')]]

    return layout

win1 = sg.Window('Window 1', win1_layout())

win2_active = False
while True:
    ev1, vals1 = win1.read(timeout=100)
    win1['-OUTPUT-'].update(vals1[0])
    if ev1 == sg.WIN_CLOSED or ev1 == 'Exit':
        break

    if not win2_active and ev1 == 'Launch 2':
        win2_active = True
        #win1.Hide()  # fjern hashtag for å skjule window 1 når window 2 skal vises
        win2 = sg.Window('Window 2', win2_layout())

    if win2_active:
        ev2, vals2 = win2.read(timeout=100)
        if ev2 == sg.WIN_CLOSED or ev2 == 'Exit':
            win2_active  = False
            #win1.UnHide()   # fjern hashtag for å vise window 1 igjen
            win2.close()

