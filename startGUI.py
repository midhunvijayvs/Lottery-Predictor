import main
import tkinter
import tkinter.messagebox
from tkinter import *
from PIL import Image
from PIL import ImageTk


mainWindow = tkinter.Tk()
mainWindow.geometry("600x400")
mainWindow.title("Lottery Analizer")
mainWindow.configure(bg='#65b4ff')


image1 = Image.open("/home/midhunvijay/My Projects/Lottery Analiser/image.png")
#image1 = img.resize((50, 50), Image.ANTIALIAS)
test = ImageTk.PhotoImage(image1)

label1 = tkinter.Label(image=test)
label1.image = test
# Position image
label1.place(x=0, y=0)



def openAnalisesWindow():
     analiseWindow = Toplevel(mainWindow)
     analiseWindow.title("Analisis Report")
     analiseWindow.geometry("400x1200")

     S = tkinter.Scrollbar(analiseWindow)
     T = tkinter.Text(analiseWindow, height=4, width=50)
     S.pack(side=tkinter.RIGHT, fill=tkinter.Y)
     T.pack(side=tkinter.LEFT, fill=tkinter.Y)
     S.config(command=T.yview)
     T.config(yscrollcommand=S.set)
     T.insert(tkinter.END, main.index)
     T.insert(tkinter.END, "\n")
     T.insert(tkinter.END, main.Dig3Result)
     T.insert(tkinter.END, "\n")
     T.insert(tkinter.END, main.Dig2Result)
     T.insert(tkinter.END, "\n")
     T.insert(tkinter.END, main.Dig1Result)
     T.insert(tkinter.END, "\n")
     T.insert(tkinter.END, main.Dig0Result)
     T.insert(tkinter.END, "\n")
     
def openSettingsWindow():
   settingsWindow = Toplevel(mainWindow)
   settingsWindow.title("Settings")
   settingsWindow.geometry("600x200")
 
     

B1 = tkinter.Button(mainWindow, text ="Analise!", command = openAnalisesWindow,bg="#ff44aa")
B1.pack()
B1.place(x=270,y=300)
B2 = tkinter.Button(mainWindow, text ="Setings", command = openSettingsWindow,bg="#666666")
B2.pack()
B2.place(x=370,y=300)
mainWindow.mainloop()
