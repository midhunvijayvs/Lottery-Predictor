import main
import tkinter
import tkinter.messagebox
from tkinter import *
from PIL import Image
from PIL import ImageTk


mainWindow = tkinter.Tk()
mainWindow.geometry("600x400")
mainWindow.title("Lottery Analizer")
mainWindow.configure(bg='#222222')


image1 = Image.open("D:\Midhun\Lottery Analiser-python/image.png")
#image1 = img.resize((50, 50), Image.ANTIALIAS)
test = ImageTk.PhotoImage(image1)

label1 = tkinter.Label(image=test)
label1.image = test
# Position image
label1.place(x=0, y=0)




mainWindow.state('zoomed')
'''mainWindow.attributes('-fullscreen',True)'''
def analize():
     S = tkinter.Scrollbar(mainWindow)
     T = tkinter.Text(mainWindow, height=4, width=90)
     S.pack(side=tkinter.RIGHT, fill=tkinter.Y)
     T.pack(side=tkinter.RIGHT, fill=tkinter.Y)
     S.config(command=T.yview)
     T.config(yscrollcommand=S.set)
     T.configure(bg='#000000')
     T.configure(fg='#00ff00')
     T.configure(padx=50)
     T.configure(pady=50)
     T.insert(tkinter.END, main.index)
     T.insert(tkinter.END, "\n")
     T.insert(tkinter.END,main.Dig3Result)
     T.insert(tkinter.END, "\n")
     T.insert(tkinter.END, main.Dig2Result)
     T.insert(tkinter.END, "\n")
     T.insert(tkinter.END, main.Dig1Result)
     T.insert(tkinter.END, "\n")
     T.insert(tkinter.END, main.Dig0Result)
     T.insert(tkinter.END, "\n")


def radioSelected():
   selection = "You selected the option " + str(var.get())
   label.config(text = selection)


def openSettingsWindow():
   settingsWindow = Toplevel(mainWindow)
   settingsWindow.title("Settings")
   settingsWindow.geometry("600x200")

   
   
   var = IntVar()
   R1 = Radiobutton(settingsWindow, text="Option 1", variable=var, value=1,command=radioSelected)
   R1.pack( anchor = settingsWindow )
   R2 = Radiobutton(settingsWindow, text="Option 2", variable=var, value=2, command=radioSelected)
   R2.pack( anchor = settingsWindow )

   R3 = Radiobutton(settingsWindow, text="Option 3", variable=var, value=3,command=radioSelected)
   R3.pack( anchor = settingsWindow)
   
   label = Label(settingsWindow)
   label.pack()
   settingsWindow.mainloop()   
     

B1 = tkinter.Button(mainWindow, text ="Analise!", command = analize,bg="#ff44aa")
B1.pack()
B1.place(x=270,y=300)
B2 = tkinter.Button(mainWindow, text ="Setings", command = openSettingsWindow,bg="#666666")
B2.pack()
B2.place(x=370,y=300)
mainWindow.mainloop()
