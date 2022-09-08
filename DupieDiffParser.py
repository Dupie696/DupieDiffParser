import classes.pdfReader
import classes.pdfHeaderCleaner
import classes.pdfQuestionIdentify
import os.path

class DupieDiffParser(
    classes.pdfReader.pdfReader,
    classes.pdfHeaderCleaner.pdfHeaderCleaner,
    classes.pdfQuestionIdentify.pdfQuestionIdentify,
                        ):

    def __init__(self):
        if not os.path.exists('tmp/00_columns.txt'):
            self.readColumnsFormat()
        if not os.path.exists('tmp/00_rows.txt'):
            self.readPageRowFormat()

        if not os.path.exists('tmp/01_columns.txt'):
            self.clean_columns_pdf()
        if not os.path.exists('tmp/01_rows.txt'):
            self.clean_rows_pdf()

        self.IdenfityQuestions()



if __name__ == "__main__":
    x = cheatSheetParser()