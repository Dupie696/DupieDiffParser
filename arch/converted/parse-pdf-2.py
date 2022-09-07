import textract
text = textract.process('pdf1.pdf', method='pdfminer')
print (str(text)[:4000].replace("\\n","\n"))