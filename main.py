
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
    split_to_words_and_filter_numbers,
    filter_4_digit_numbers,
    sixToFour,
    unpack,
    count,
    analyze,
 format_result_for_display,
 find_most_frequent_digits,
 find_second_most_frequent_digits,
 generate_positional_combinations,
 get_platform,
 show_digit_plots
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

update_pdf_button = tkinter.Button(mainWindow)
analyze_button = tkinter.Button(mainWindow)
show_last_result_button = tkinter.Button(mainWindow)
clear_screen_button = tkinter.Button(mainWindow)
settings_button = tkinter.Button(mainWindow)





# function to print any text to the ouput screen
def add_text_to_output_screen(text, color="green", bold=False):
    tag_name = f"{color}_{'bold' if bold else 'normal'}"
    
    text_color=""
    font_size=10
    
    if (color=="red"):
        text_color="#ff0000"
    elif (color=="yellow"):
        text_color="#ffff00"

    else:
        text_color="#00ff00"
        
    font_weight = "bold" if bold else "normal"    
    
    
    if platform_type == "Windows":
      font_size=10
    elif platform_type == "Android":
      font_size=7
      
    # If the tag doesn't exist yet, configure it
    if not tag_name in outputText.tag_names():
        
        outputText.tag_configure(tag_name, foreground=text_color, font=("Arial", font_size, font_weight))
    
    outputText.insert(tkinter.END, "\n", ())
    outputText.insert(tkinter.END, text, (tag_name,))
    outputText.see(tkinter.END)  # Auto-scroll to the bottom
    outputText.update_idletasks()  # Force UI update

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
   
 
 
 
# function to read row result from file and show the final result in the logger and plot the result
def show_result():
    try:
        with open("last_analysis_report.txt", "r") as f:
            lines = f.readlines()
            Dig0Result = eval(lines[0].strip())
            Dig1Result = eval(lines[1].strip())
            Dig2Result = eval(lines[2].strip())
            Dig3Result = eval(lines[3].strip())

        # Now use Dig0Result through Dig3Result as needed
        show_digit_plots(Dig0Result, Dig1Result, Dig2Result, Dig3Result)

    except Exception as e:
        add_text_to_output_screen(f"Error loading analysis result from file:, {e}","red",True)
        return
        
    add_text_to_output_screen("Raw Result")
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
    add_text_to_output_screen("Final Result: ", color="yellow", bold=True)
    add_text_to_output_screen("--------------------------------------------------")
    for row in formattedResultToDisplay:
       add_text_to_output_screen(row, color="yellow", bold=True)

    add_new_line_to_output_screen()
    add_text_to_output_screen("--------------------------------------------------")
    add_new_line_to_output_screen()

    # show most repeated digits
    add_text_to_output_screen("Most Repeated Digits: ", color="yellow", bold=True)
    add_text_to_output_screen(mostRepeatedDigits, color="yellow", bold=True)
    add_new_line_to_output_screen()
    add_text_to_output_screen("--------------------------------------------------")
    add_new_line_to_output_screen()
    add_text_to_output_screen("Second Most Repeated Digits: ", color="yellow", bold=True)
    add_text_to_output_screen(secondMostRepeatedDigits, color="yellow", bold=True)
    add_text_to_output_screen("--------------------------------------------------")
   
    #Show positional combinations of the most repeated digits
    add_new_line_to_output_screen()
    add_text_to_output_screen("Positional Combinations: ", color="yellow", bold=True)
    add_text_to_output_screen("--------------------------------------------------")
    positionalCombinations=generate_positional_combinations(mostRepeatedDigits, secondMostRepeatedDigits)
   
    add_text_to_output_screen(positionalCombinations, color="yellow", bold=True)

    show_digit_plots(Dig0Result, Dig1Result, Dig2Result, Dig3Result)



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
   
   
   try:
        count = int(file_count_entry.get())
        
   except ValueError:
        add_text_to_output_screen("Input Error!! Please enter valid numbers.")
        return
      
   for i in range(1,count+1):
      add_text_to_output_screen(f" \n extracting data from PDF file {i}.pdf.....\n")
      
      text=(extractTextFromFile(str(i)+".pdf"))
      extractedText+=text
   
   add_text_to_output_screen(f" \n Data extraction Completed!!\n\n")
   
   add_text_to_output_screen(f" \n Splitting the text data into words and filtering numbers....\n")
   numbers_array=split_to_words_and_filter_numbers(extractedText)
   add_new_line_to_output_screen()
   add_text_to_output_screen(f" \n Data Splitting and filtering completed!!\n")
   add_text_to_output_screen(f"  The result number word array is\n\n{numbers_array}\n\n")
   
   add_text_to_output_screen(f" \n Collecting 4 digit numbers from the data....\n")

   four_digit_numbers=filter_4_digit_numbers(numbers_array)
   
   #FDN=sixToFour(four_digit_numbers) #FDN=Four Digit Numbers Array
   
   add_text_to_output_screen("\n\nExtracted 4 digit numbers from all the pdf files:")
   add_text_to_output_screen("------------------------------------------")
   add_new_line_to_output_screen()

   add_text_to_output_screen(four_digit_numbers)
    
   add_new_line_to_output_screen()
   add_text_to_output_screen(f" \n Collected all 4 digit numbers!!\n")
   add_new_line_to_output_screen()
    
   add_text_to_output_screen("Total number of numbers in the above list: "+str(len(four_digit_numbers)))
   add_new_line_to_output_screen()
   add_text_to_output_screen(f"Total number of pdf files:{count} ")
   add_text_to_output_screen(f"Expected number of 4 digit results per files: 606")
   add_text_to_output_screen(f"Total number of expected 4 digit results :{count} x 606 = {count*606}")
   add_new_line_to_output_screen()
   add_text_to_output_screen("------------------------------------------------------------------------------")
    
   add_new_line_to_output_screen()
   add_new_line_to_output_screen() 
    
   
   

   Dig0Result, Dig1Result, Dig2Result, Dig3Result=analyze(four_digit_numbers)
   
   with open("last_analysis_report.txt", "w") as f:
    f.write(repr(Dig0Result) + "\n")
    f.write(repr(Dig1Result) + "\n")
    f.write(repr(Dig2Result) + "\n")
    f.write(repr(Dig3Result) + "\n")
    
   show_result()
    
   
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
    add_text_to_output_screen("Platform detected: Windows\n")
   
    mainWindow.state('zoomed')  # Only works on Windows
    bannerImage = bannerImage.resize((400, 150), Image.Resampling.LANCZOS)
    label_file_count.place(x=20, y=230)
    file_count_entry.place(x=400, y=230)

    label_serial_number.place(x=20, y=300)
    serial_number_entry.place(x=400, y=300)
    
    update_pdf_button.place(x=20,y=400)
    analyze_button.place(x=200,y=400)
    show_last_result_button.place(x=300,y=400)
    clear_screen_button.place(x=20,y=550)
    settings_button.place(x=600,y=550)
    
    outputText.pack(side=tkinter.RIGHT, fill=tkinter.Y)
    outputScrollBar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
    
    
    
elif platform_type == "Android":
    add_text_to_output_screen("Platform detected: Android\n")
     
    mainWindow.attributes('-fullscreen', True) #set fullscreen or a fixed size for android
    bannerImage = bannerImage.resize((1350, 400), Image.Resampling.LANCZOS)
    
    label_file_count.place(x=20, y=450)
    file_count_entry.place(x=400, y=450)

    label_serial_number.place(x=20, y=550)
    serial_number_entry.place(x=400, y=550)
        
    update_pdf_button.place(x=20,y=650)
    analyze_button.place(x=600,y=650)
    show_last_result_button.place(x=900,y=650)
    clear_screen_button.place(x=20,y=800)
    settings_button.place(x=600,y=800)
    
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
update_pdf_button.config(text="Update PDF Files", command=update_pdf_files, bg="#ff44aa")
analyze_button.config(text="Analyze!", command=analyze_and_show, bg="#ff44aa")
show_last_result_button.config(text="Show Last Result!", command=show_result, bg="#ff44aa")
clear_screen_button.config(text="Clear Screen", command=clear_output_screen, bg="#ff44aa")
settings_button.config(text="Settings", command=openSettingsWindow, bg="#666666")





mainWindow.mainloop()
