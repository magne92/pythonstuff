import PySimpleGUI as sg

sg.theme('BluePurple')

layout = [
        [sg.Text('Det du skriv kommer opp her:'), sg.Text(size=(15, 1), key='-OUTPUT-')],
        [sg.Input(key='-IN-')],
        [sg.Button('Show'), sg.Button('Exit')]
]

window = sg.Window('Tittel på programmer', layout)

while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if event in (None, 'Exit'):
        break
    if event == 'Show':
        # Update the "output" text element to be the value of "input" element
        window['-OUTPUT-'].update(values['-IN-'])

window.close()




