import PySimpleGUI as sg
import time

sg.theme('Dark Blue 8')

for i in range(1000):
    sg.OneLineProgressMeter('One Line Meter Example', i + 1, 1000, 'key')
    
time.sleep(5)