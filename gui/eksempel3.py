import PySimpleGUI as sg
 
sg.ChangeLookAndFeel('GreenTan')
 
layout = [
    [sg.Text('Mitt test vindu', size=(30, 1), font=("Helvetica", 25)) ],
    [sg.Image('gui\potet.png')],
    [sg.Text(key='output_field')],
    [sg.Input(key='INPUT')],
    [sg.Submit(), sg.Cancel(), sg.Button('Potet')]
]
layout2 = [
    [sg.Text('Mitt test vindu2  ', size=(30, 1), font=("Helvetica", 25)) ],
    [sg.Text(key='output_field')],
    [sg.Input(key='INPUT')],
    [sg.Submit(), sg.Cancel(), sg.Button('Potet')]
]
 
 
window = sg.Window('Everything bagel', resizable=True, default_element_size=(40, 1)).Layout(layout)
 
while True:
    event, values = window.Read()
 
    if event == 'Cancel' or event == sg.WIN_CLOSED:
        window.close()
        break
    if event == 'Submit':
        window.close()
        window = sg.Window('Everything bagel', default_element_size=(40, 1)).Layout(layout2)
 
    if event == 'Potet':
        window['output_field'].update(values['INPUT'])