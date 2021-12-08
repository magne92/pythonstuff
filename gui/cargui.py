import PySimpleGUI as sg
import mysql.connector
from gui.layouts import *

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    passwd="",
    database="carreg"
)

mycursor = mydb.cursor()
sg.change_look_and_feel('Reddit')

logwindow = sg.Window('Car registration', loginlayout())
loginstate = False

myid = ''

while True:
    eventlogin, valueslogin = logwindow.read(timeout=100)
    if eventlogin is None or eventlogin is 'Exitprogram':
        break

    if eventlogin == 'Login':
        username = valueslogin['-username-']
        pw = valueslogin['-password-']
        print(username, pw)

        sql = "SELECT userid, username, password FROM users WHERE username =%s AND password = %s"
        mycursor.execute(sql, (username, pw))
        myresult = mycursor.fetchall()
        print(myresult)

        row_count = mycursor.rowcount
        if row_count == 1:
            sql = "SELECT userid FROM users WHERE username =%s AND password = %s"
            mycursor.execute(sql, (username, pw))
            myresult = mycursor.fetchone()

            myid = myresult[0]

            loginstate = True
            logwindow.Hide()
        else:
            print("feil ved innlogging")

    if loginstate:
        mainwindow = sg.Window('Cars', mainlayout())
        regwindow_active = False

        while True:  # main window loop
            event1, values1 = mainwindow.Read(timeout=100)

            if event1 in (None, 'Logout'):
                loginstate = False
                logwindow.UnHide()
                mainwindow.close()
                break

            elif event1 == 'Registration' and not regwindow_active:
                mainwindow.Hide()
                regwindow = sg.Window('Car registration', regilayout())

                while True:
                    event, values = regwindow.read()
                    print(event, values)
                    if event == 'Submit':
                        regid = values['-reg-']
                        brand = values['-brand-']
                        model = values['-model-']
                        year = values['-year-']
                        ownerid = values['-ownerid-']

                        sql = "INSERT INTO car(regid, brand, model, year, owner) VALUES (%s, %s, %s, %s, %s)"
                        val = (regid, brand, model, year, ownerid)
                        mycursor.execute(sql, val)

                        mydb.commit()
                        print(mycursor.rowcount, "record inserted.")

                        sg.popup('The car was registered. Registration number:', regid)

                    if event in (None, 'Exit'):
                        mainwindow.UnHide()
                        regwindow_active = False
                        break

                regwindow.close()

            elif event1 == 'Show cars':
                mainwindow.Hide()

                while True:
                    sql = "SELECT regid, brand, model, year, username FROM car JOIN users ON car.owner=users.userid"
                    mycursor.execute(sql)
                    myresult = mycursor.fetchall()

                    car_layout = carlayout(myresult)
                    carwindow = sg.Window('All cars in database', car_layout)

                    event, values = carwindow.read()
                    print(event, values)
                    if event in (None,'Exit'):
                        mainwindow.UnHide()
                        carwindow.Close()
                        break

                    if event == 'Update':
                        #sql = "SELECT regid, brand, model, year FROM car"
                        #mycursor.execute(sql)
                        #myresult = mycursor.fetchall()
                        carwindow.Close()
                        #car_layout2 = carlayout(myresult)
                        #carwindow2 = sg.Window('All cars in database', car_layout2)
                        print(myresult)

            elif event1 == 'My cars':
                mainwindow.Hide()
                print(myid)
                while True:
                    sql = "SELECT * FROM car WHERE owner = " + str(myid)
                    mycursor.execute(sql)
                    mycarresult = mycursor.fetchall()
                    row_count = mycursor.rowcount

                    if row_count > 0:
                        mylayout = mycarlayout(mycarresult)
                        mycarwindow = sg.Window('All cars in database', mylayout)
                        event3, values3 = mycarwindow.read()
                        print(mycarresult)

                        if event3 in (None, 'Exit'):
                            mainwindow.UnHide()
                            mycarwindow.Close()
                            break

                    else:
                        sg.popup('No cars registered at logged in user')
                        mainwindow.UnHide()
                        break




logwindow.close()
mydb.close()




