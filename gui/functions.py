
def registration():
    while True:
        event, values = regwindow.read()
        print(event, values)
        if event == 'Submit':
            regid = values['-reg-']
            brand = values['-brand-']
            model = values['-model-']
            year = values['-year-']

            sql = "INSERT INTO car(regid, brand, model, year) VALUES (%s, %s, %s, %s)"
            val = (regid, brand, model, year)
            mycursor.execute(sql, val)

            mydb.commit()
            print(mycursor.rowcount, "record inserted.")

            text_input = values['-reg-']
            sg.popup('The car was registered. Registration number:', text_input)

        if event in (None, 'Exit'):
            mainwindow.UnHide()
            regwindow_active = False
            break