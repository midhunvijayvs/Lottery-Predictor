
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
    analyze,
 format_result_for_display,
 find_most_frequent_digits,
 find_second_most_frequent_digits,
 get_platform
 )

mainWindow = tkinter.Tk()
mainWindow.geometry("600x400")
mainWindow.title("Lottery Analyzer")
mainWindow.configure(bg='#222222')


image1 = Image.open("image.png")
image1 = image1.resize((200, 150), Image.Resampling.LANCZOS)

test = ImageTk.PhotoImage(image1)

label1 = tkinter.Label(image=test)
label1.image = test
# Position image
label1.place(x=0, y=0)



platform_type = get_platform()

if platform_type == "Windows":
    mainWindow.state('zoomed')  # Only works on Windows
elif platform_type == "Android":
    print("Running on Android - skipping zoomed")
    # You might want to set fullscreen or a fixed size here
    # mainWindow.attributes('-fullscreen', True)
else:
    print("Platform not recognized:", platform_type)
    
    
    

def update_pdf_files():
   delete_all_pdfs()
   downloadPDF(7,74897)
  
   downloadReport=verifyPDFs()
   print("Report of PDF files:")
   print(downloadReport)
   tkinter.messagebox.showinfo("Download Report", downloadReport)
   
def analyze_and_show():
   
   extractedText=""
   
   for i in range(1,7):
      text=(extractTextFromFile(str(i)+".pdf"))
      extractedText+=text
      
   array=splitToIntArray(extractedText)
   conditionedArray=conditionArray(array)
   FDN=sixToFour(conditionedArray) #FDN=Four Digit Numbers Array

   Dig0Result, Dig1Result, Dig2Result, Dig3Result=analyze(FDN)

  
  
   print("Result seperated")
   print(Dig0Result)
   print(Dig1Result)
   print(Dig2Result)
   print(Dig3Result)
   
   formattedResultToDisplay= format_result_for_display(Dig3Result, Dig2Result, Dig1Result, Dig0Result)
   mostRepeatedDigits=find_most_frequent_digits(Dig3Result, Dig2Result, Dig1Result, Dig0Result)
   secondMostRepeatedDigits=find_second_most_frequent_digits(Dig3Result, Dig2Result, Dig1Result, Dig0Result)
   
   
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
   
   T.delete("1.0", tkinter.END)

   # Insert formatted rows
   for row in formattedResultToDisplay:
      T.insert(tkinter.END, row)
      T.insert(tkinter.END, "\n")

   # Insert most repeated digits
   T.insert(tkinter.END, "\nMost Repeated Digits: ")
   T.insert(tkinter.END, mostRepeatedDigits)
   T.insert(tkinter.END, "\n\nSecond Most Repeated Digits: ")
   T.insert(tkinter.END, secondMostRepeatedDigits)
   T.insert(tkinter.END, "\n")






def openSettingsWindow():
   settingsWindow = Toplevel(mainWindow)
   settingsWindow.title("Settings")
   settingsWindow.geometry("600x200")
   
   var = IntVar()
   label = Label(settingsWindow)
   label.pack()

   def radioSelected():
       selection = "You selected the option " + str(var.get())
       label.config(text = selection)

   R1 = Radiobutton(settingsWindow, text="Full result Analyze", variable=var, value=1, command=radioSelected)
   R1.pack(anchor = settingsWindow)
   R2 = Radiobutton(settingsWindow, text="4th Prize Analyze", variable=var, value=2, command=radioSelected)
   R2.pack(anchor = settingsWindow)
   R3 = Radiobutton(settingsWindow, text="5th Prize Analyze", variable=var, value=3, command=radioSelected)
   R3.pack(anchor = settingsWindow)
   
B1 = tkinter.Button(mainWindow, text ="Update PDF Files", command = update_pdf_files,bg="#ff44aa")
B1.place(x=270,y=300)

B2 = tkinter.Button(mainWindow, text ="Analyze!", command = analyze_and_show,bg="#ff44aa")
B2.place(x=370,y=300)



B3 = tkinter.Button(mainWindow, text ="Settings", command = openSettingsWindow,bg="#666666")
B3.place(x=470,y=300)


mainWindow.mainloop()
