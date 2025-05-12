
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





platform_type = get_platform() # Get the platform type, windows or android




#setting up the UI
mainWindow = tkinter.Tk()
mainWindow.geometry("600x400")
mainWindow.title("Lottery Analyzer")
mainWindow.configure(bg='#222222')

bannerImage = Image.open("image.png")
outputScrollBar = tkinter.Scrollbar(mainWindow)
outputText = tkinter.Text(mainWindow, height=4, width=90)
outputScrollBar.config(command=outputText.yview)
outputText.config(yscrollcommand=outputScrollBar.set)
outputText.configure(bg='#000000', fg='#00ff00', padx=50, pady=50)

label_file_count = tkinter.Label(mainWindow)
label_file_count.config(text="No. of Files:", bg='#222222', fg='white')

file_count_entry = tkinter.Entry(mainWindow)
file_count_entry.insert(0, "7")  # Default value

label_serial_number = tkinter.Label(mainWindow)
label_serial_number.config(text="Start Serial No:", bg='#222222', fg='white')

serial_number_entry = tkinter.Entry(mainWindow)
serial_number_entry.insert(0, "74890")  # Default value

B1 = tkinter.Button(mainWindow)
B2 = tkinter.Button(mainWindow)
B3 = tkinter.Button(mainWindow)
B4 = tkinter.Button(mainWindow)





# function to print any text to the ouput screen
def add_text_to_output_screen(text):
    outputText.insert(tkinter.END, "\n")
    outputText.insert(tkinter.END, text)
    outputText.see(tkinter.END)  #Without outputText.see(tkinter.END), if the user has scrolled up in the Text widget, they might miss new content being added at the bottom. This command keeps the view auto-scrolled to the latest entry — useful for logging or real-time output windows.
    outputText.update_idletasks()  # <- This forces the UI to update immediately . So that output will be seen as updating in real time.

def clear_output_screen():
      outputText.delete(1.0, tkinter.END)  # Clear the text widget
      outputText.insert(tkinter.END, "Screen Cleared\n")  # Optional: Add a message after clearing

def add_new_line_to_output_screen():
      outputText.insert(tkinter.END, "\n")
      outputText.see(tkinter.END)  # Scroll to the end after adding a new line     
set_logger(add_text_to_output_screen,clear_output_screen, add_new_line_to_output_screen)  # Set the logger once  to print to the screen, from the FunctionsModule.py file too




#summary function to update the pdf files
# This function will be called when the update pdf button is clicked
def update_pdf_files():
    try:
        count = int(file_count_entry.get())
        start_serial = int(serial_number_entry.get())
    except ValueError:
        add_text_to_output_screen("Input Error!! Please enter valid numbers.")
        return

    delete_all_pdfs()
    downloadPDF(count, start_serial)
    verifyPDFs()
   
 
 
 
 #summary function to update the pdf files



#summary function to extract and analyze the data from the pdf files
# This function will be called when the Analyze button is clicked  
def analyze_and_show():
   #clear_output_screen() 
   extractedText=""
   
   add_text_to_output_screen(f" \n Extracting text from PDF Files....\n\n")
   if platform_type == "Windows":
      add_text_to_output_screen("Platform detected: Windows, Using PyMuPDF for PDF extraction")
   elif platform_type == "Android":
      add_text_to_output_screen("Platform detected: Android, Using PyPDF2 for PDF extraction")   
         
   for i in range(1,7):
      add_text_to_output_screen(f" \n extracting data from PDF file {i}.pdf.....\n")
      
      text=(extractTextFromFile(str(i)+".pdf"))
      extractedText+=text
   
   add_text_to_output_screen(f" \n Data extraction Completed!!\n")
   
   add_text_to_output_screen(f" \n Collecting 4 digit numbers from the data....\n")
   
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
   


#function to open the settings window
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






# Setting up the UI based on the platform
if platform_type == "Windows":
    add_text_to_output_screen("Platform detected: Windows")
   
    mainWindow.state('zoomed')  # Only works on Windows
    bannerImage = bannerImage.resize((400, 150), Image.Resampling.LANCZOS)
    label_file_count.place(x=20, y=230)
    file_count_entry.place(x=400, y=230)

    label_serial_number.place(x=20, y=300)
    serial_number_entry.place(x=400, y=300)
    
    B1.place(x=20,y=400)
    B2.place(x=600,y=400)
    B3.place(x=20,y=550)
    B4.place(x=600,y=550)
    
    outputText.pack(side=tkinter.RIGHT, fill=tkinter.Y)
    outputScrollBar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
    
    
    
elif platform_type == "Android":
    add_text_to_output_screen("Platform detected: Android")
     
    mainWindow.attributes('-fullscreen', True) #set fullscreen or a fixed size for android
    bannerImage = bannerImage.resize((1350, 400), Image.Resampling.LANCZOS)
    
    label_file_count.place(x=20, y=450)
    file_count_entry.place(x=400, y=450)

    label_serial_number.place(x=20, y=550)
    serial_number_entry.place(x=400, y=550)
        
    B1.place(x=20,y=650)
    B2.place(x=600,y=650)
    B3.place(x=20,y=800)
    B4.place(x=600,y=800)
    
    outputText.place(x=20, y=950, width=1300, height=1000)
    outputScrollBar.place(x=1320, y=950, height=1000)
else:
    print("Platform not recognized:", platform_type)
    
    

banner_photo  = ImageTk.PhotoImage(bannerImage)

labelForImage = tkinter.Label(image=banner_photo )
labelForImage.image = banner_photo 
# Position image
labelForImage.place(x=0, y=0)



# --- Configure button properties ---
B1.config(text="Update PDF Files", command=update_pdf_files, bg="#ff44aa")
B2.config(text="Analyze!", command=analyze_and_show, bg="#ff44aa")
B3.config(text="Clear Screen", command=clear_output_screen, bg="#ff44aa")
B4.config(text="Settings", command=openSettingsWindow, bg="#666666")





mainWindow.mainloop()
