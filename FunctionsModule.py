# Import libraries
import os
import glob
import requests
from bs4 import BeautifulSoup
import fitz  # this is pymupdf;  use the command "pip install PyMuPDF" in OS terminal to install this library


#*******************************************************************************
#following are the functions for downloading the pdf files
def delete_all_pdfs(folder="pdf-downloads"):
    if not os.path.exists(folder):
        print(f"Folder '{folder}' does not exist.")
        return

    pdf_files = glob.glob(os.path.join(folder, "*.pdf"))

    if not pdf_files:
        print("No PDF files found to delete.")
        return

    for file_path in pdf_files:
        try:
            os.remove(file_path)
            print(f"Deleted: {file_path}")
        except Exception as e:
            print(f"Error deleting {file_path}: {e}")

    print("All PDF files deleted.")
    
    
def downloadPDF(noOfFilesToDownload, startingSerialNumber):
    folder = "pdf-downloads"
    os.makedirs(folder, exist_ok=True)

    for i in range(1, noOfFilesToDownload + 1):  # Starting from 1
        url = f"https://result.keralalotteries.com/viewlotisresult.php?drawserial={startingSerialNumber + i - 1}"
        print(f"Downloading from: {url}")
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            content_type = response.headers.get("Content-Type", "")

            if "application/pdf" not in content_type:
                print(f"Skipped {i}: Not a PDF file.")
                continue

            file_path = os.path.join(folder, f"{i}.pdf")  # Saving as 1.pdf, 2.pdf, etc.
            with open(file_path, 'wb') as pdf:
                pdf.write(response.content)
            print(f"Saved to {file_path}")
        except Exception as e:
            print(f"Error downloading {i}: {e}")

    print("Download complete.")


def verifyPDFs(folder="pdf-downloads"):
    pdf_files = glob.glob(os.path.join(folder, "*.pdf"))
    deleted = []
    kept = []

    for file in pdf_files:
        if os.path.getsize(file) == 0:
            os.remove(file)
            deleted.append(os.path.basename(file))
        else:
            kept.append(os.path.basename(file))

    report = (
        f"✅ Verified PDF files in '{folder}':\n\n"
        f"📁 Total files scanned: {len(pdf_files)}\n"
        f"🗑️  Deleted empty files: {len(deleted)}\n"
        f"📌 Valid files kept: {len(kept)}\n"
    )

    if deleted:
        report += "\n🗑️ Deleted Files:\n" + "\n".join(deleted)

    if kept:
        report += "\n\n📌 Valid Files:\n" + "\n".join(kept)

    return report


#*******************************************************************************
#following are the functions for extracting text from the pdf files
def countDigit(n):
    count = 0
    while n != 0:
            n //= 10
            count += 1
    return count
	
#to extract text from all the pages of the pdf into a single string
def extractTextFromFile(filename):
    folder = "pdf-downloads"
    full_path = os.path.join(folder, filename)

    if not os.path.exists(full_path):
        print(f"File not found: {full_path}")
        return ""

    with fitz.open(full_path) as doc:
        text = ""
        for page in doc:
            text += page.get_text()
    return text


#to split the string to list of words and to filter them to int values only
def splitToIntArray(s):
    numbers = []

    for word in s.split():   

            if word.isdigit():

                    numbers.append(int(word))
    return numbers

        #to remove consolidation prize repitation
	#To remove page numbers and other unwanted value 30
	# A slight logical error exsist in indexing. clarify on implementation which requires high precision     

#removing some unwanted values
#and the first 12 items
def conditionArray(A):
    A = A[12:]  # remove first 12 items
    A = [v for v in A if v not in {1, 2, 3, 30}]
    return A



def sixToFour(A):
    N=[]
    for i in range(0,len(A)):
        if countDigit(A[i])==6:
            d4=A[i]%10000
            #print(d4)
            N.append(d4)
        else:
                N.append(A[i])
    print("Six to Four Result:")
    print (N)
    return N
        

#*******************************************************************************
#following are the functions for analyzing the extracted text



def unpack(a):
    dig3=[]
    dig2=[]
    dig1=[]
    dig0=[]

    for y in range(0,len(a)):
            temp=a[y]
            dig0.append(temp%10)
            temp=int(temp/10)
            dig1.append(temp%10)
            temp=int(temp/10)
            dig2.append(temp%10)
            temp=int(temp/10)
            dig3.append(temp%10)
   
    return dig0,dig1,dig2,dig3


        
def count(digitArray):
    result=[0,0,0,0,0,0,0,0,0,0]
    for i in range(0,len(digitArray)):
            if digitArray[i]==0:
                    result[0]+=1
            elif digitArray[i]==1:
                    result[1]+=1
            elif digitArray[i]==2:
                    result[2]+=1
            elif digitArray[i]==3:
                    result[3]+=1
            elif digitArray[i]==4:
                    result[4]+=1
            elif digitArray[i]==5:
                    result[5]+=1
            elif digitArray[i]==6:
                    result[6]+=1
            elif digitArray[i]==7:
                    result[7]+=1
            elif digitArray[i]==8:
                    result[8]+=1
            elif digitArray[i]==9:
                    result[9]+=1
    return result



def analize(array):
 
    digit0,digit1,digit2,digit3=unpack(array)
    D0Result=count(digit0)
    D1Result=count(digit1)
    D2Result=count(digit2)
    D3Result=count(digit3)

    
    return D0Result, D1Result, D2Result, D3Result



def format_result_for_display(Dig3Result, Dig2Result, Dig1Result, Dig0Result):
    """Creates a 2D array combining digit position results into rows by digit (0-9).

    Each row format: [digit, Dig3, Dig2, Dig1, Dig0]"""
    result = []
    for i in range(10):
        row = [i, Dig3Result[i], Dig2Result[i], Dig1Result[i], Dig0Result[i]]
        result.append(row)
    return result


def find_most_frequent_digits(Dig3Result, Dig2Result, Dig1Result, Dig0Result):
    """
    Returns the most frequent digit (0–9) at each digit position.
    
    Output format:
        [MostCommonAtD3, MostCommonAtD2, MostCommonAtD1, MostCommonAtD0]
    """
    return [
        Dig3Result.index(max(Dig3Result)),
        Dig2Result.index(max(Dig2Result)),
        Dig1Result.index(max(Dig1Result)),
        Dig0Result.index(max(Dig0Result)),
    ]


def find_second_most_frequent_digits(Dig3Result, Dig2Result, Dig1Result, Dig0Result):
    """
    Returns the second most frequent digit (0–9) at each digit position.
    
    Output format:
        [SecondMostAtD3, SecondMostAtD2, SecondMostAtD1, SecondMostAtD0]
    """
    result = []
    for position_result in [Dig3Result, Dig2Result, Dig1Result, Dig0Result]:
        # Get a list of (digit, count) pairs and sort by count in descending order
        sorted_counts = sorted(enumerate(position_result), key=lambda x: x[1], reverse=True)
        # Get the digit with the second highest count
        second_most = sorted_counts[1][0] if len(sorted_counts) > 1 else -1  # -1 if not available
        result.append(second_most)
    return result