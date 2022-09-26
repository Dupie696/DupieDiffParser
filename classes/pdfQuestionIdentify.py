import re


template_string = "\n%(symbol)s:[%(coltell1)s-%(coltell2)s,%(rowtell1)s-%(rowtell2)s]%(matched_string)s"

class pdfQuestionIdentify():
    def IdenfityQuestions(self):

        self.document0col = open('tmp/01_columns.txt', 'r')
        self.document0row = open('tmp/01_rows.txt', 'r')

        # always point at the next character
        self.mycharacterR = self.document0row.read(1)
        self.mycharacterC = self.document0col.read(1)

        print ("Lengend: _[c,r]")

        y,z = self.skipwhitespace()
        print (template_string % y, template_string % z)

        y,z = self.debugprint()
        print ("N:[%(coltell)s,%(rowtell)s]%(character)s(%(hex)s)" % y)
        print ("N:[%(coltell)s,%(rowtell)s]%(character)s(%(hex)s)" % z)

        print ()

        for x in range(0,1):

            
            y,z = self.showmatches()
            print (template_string % y, template_string % z)

            y,z = self.debugprint()
            print ("N:[%(coltell)s,%(rowtell)s]%(character)s(%(hex)s)" % y)
            print ("N:[%(coltell)s,%(rowtell)s]%(character)s(%(hex)s)" % z)

            print ()

            y,z = self.seekformatches_skipwhitespace()
            print ("U:[%(coltell)s,%(rowtell)s]%(matched_string)s" % y)
            print ("U:[%(coltell)s,%(rowtell)s]%(matched_string)s" % z)

            print ()



    def printer(self,myParsers):
        y,z = myParsers
        print (template_string % y, template_string % z)

    def skipwhitespace(self):
        dto_col = {
            "coltell1": self.document0col.tell()
            }
        dto_row = {
            "rowtell1": self.document0row.tell()
            }
        rlist = []
        clist = []
        
        
        while self.mycharacterR in ["\x0a","\x20"]:
            rhex = hex(ord(self.mycharacterR))
            rlist.append(rhex)
            self.mycharacterR = self.document0row.read(1)

        while self.mycharacterC in ["\x0a","\x20"]: 
            chex = hex(ord(self.mycharacterC))
            clist.append(chex)
            self.mycharacterC = self.document0col.read(1)

        ctell_2 = self.document0col.tell()
        rtell_2 = self.document0row.tell()

        dto_col |= {
            "coltell2": ctell_2-1,
            "rowtell1": "x",
            "rowtell2": "x",
            "matched_string":" ".join(clist),
            "symbol": "W"
                }
        dto_row |= {
            "coltell1": "x",
            "coltell2": "x",
            "rowtell2": rtell_2-1,
            "matched_string":" ".join(rlist),
            "symbol": "W"
                }

        return dto_col,dto_row






    def showmatches(self):
        """

        Returns the matched characters and position information

        """


        dto_col = {
            "coltell1": self.document0col.tell()
            }
        dto_row = {
            "rowtell1": self.document0row.tell()
            }

        mlist = ""


        while self.mycharacterR == self.mycharacterC:
            mlist += self.mycharacterR
            self.mycharacterR = self.document0row.read(1)
            self.mycharacterC = self.document0col.read(1)


        ctell_2 = self.document0col.tell()
        rtell_2 = self.document0row.tell()

        dto_col = {
            "coltell1": dto_col["coltell1"],
            "coltell2": ctell_2-1,
            "rowtell1": dto_row["rowtell1"],
            "rowtell2": rtell_2-1,
            "matched_string":"".join(mlist),
            "symbol": "M"
                }
        dto_rows = {
            "coltell1": dto_col["coltell1"],
            "coltell2": ctell_2-1,
            "rowtell1": dto_row["rowtell1"],
            "rowtell2": rtell_2-1,
            "matched_string":"".join(mlist),
            "symbol": "M"
                }


        return dto_col,dto_rows





    def debugprint(self):
        dto_col = {
            "coltell": self.document0col.tell(),
            "rowtell": "x",
            "character": self.mycharacterC,
            "hex":hex(ord(self.mycharacterC)),
                }
        dto_rows = {
            "coltell": "x",
            "rowtell": self.document0row.tell(),
            "character": self.mycharacterR,
            "hex":hex(ord(self.mycharacterR)),
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
