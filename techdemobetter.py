# Import module 
from tkinter import *
from PIL import Image,ImageTk

# Create object 
root = Tk() 

# Adjust size 
root.geometry("400x400") 

# Add image file 
bg = PhotoImage(file = "/terrain/mapdemo.png") 

# Show image using label 
label1 = Label( root, image = bg) 
label1.place(x = -2, y = 0) 

photo = (Image.open("MediumAdultMale.png"))
simw = 30
simh = simw*1.5
resized_image= photo.resize((int(simw),int(simh)))
photo2= ImageTk.PhotoImage(resized_image)
buttonshow1 = 0
mysimbutton1 = Button(root, text = 'Click Me !',height= 1, width=5)
def clickedsim():
    print('clicked the sim')
    mysimbutton1.place(x = 100, y = 210)
# here, image option is used to 
# set image on button 
mysim = Button(root, text = 'Click Me !',height= 40, width=40, image = photo2,command = clickedsim,bg= '#ab23ff')
# Execute tkinter 
mysim.place(x = 202, y = 202) 
root.mainloop()
