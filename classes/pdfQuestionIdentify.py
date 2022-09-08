import re

class pdfQuestionIdentify():
    def IdenfityQuestions(self):

        self.document0col = open('tmp/01_columns.txt', 'r')
        self.document0row = open('tmp/01_rows.txt', 'r')
        self.mycharacterR = self.document0row.read(1)
        self.mycharacterC = self.document0col.read(1)



        self.skipwhitespace()

        for x in range(0,30):

            
            x = self.showmatches()
            print ("M:[%(coltell)s,%(rowtell)s]%(matched_string)s" % x)

            # y,z = self.debugprint()
            # print ("D:[%(coltell)s,%(rowtell)s]%(matched_string)s" % y)
            # print ("D:[%(coltell)s,%(rowtell)s]%(matched_string)s" % z)

            y,z = self.seekformatches_skipwhitespace()
            print ("U:[%(coltell)s,%(rowtell)s]%(matched_string)s" % y)
            print ("U:[%(coltell)s,%(rowtell)s]%(matched_string)s" % z)

            print ()

#            self.seekformatches()


    def skipwhitespace(self):
        while self.mycharacterR in ["\x0a","\x20"]:
            self.mycharacterR = self.document0row.read(1)

        while self.mycharacterC in ["\x0a","\x20"]:
            self.mycharacterC = self.document0col.read(1)

    def showmatches(self):
        # matched_string = ""

        dto = {
            "coltell": self.document0col.tell(),
            "rowtell": self.document0row.tell(),
            "matched_string":"",
                }
        while self.mycharacterR == self.mycharacterC:
            #print (self.mycharacterR,end="")
            dto["matched_string"] += self.mycharacterR
            self.mycharacterR = self.document0row.read(1)
            self.mycharacterC = self.document0col.read(1)

        return dto

    def debugprint(self):
        dto_col = {
            "coltell": self.document0col.tell(),
            "rowtell": "x",
            "matched_string":hex(ord(self.mycharacterC)),
                }
        dto_rows = {
            "coltell": "x",
            "rowtell": self.document0row.tell(),
            "matched_string":hex(ord(self.mycharacterR)),
                }
        return dto_col,dto_rows

    def seekformatches_skipwhitespace(self):
        ctell_1 = self.document0col.tell()
        rtell_1 = self.document0row.tell()

        self.skipwhitespace()

        if self.mycharacterR == self.mycharacterC:
            ctell_2 = self.document0col.tell()
            rtell_2 = self.document0row.tell()

            self.document0col.seek(ctell_1)
            clist = []
            for c in range(0,(ctell_2-ctell_1)):
                chex = hex(ord(self.document0col.read(1)))
                clist.append(chex)

            self.document0row.seek(rtell_1)
            rlist = []
            for r in range(0,(rtell_2-rtell_1)):
                rhex = hex(ord(self.document0row.read(1)))
                rlist.append(rhex)

            self.document0col.seek(ctell_2)
            self.document0row.seek(rtell_2)


            print ("(%s->%s),(%s->%s)" % (ctell_2,ctell_1,rtell_2,rtell_1))

            dto_col = {
                "coltell": ctell_1,
                "rowtell": "x",
                "matched_string":" ".join(clist),
                    }
            dto_rows = {
                "coltell": "x",
                "rowtell": rtell_1,
                "matched_string":" ".join(rlist),
                    }

            return dto_col,dto_rows

        elif self.mycharacterR == "S" or self.mycharacterR == "N":
            rtell_2 = self.document0row.tell()
            nextchar = self.document0row.read(1)

            dto_col = {
                "coltell": "x",
                "rowtell": "x",
                "matched_string":"",
                    }

            if self.mycharacterR == "S" and nextchar == "i":

                dto_rows = {
                    "coltell": "x",
                    "rowtell": rtell_2,
                    "matched_string":"Si",
                        }
                self.mycharacterR = self.document0row.read(1)
                self.skipwhitespace()
                return dto_col,dto_rows

            elif self.mycharacterR == "N" and nextchar == "o":
                dto_rows = {
                    "coltell": "x",
                    "rowtell": rtell_2,
                    "matched_string":"No",
                        }
                self.mycharacterR = self.document0row.read(1)
                self.skipwhitespace()
                return dto_col,dto_rows
            else:
                 raise BaseException("ehh?")



        raise BaseException("ehh?")



    def seekformatches(self):
        pass
