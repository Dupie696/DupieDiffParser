#install pyDF2
#pip install PyPDF2

# importing all the required modules
import PyPDF2

# creating an object 
file = open('pdf1.pdf', 'rb')

# creating a pdf reader object
fileReader = PyPDF2.PdfFileReader(file)

# print the number of pages in pdf file
print(fileReader.numPages)

from PyPDF2 import PdfFileReader

with open('pdf1.pdf', 'rb') as f:
    pdf = PdfFileReader(f)
    # get the first page
    page = pdf.getPage(1)
    print(page)
    print('Page type: {}'.format(str(type(page))))
    text = page.extractText()
    print(str(text).replace("  ","\n"))