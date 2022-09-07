import re

class pdfHeaderCleaner():
    def clean_columns_pdf(self):
        document0 = open('tmp/00_columns.txt', 'r').read()

        regx = """([\x20\x0a]*
Nota: El color verde indica que la opción es la correcta,  el color rojo indica  que la opción es incorrecta.[\x20]*
[\x20]*)?
CORTE SUPREMA DE JUSTICIA[\x20]*
EXAMEN DE NOTARIADO 2021[\x20]*

Cuestionario Jornada \d:[\x20]*

Sábado 4 de diciembre de 9:20 a.m. a 11:00 a.m.[\x20]*
([\x0a\x20]*
PREGUNTAS[\x20]*
[\x20]*
RESPUESTA[\x20]*
CORRECTA[\x20]*)?"""
        document = re.sub(regx, "", document0)


        regx = """Página \d+ de \d+"""
        document = re.sub(regx, "", document)


        # print (document0[:4000])
        # print("="*80)
        # print(document[:4000])

#        print(res_str[:4000].replace("ICIA\x20\x0aEX",""))
#        print(res_str[:4000].replace("\x49\x41\x20\x0a\x45\x58",""))
        open("tmp/01_columns.txt", "w").write(document)




    def clean_rows_pdf(self):
        document0 = open('tmp/00_rows.txt', 'r').read()
        
        regx = """[\x20\x0a]*
CORTE SUPREMA DE JUSTICIA EXAMEN DE NOTARIADO 2021 Cuestionario Jornada \d:
Sábado 4 de diciembre de 9:20 a.m. a 11:00 a.m.[\x20]*
([\x0a\x20]*
Página \d+ de \d+
[\x0a\x20]*
*Nota: El color verde indica que la opción es la correcta,
el color rojo indica
que la opción es incorrecta.
PREGUNTAS RESPUESTA CORRECTA)?"""
        document = re.sub(regx, "", document0)


        regx = """Página \d+ de \d+"""
        document = re.sub(regx, "", document)


        print (document0[:4000])
        print("="*80)
        print(document[:4000])

#        print(res_str[:4000].replace("ICIA\x20\x0aEX",""))
#        print(res_str[:4000].replace("\x49\x41\x20\x0a\x45\x58",""))
        open("tmp/01_rows.txt", "w").write(document)