
import tkinter
import tkinter.messagebox
from tkinter import *
from PIL import Image
from PIL import ImageTk
from FunctionsModule import (
   delete_all_pdfs,
    downloadPDF,
    verifyPDFs,
    extractTextFromFile,
    splitToIntArray,
    conditionArray,
    sixToFour,
    unpack,
    count,
    analize,
 format_result_for_display,
 find_most_frequent_digits,
 find_second_most_frequent_digits
 )

mainWindow = tkinter.Tk()
mainWindow.geometry("600x400")
mainWindow.title("Lottery Analizer")
mainWindow.configure(bg='#222222')


image1 = Image.open("image.png")
#image1 = img.resize((50, 50), Image.ANTIALIAS)
test = ImageTk.PhotoImage(image1)

label1 = tkinter.Label(image=test)
label1.image = test
# Position image
label1.place(x=0, y=0)




mainWindow.state('zoomed')
'''mainWindow.attributes('-fullscreen',True)'''


def update_pdf_files():
   delete_all_pdfs()
   downloadPDF(7,74897)
  
   downloadReport=verifyPDFs()
   print("Report of PDF files:")
   print(downloadReport)
   tkinter.messagebox.showinfo("Download Report", downloadReport)
   
def analize_and_show():
   
   extractedText=""
   
   for i in range(1,7):
      text=(extractTextFromFile(str(i)+".pdf"))
      extractedText+=text
      
   array=splitToIntArray(extractedText)
   conditionedArray=conditionArray(array)
   FDN=sixToFour(conditionedArray) #FDN=Four Digit Numbers Array

   Dig0Result, Dig1Result, Dig2Result, Dig3Result=analize(FDN)

  
  
   print("Result seperated")
   print(Dig0Result)
   print(Dig1Result)
   print(Dig2Result)
   print(Dig3Result)
   
   formatedResultToDiplay= format_result_for_display(Dig3Result, Dig2Result, Dig1Result, Dig0Result)
   mostRepetitionDigits=find_most_frequent_digits(Dig3Result, Dig2Result, Dig1Result, Dig0Result)
   secondMostRepetitionDigits=find_second_most_frequent_digits(Dig3Result, Dig2Result, Dig1Result, Dig0Result)
   
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
   T.insert(tkinter.END, formatedResultToDiplay[0])
   T.insert(tkinter.END, "\n")
   T.insert(tkinter.END,formatedResultToDiplay[1])
   T.insert(tkinter.END, "\n")
   T.insert(tkinter.END, formatedResultToDiplay[2])
   T.insert(tkinter.END, "\n")
   T.insert(tkinter.END, formatedResultToDiplay[3])
   T.insert(tkinter.END, "\n")
   T.insert(tkinter.END, formatedResultToDiplay[4])
   T.insert(tkinter.END, "\n")
   T.insert(tkinter.END, formatedResultToDiplay[5])
   T.insert(tkinter.END, "\n")
   T.insert(tkinter.END, formatedResultToDiplay[6])
   T.insert(tkinter.END, "\n")
   T.insert(tkinter.END, formatedResultToDiplay[7])
   T.insert(tkinter.END, "\n")
   T.insert(tkinter.END, formatedResultToDiplay[8])
   T.insert(tkinter.END, "\n")
   T.insert(tkinter.END, formatedResultToDiplay[9])
   
   T.insert(tkinter.END, "\n")
   T.insert(tkinter.END, "\n")
   T.insert(tkinter.END, "Most Repeated Digits: ")
   T.insert(tkinter.END, mostRepetitionDigits)
   T.insert(tkinter.END, "\n")
   T.insert(tkinter.END, "\n")
   T.insert(tkinter.END, "Second Most Repeated Digits: ")
   T.insert(tkinter.END, secondMostRepetitionDigits)
   T.insert(tkinter.END, "\n")






def radioSelected():
   selection = "You selected the option " + str(var.get())
   label.config(text = selection)


def openSettingsWindow():
   settingsWindow = Toplevel(mainWindow)
   settingsWindow.title("Settings")
   settingsWindow.geometry("600x200")
   
   var = IntVar()
   R1 = Radiobutton(settingsWindow, text="Full result Analize", variable=var, value=1,command=radioSelected)
   R1.pack( anchor = settingsWindow )
   R2 = Radiobutton(settingsWindow, text="4th Prize Analize", variable=var, value=2, command=radioSelected)
   R2.pack( anchor = settingsWindow )

   R3 = Radiobutton(settingsWindow, text="5th Price Analize", variable=var, value=3,command=radioSelected)
   R3.pack( anchor = settingsWindow)
   
   label = Label(settingsWindow)
   label.pack()
   settingsWindow.mainloop()   
     

B1 = tkinter.Button(mainWindow, text ="Analise!", command = analize_and_show,bg="#ff44aa")
B1.pack()
B1.place(x=270,y=300)


B2 = tkinter.Button(mainWindow, text ="Update PDF Files", command = update_pdf_files,bg="#666666")
B2.pack()
B2.place(x=370,y=300)

B3 = tkinter.Button(mainWindow, text ="Setings", command = openSettingsWindow,bg="#666666")
B3.pack()
B3.place(x=470,y=300)


mainWindow.mainloop()
