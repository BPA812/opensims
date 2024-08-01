import tkinter as tk
import time
from tkinter import messagebox, ttk

def display_selection():
    valer = 0
    # Get the selected value.
    selection = combos.get()
    selection2 = combos2.get()
    selection3 = combos3.get()
    selection4 = combos4.get()
    selection5 = combos5.get()
    selection6 = combos6.get()
    if selection == 'Dark':
        selection = '00Dark'
    if selection == 'Light':
        selection = '0Light'
    if selection3 == 'Male':
        selection3 = '00Male'
    try:
        if int(selection4) < 10:
            selection4 = '0' + selection4
    except ValueError:
        if valer == 0:
            messagebox.showinfo(
                message=f"Please fill out all of the fields before generating the code.",
                title="Alert"
            )
        valer = 1
    try:
        if int(selection5) < 10:
            selection5 = '0' + selection5
    except ValueError:
        if valer == 0:
            messagebox.showinfo(
                message=f"Please fill out all of the fields before generating the code.",
                title="Alert"
            )
        valer = 1
    try:
        if int(selection6) < 10:
            selection6 = '0' + selection6
    except ValueError:
        if valer == 0:
            messagebox.showinfo(
                message=f"Please fill out all of the fields before generating the code.",
                title="Alert"
            )
        valer = 1
    ckey = selection + selection2 + selection3 + selection4 + selection5 + selection6
    if valer == 0:
        messagebox.showinfo(
            message=f"Your character key: {ckey}",
            title="Selection"
        )
def run():

    if var1.get() == "A":
        Labelvar.set("Label updated")

    result_label.config(textvariable=Labelvar)

    return
def on_option_select(event):
    selected_option.set(event)
    label1['text'] = event
root = tk.Tk()
root.title("OpenSims Creator")
root.geometry("750x300")

Labelvar = tk.StringVar()

var1 = tk.StringVar()

var1.set("A")
# Create a StringVar to hold the selected option
selected_option = tk.StringVar()
# Create the dropdown menu
options = ["Light", "Medium",  "Dark"]
combos = ttk.Combobox(
    state="readonly",
    values=["Light", "Medium", "Dark"]
)
combos.place(x=90,y=22)
# Add a button to display the selected option
label1 = tk.Label(root, text="Skin Colour")
label1.place(x=10,y=20)

selected_option2 = tk.StringVar()
combos2 = ttk.Combobox(
    state="readonly",
    values=["Adult", "Child"]
)
combos2.place(x=90,y=52)
# Add a button to display the selected option
label2 = tk.Label(root, text="Age Group")
label2.place(x=10,y=50)

button = ttk.Button(text="Display selection", command=display_selection)
button.place(x=500, y=100)
# Label to display the selected option
selected_option3 = tk.StringVar()
combos3 = ttk.Combobox(
    state="readonly",
    values=["Male", "Female"]
)
combos3.place(x=90,y=84)
# Add a button to display the selected option
label3 = tk.Label(root, text="Gender:")
label3.place(x=10,y=82)

selected_option4 = tk.StringVar()
combos4 = ttk.Combobox(
    state="readonly",
    values=["1", "2","3","4","5","6","7","8","9","10"]
)
combos4.place(x=90,y=116)
# Add a button to display the selected option
label4 = tk.Label(root, text="Neatness:")
label4.place(x=10,y=114)

selected_option5 = tk.StringVar()
combos5 = ttk.Combobox(
    state="readonly",
    values=["1", "2","3","4","5","6","7","8","9","10"]
)
combos5.place(x=90,y=148)
# Add a button to display the selected option
label5 = tk.Label(root, text="Outgoing:")
label5.place(x=10,y=146)

selected_option6 = tk.StringVar()
combos6 = ttk.Combobox(
    state="readonly",
    values=["1", "2","3","4","5","6","7","8","9","10"]
)
combos6.place(x=90,y=180)
# Add a button to display the selected option
label6 = tk.Label(root, text="Activeness:")
label6.place(x=10,y=178)

root.mainloop()
