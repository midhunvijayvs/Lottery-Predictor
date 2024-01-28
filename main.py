from Engine import  Extract
from Engine import Analise

# To convert 6-digit numbers to four-digit numbers
def sixToFour(A):
        N=[]
        for i in range(0,len(A)):
            if Extract.countDigit(A[i])==6:
                d4=A[i]%10000;
                #print(d4)
                N.append(d4)
            else:
                    N.append(A[i])
        print("Six to Four Result:")
        print (N)
        return N
        

def find_largest_index(arr):
    if not arr:
        return -1  # Return -1 if the array is empty

    largest_index = 0

    for i in range(1, len(arr)):
        if arr[i] > arr[largest_index]:
            largest_index = i

    return largest_index


extractedText=""
for i in range(1,7):
    text=(Extract.extractTextFromFile(str(i)+".pdf"))
    extractedText+=text;
array=Extract.splitToIntArray(extractedText)
conditionedArray=Extract.conditionArray(array)
FDN=sixToFour(conditionedArray) #FDN=Four Digit Numbers Array

Analise1=Analise(FDN)

Result=(Analise1.result())
Dig0Result=Result[0]
Dig1Result=Result[1]
Dig2Result=Result[2]
Dig3Result=Result[3]

index=["-0-","-1-","-2-","-3-","-4-","-5-","-6-","-7-","-8-","-9-"]


MostRepeated=[find_largest_index(Dig3Result),find_largest_index(Dig2Result),find_largest_index(Dig1Result),find_largest_index(Dig0Result)]




