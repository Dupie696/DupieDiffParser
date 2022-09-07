import re

class lawclass():
    def __init__(self,pdffile,wordfile):
        self.pdffile = open(pdffile, "r").read()
        self.wordfile = open(wordfile, "r").read()
        self._basic_cleanup()
        #print(self.pdffile[:1000])
        self._breakup_question2()


    def _basic_cleanup(self):
        file1Header = """CORTE SUPREMA DE JUSTICIA
EXAMEN DE NOTARIADO 2021
Cuestionario Jornada \d: 
Sábado 4 de diciembre de 9:20 a.m. a 11:00 a.m.
Página \d+ de \d+
(Nota: El color verde indica que la opción es la correcta, el color rojo indica que la opción es incorrecta.
PREGUNTAS
RESPUESTA 
CORRECTA)?""".replace("\n","\\n")
        self.pdffile = re.sub(file1Header, "", self.pdffile)

        if self.pdffile[0:1] == "\n":
            self.pdffile = self.pdffile[1:]

    def _breakup_question(self):
        counter = 0
        startat = 0
        question = 0
        for index, z in enumerate(self.pdffile.split("\n")):
            if z[-2:] == "Si" or z[-2:] == "No":
                counter +=1
                print ("%s %s" % (counter,index))

                if counter == 4:
                    print ("\n".join(self.pdffile.split("\n")[startat:index+1]))
                    startat = index+1
                    counter = 0
                    question +=1
                    print ("---------------------")

                if question == 10:
                    exit(0)

    def _breakup_question2(self):

        _dict = {}


        for index, z in enumerate(self.pdffile.split("\n")[:20]):
            print (index,z)

            if "first" not in _dict:
                _dict["first"] = z
                continue
            
            if z[-2:] == "Si" or z[-2:] == "No":
                if "answers" not in _dict:
                    _dict["answers"] = []
                _dict["answers"] = _dict["answers"] + [z]
                continue     
            else: 
                if "muddy" not in _dict:
                    _dict["muddy"] = []
                _dict["muddy"].append(z)                
                continue     
        
        import pprint

        print(pprint.pformat(_dict["answers"][1]))
        print(type(_dict["answers"][1]))
        print(_dict["answers"][1])



if __name__ == "__main__":
    lc = lawclass("law.txt","law3.txt")

