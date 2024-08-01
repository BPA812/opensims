from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
import webbrowser
import simsutils
from playsound import playsound
from PIL import ImageTk, Image
window = Tk()
window.geometry('750x500')
window.title("OpenSims")
def opensims():
    button.destroy()
    button2.destroy()
    button3.destroy()
    button4.destroy()
    button5.destroy()
    play1.destroy()
    play2.destroy()
    play3.destroy()
    play4.destroy()
    play5.destroy()
    canvas.pack()
    window.geometry('500x370')
def opengithub():
    webbrowser.open('https://bpa812.github.io/', new=2)
def openea():
    webbrowser.open('https://www.ea.com/en-gb', new=2)
def startmusic():
    playsound('ts1.mp3', False)
def displayinfo():
    messagebox.showinfo("showinfo", "About this project: \n This game is an open source project made by @BPA812 on Github. \n C BPA812 2024")
def exitwin():
    window.destroy()
def sim1f():
    print('1 sim lane selected')
def sim2f():
    print('2 sim lane selected')
def sim3f():
    print('3 sim lane selected')
def newfamily():
    print('new family creation started ')
    answer = simpledialog.askstring("Families", "Family Surname:", parent=window)
def deletefamily():
    print('deleting family')
def movefamily():
    print('moving family')
def openfamilywindow():
    # Create secondary (or popup) window.
    secondary_window = Toplevel()
    secondary_window.title("Families")
    secondary_window.config(width=400, height=300)
    # Create a button to close (destroy) this window.
    button_close = Button(
        secondary_window,
        text="Close",
        command=secondary_window.destroy
    )
    button_close.place(x=20, y=260)

    button_close2 = Button(
        secondary_window,
        text="Create",
        command=newfamily
    )
    button_close2.place(x=130, y=260)
    button_close3 = Button(
        secondary_window,
        text="Delete",
        command=deletefamily
    )
    button_close3.place(x=205, y=260)
    button_close4 = Button(
        secondary_window,
        text="Move In",
        command=movefamily
    )
    button_close4.place(x=280, y=260)
play1 = Label(text="Play")
play1.place(x=115, y=175)
startmusic()
#Let us create a dummy button and pass the image
button= Button(
    window,
    text=' Open \n Sims',
    height=4,
    width=4,
    command = opensims,
)
button.place(x=150, y=150)

button2= Button(
    window,
    text=' w w w',
    command = opengithub,
    height=4,
    width=4
)
button2.place(x=225, y=225)
play2 = Label(text="Visit My Website")
play2.place(x=110, y=250)
button3= Button(
    window,
    text=' Electronic \n  Arts',
    command = openea,
    height=4,
    width=4
)
button3.place(x=300, y=300)
play3 = Label(text="Visit EA")
play3.place(x=235, y=325)
button4= Button(
    window,
    text=' ?',
    command = displayinfo,
    height=4,
    width=4
)
button4.place(x=375, y=375)
play4 = Label(text="Information")
play4.place(x=290, y=400)
button5= Button(
    window,
    text=' O>',
    command = exitwin,
    height=4,
    width=4
)
button5.place(x=450, y=425)
play5 = Label(text="Exit")
play5.place(x=415, y=450)
sims = Label(text='Sims')
sims['font'] = ('Helvetica', 50, 'bold')
sims.place(x=50, y=50)
sims2 = Label(text='Open')
sims2['font'] = ('Helvetica', 25, 'bold')
sims2.place(x=70, y=20)
#Specify the file name present in the same directory or else
#specify the proper path for retrieving the image to set it as background image.
canvas = Canvas(window, width=750, height=500)
tk_img= PhotoImage(file = "ts1.png")
canvas.create_image(125, 125, image=tk_img)
siml1 = Button(window, text = "1 Sim Lane ($7000)", command = sim1f, anchor = 'w',
width = 10, activebackground = "#33B5E5")
quit_button_window = canvas.create_window(180, 140, anchor='nw', window=siml1)
siml2 = Button(window, text = "2 Sim Lane ($7000)", command = sim2f, anchor = 'w',
               width = 10, activebackground = "#33B5E5")
quit_button_window2 = canvas.create_window(350, 250, anchor='nw', window=siml2)
siml3 = Button(window, text = "3 Sim Lane ($7000)", command = sim3f, anchor = 'w',
width = 10, activebackground = "#33B5E5")
quit_button_window3 = canvas.create_window(185, 325, anchor='nw', window=siml3)
family1 = Button(window, text = "Families", command = openfamilywindow, anchor = 'w',
               width = 5, activebackground = "#33B5E5")
make_family_window1 = canvas.create_window(25, 5, anchor='nw', window=family1)
window.mainloop()