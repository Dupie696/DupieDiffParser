import re

class pdfQuestionIdentify():
    def IdenfityQuestions(self):

        self.document0col = open('tmp/01_columns.txt', 'r')
        self.document0row = open('tmp/01_rows.txt', 'r')
        self.mycharacterR = self.document0row.read(1)
        self.mycharacterC = self.document0col.read(1)



        for x in range(0,50):
            self.skipwhitespace()

            x = self.showmatches()
            print (x)

            self.debugprint()

    def skipwhitespace(self):
        while self.mycharacterR in ["\x0a","\x20"]:
            self.mycharacterR = self.document0row.read(1)

        while self.mycharacterC in ["\x0a","\x20"]:
            self.mycharacterC = self.document0col.read(1)

    def showmatches(self):
        ret = ""
        while self.mycharacterR == self.mycharacterC:
            #print (self.mycharacterR,end="")
            ret += self.mycharacterR
            self.mycharacterR = self.document0row.read(1)
            self.mycharacterC = self.document0col.read(1)
        return ret

    def debugprint(self):
        print ()
        print ()
        print ("r:", hex(ord(self.mycharacterR)), "c:",hex(ord(self.mycharacterC)))
        print ("break")
        print ()
