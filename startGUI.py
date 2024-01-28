import main
import tkinter as tk
from tkinter import scrolledtext
import tkinter.ttk as ttk  # pack for styling. if you don't want modern styling, just use tk. instead of ttk.
from PIL import Image, ImageTk
from updatePDFfiles import handleUpdatePDFFiles
def openAnalysesWindow():
    table_frame.place(x=0, y=0)

def closeAnalysesWindow():
    table_frame.place_forget()

def updatePDFFiles():
    today_result_serial = today_result_serial_entry.get()

    if today_result_serial:
        log_area.delete("1.0", tk.END)  # Clear the log area
        log_area.insert(tk.END, "Updating PDF files...\n")

        today_result_serial = int(today_result_serial)
        handleUpdatePDFFiles(today_result_serial, log_area)

    else:
        log_area.insert(tk.END, "Please enter a value for Draw Serial From.")


mainWindow = tk.Tk()
mainWindow.geometry("600x600")  # Adjust the dimensions as needed
mainWindow.title("Lottery Analyzer")
mainWindow.configure(bg='#222222')

image1 = Image.open("./image.png")
test = ImageTk.PhotoImage(image1)

label1 = ttk.Label(image=test)
label1.image = test
label1.pack()

today_result_serial_label = ttk.Label(mainWindow, text="Draw Serial From:")
today_result_serial_label.place(x=10, y=300)
today_result_serial_entry = ttk.Entry(mainWindow)
today_result_serial_entry.place(x=110, y=300)

number_of_results_to_fetch_label = ttk.Label(mainWindow, text="No. of results to fetch:")
number_of_results_to_fetch_label.place(x=10, y=330)
number_of_results_to_fetch_entry = ttk.Entry(mainWindow)
number_of_results_to_fetch_entry.place(x=110, y=330)

update_button = ttk.Button(mainWindow, text="Update PDF files", command=updatePDFFiles)
update_button.place(x=10, y=360)

log_area = scrolledtext.ScrolledText(mainWindow, height=17, width=40, foreground="#00ff00", bg="#333333")
log_area.pack()
log_area.place(x=250, y=300)

B1 = ttk.Button(mainWindow, text="Analyze!", command=openAnalysesWindow)
B1.pack()
B1.place(x=50, y=450)

table_frame = tk.Frame(mainWindow, width=780, height=400, bg="#121212")

back_button = ttk.Button(table_frame, text="Back", command=closeAnalysesWindow, )
back_button.grid(row=0, column=0, padx=10, pady=5, sticky='nw')


# Create labels to display the results
column_labels = ["Digit", "4th", "3rd", "2nd", "1st"]
for col_idx, col_label in enumerate(column_labels):
    label = tk.Label(table_frame,background="#121212", foreground="#ccffcc", text=col_label, font=('Helvetica', 12, 'bold'))
    label.grid(row=1, column=col_idx, padx=10, pady=5)

# Populate the table with data
results = [main.index, main.Dig3Result, main.Dig2Result, main.Dig1Result, main.Dig0Result]
for row_idx in range(10):
    for col_idx in range(5):
        result = results[col_idx][row_idx]
        label = tk.Label(table_frame, text=result, font=('Helvetica', 10), background="#121212", foreground="#fcfcfc")
        label.grid(row=row_idx + 2, column=col_idx, padx=10, pady=5)

for col_idx in range(4):
    finalResult = tk.Label(table_frame, text=str(main.MostRepeated[col_idx]), font=('Helvetica', 15, 'bold'), height=2, width=4, foreground="#22cc22", bg="#333333")
    finalResult.grid(row=12, column=col_idx+1, padx=10, pady=5)

mainWindow.mainloop()
