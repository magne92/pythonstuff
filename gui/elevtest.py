import PySimpleGUI as sg

sg.theme('sandy beach')

layout = [[sg.Text('Skriv inn din bils info under : '), sg.Text(size=(25,1), key='-output-')],
          [sg.Text('Merke :'), sg.Input(size=(21,1), key='-merke-'), sg.Text(size=(15,1), key='-omerke-')],
          [sg.Text('Modell :'), sg.Input(size=(21,1), key='-modell-'), sg.Text(size=(15,1), key='-omodell-')],
          [sg.Text('Årsmodell :'), sg.Input(size=(18,1), key='-års-'), sg.Text(size=(15,1), key='-oårs-')],
          [sg.Text('Reg. nummer :'), sg.Input(size=(15,1), key='-reg-'), sg.Text(size=(15,1), key='-oreg-')],
          [sg.Button('Show'), sg.Button('Exit')]]


window = sg.Window('Bil Informasjon', layout)

while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if event in (None, 'Exit'):
        break
    if event == 'Show':
        # Update the "output" text element to be the value of "input" element
        window['-output-'].update('Er dette din bils informasjon?')
        window['-omerke-'].update(values['-merke-'])
        window['-omodell-'].update(values['-modell-'])
        window['-oårs-'].update(values['-års-'])
        window['-oreg-'].update(values['-reg-'])

window.close()

