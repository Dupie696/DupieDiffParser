class pdfReader():
    def readColumnsFormat(self):
        import textract
        text = textract.process('resources/pdf1.pdf', method='pdfminer')
      
        open("tmp/00_columns.txt", "w").write(text.decode('utf-8'))
        
    def readPageRowFormat(self):
        import PyPDF2
        file = open('resources/pdf1.pdf', 'rb')
        fileReader = PyPDF2.PdfFileReader(file)

        pageRange = range(0,fileReader.numPages)

        pdf = PyPDF2.PdfFileReader(file)

        with open('tmp/00_rows.txt', 'w') as f:
            for x in pageRange:
                pdfpage = pdf.getPage(x)
                f.write(pdfpage.extractText().replace("  ","\n"))
                f.write("----")
