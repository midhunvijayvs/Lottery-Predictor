
import tkinter
import tkinter.messagebox
from tkinter import *
from PIL import Image
from PIL import ImageTk
from FunctionsModule import (
   set_logger,
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

#setting up the UI
mainWindow = tkinter.Tk()
mainWindow.geometry("600x400")
mainWindow.title("Lottery Analyzer")
mainWindow.configure(bg='#222222')



#making the window fullscreen
platform_type = get_platform()
if platform_type == "Windows":
    mainWindow.state('zoomed')  # Only works on Windows
elif platform_type == "Android":
    print("Running on Android - skipping zoomed")
    # You might want to set fullscreen or a fixed size here
    # mainWindow.attributes('-fullscreen', True)
else:
    print("Platform not recognized:", platform_type)
    
    
bannerImage = Image.open("image.png")
bannerImage = bannerImage.resize((200, 150), Image.Resampling.LANCZOS)

test = ImageTk.PhotoImage(bannerImage)

labelForImage = tkinter.Label(image=test)
labelForImage.image = test
# Position image
labelForImage.place(x=0, y=0)

outputScrollBar = tkinter.Scrollbar(mainWindow)
T = tkinter.Text(mainWindow, height=4, width=90)

if platform_type == "Android":
    # Scrollbar still vertical but placed at bottom
    T.place(x=20, y=800, width=1300, height=1000)
    outputScrollBar.place(x=1320, y=800, height=1000)
else:
    T.pack(side=tkinter.RIGHT, fill=tkinter.Y)
    outputScrollBar.pack(side=tkinter.RIGHT, fill=tkinter.Y)

outputScrollBar.config(command=T.yview)
T.config(yscrollcommand=outputScrollBar.set)
T.configure(bg='#000000', fg='#00ff00', padx=50, pady=50)

# function to print any text to the ouput screen
def add_text_to_output_screen(text):
    T.insert(tkinter.END, "\n")
    T.insert(tkinter.END, text)
    T.see(tkinter.END)  #Without T.see(tkinter.END), if the user has scrolled up in the Text widget, they might miss new content being added at the bottom. This command keeps the view auto-scrolled to the latest entry — useful for logging or real-time output windows.
    T.update_idletasks()  # <- This forces the UI to update immediately . So that output will be seen as updating in real time.

def clear_output_screen():
      T.delete(1.0, tkinter.END)  # Clear the text widget
      T.insert(tkinter.END, "Screen Cleared\n")  # Optional: Add a message after clearing

def add_new_line_to_output_screen():
      T.insert(tkinter.END, "\n")
      T.see(tkinter.END)  # Scroll to the end after adding a new line     
set_logger(add_text_to_output_screen,clear_output_screen, add_new_line_to_output_screen)  # Set the logger once  to print to the screen, from the FunctionsModule.py file too



if platform_type == "Windows":
   add_text_to_output_screen("Platform detected: Windows")
elif platform_type == "Android":
   add_text_to_output_screen("Platform detected: Android")




def update_pdf_files():
    try:
        count = int(file_count_entry.get())
        start_serial = int(serial_entry.get())
    except ValueError:
        add_text_to_output_screen("Input Error!! Please enter valid numbers.")
        return

    delete_all_pdfs()
    downloadPDF(count, start_serial)
    verifyPDFs()
   
 
 
 
 
 
 
 
 
 
   
def analyze_and_show():
   #clear_output_screen() 
   extractedText=""
   
   for i in range(1,7):
      text=(extractTextFromFile(str(i)+".pdf"))
      extractedText+=text
      
   array=splitToIntArray(extractedText)
   conditionedArray=conditionArray(array)
   FDN=sixToFour(conditionedArray) #FDN=Four Digit Numbers Array

   Dig0Result, Dig1Result, Dig2Result, Dig3Result=analyze(FDN)

    
   add_text_to_output_screen("Row Result")
   add_text_to_output_screen(Dig0Result)
   add_text_to_output_screen(Dig1Result)
   add_text_to_output_screen(Dig2Result)
   add_text_to_output_screen(Dig3Result)
   add_new_line_to_output_screen()
   add_new_line_to_output_screen()
   
   formattedResultToDisplay= format_result_for_display(Dig3Result, Dig2Result, Dig1Result, Dig0Result)
   mostRepeatedDigits=find_most_frequent_digits(Dig3Result, Dig2Result, Dig1Result, Dig0Result)
   secondMostRepeatedDigits=find_second_most_frequent_digits(Dig3Result, Dig2Result, Dig1Result, Dig0Result)
   
   
   
  

   # show formatted final result
   add_text_to_output_screen("Final Result: ")
   add_text_to_output_screen("--------------------------------------------------")
   for row in formattedResultToDisplay:
      add_text_to_output_screen(row)

   add_new_line_to_output_screen()
   add_text_to_output_screen("--------------------------------------------------")
   add_new_line_to_output_screen()

   # show most repeated digits
   add_text_to_output_screen("Most Repeated Digits: ")
   add_text_to_output_screen(mostRepeatedDigits)
   add_new_line_to_output_screen()
   add_text_to_output_screen("--------------------------------------------------")
   add_new_line_to_output_screen()
   add_text_to_output_screen("Second Most Repeated Digits: ")
   add_text_to_output_screen(secondMostRepeatedDigits)
   add_text_to_output_screen("--------------------------------------------------")
   



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



# Entry for number of files to download
tkinter.Label(mainWindow, text="No. of Files:", bg='#222222', fg='white').place(x=20, y=230)
file_count_entry = tkinter.Entry(mainWindow)
file_count_entry.place(x=400, y=230)
file_count_entry.insert(0, "7")  # default value

# Entry for starting serial number
tkinter.Label(mainWindow, text="Start Serial No:", bg='#222222', fg='white').place(x=20, y=300)
serial_entry = tkinter.Entry(mainWindow)
serial_entry.place(x=400, y=300)
serial_entry.insert(0, "74890")  # default value   


B1 = tkinter.Button(mainWindow, text ="Update PDF Files", command = update_pdf_files,bg="#ff44aa")
B1.place(x=20,y=400)

B2 = tkinter.Button(mainWindow, text ="Analyze!", command = analyze_and_show,bg="#ff44aa")
B2.place(x=600,y=400)


B3 = tkinter.Button(mainWindow, text ="Clear Screen", command = clear_output_screen,bg="#ff44aa")
B3.place(x=20,y=550)

B4 = tkinter.Button(mainWindow, text ="Settings", command = openSettingsWindow,bg="#666666")
B4.place(x=600,y=550)


mainWindow.mainloop()
