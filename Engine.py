import fitz  # this is pymupdf;  use the command "pip install PyMuPDF" in OS terminal to install this library


class Extract:
    def countDigit(n):
        count = 0
        while n != 0:
            n //= 10
            count += 1
        return count

    # to extract text from all the pages of the pdf into a single string
    def extractTextFromFile(filename):
        with fitz.open(filename) as doc:
            text = ""
            for page in doc:
                text += page.getText()

        return text

    # to split the string to list of words and to filter them to int values only
    def splitToIntArray(s):
        numbers = []

        for word in s.split():

            if word.isdigit():
                numbers.append(int(word))
        return numbers

    # to remove consolidation prize repitation
    # To remove page numbers and other unwanted value 30
    # A slight logical error exsist in indexing. clarify on implementation which requires high precision

    def conditionArray(A):
        for i in range(1, 12):
            A.pop(0)

        for v in A:
            if v == 1:
                A.pop(A.index(v))
            elif v == 2:
                A.pop(A.index(v))
            elif v == 3:
                A.pop(A.index(v))
            elif v == 30:
                A.pop(A.index(v))

        return A


class Analise:

    def unpack(self, a):
        dig3 = []
        dig2 = []
        dig1 = []
        dig0 = []
        global digit0
        global digit1
        global digit2
        global digit3
        for y in range(0, len(a)):
            temp = a[y]
            dig0.append(temp % 10)
            temp = int(temp / 10)
            dig1.append(temp % 10)
            temp = int(temp / 10)
            dig2.append(temp % 10)
            temp = int(temp / 10)
            dig3.append(temp % 10)
        digit0 = dig0
        digit1 = dig1
        digit2 = dig2
        digit3 = dig3
        print("Digit0 inside function:")
        print(digit0)

    def count(self, digitArray):
        result = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(0, len(digitArray)):
            if digitArray[i] == 0:
                result[0] += 1
            elif digitArray[i] == 1:
                result[1] += 1
            elif digitArray[i] == 2:
                result[2] += 1
            elif digitArray[i] == 3:
                result[3] += 1
            elif digitArray[i] == 4:
                result[4] += 1
            elif digitArray[i] == 5:
                result[5] += 1
            elif digitArray[i] == 6:
                result[6] += 1
            elif digitArray[i] == 7:
                result[7] += 1
            elif digitArray[i] == 8:
                result[8] += 1
            elif digitArray[i] == 9:
                result[9] += 1
        return result

    def __init__(self, array):
        global D0Result
        global D1Result
        global D2Result
        global D3Result
        self.unpack(array)
        D0Result = self.count(digit0)
        D1Result = self.count(digit1)
        D2Result = self.count(digit2)
        D3Result = self.count(digit3)

    def result(self):
        return D0Result, D1Result, D2Result, D3Result
