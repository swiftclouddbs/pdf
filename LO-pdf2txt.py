##from PyPDF2 import PdfReader
##
##reader = PdfReader("/Users/reginaldstuart/Documents/IT/python/pdf/TheLittleOfficeOfIC-Dublin 1848.pdf")
##page = reader.pages[13]
##print(page.extract_text())

import os, glob, PyPDF2, sys, re

#Check for file and delete if needed

##file_path = "/Users/reginaldstuart/Documents/IT/python/pdf/LO.txt"
##
##if os.path.exists(file_path):
##     os.remove(file_path)
##      print("File removed.")
##else:
##      print("No file here")


file_path = '/Users/reginaldstuart/Documents/IT/python/pdf/'
read_files = glob.glob(os.path.join(file_path,'*.pdf'))

finished = open("/Users/reginaldstuart/Documents/IT/python/pdf/LO.txt","a")

for files in read_files:
    pdfReader = PyPDF2.PdfReader(files)
    count = len(pdfReader.pages)
    output = []
    for i in range(count):
        page = pdfReader.pages[i]
        match("\n", "\\n").replace("\r", "\\r")
        output.append(page.extract_text())
    print(output, file = finished)

finished.close()
