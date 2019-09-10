import os
import sys
import PyPDF2
import camelot


def pdf_tables_csv(pdf_list):
    for pdf_name in pdf_list:
        pdf_file = open(pdf_name, 'rb')
        read_pdf = PyPDF2.PdfFileReader(pdf_file)

        for pageNum in range(1, read_pdf.numPages + 1):
            tables = camelot.read_pdf(pdf_name, pages=str(pageNum))
            tables.export(f'{os.path.splitext(pdf_name)[0]}.csv', f='csv')

        pdf_file.close()


if __name__ == "__main__":
    pdf_tables_csv(sys.argv[1:])
