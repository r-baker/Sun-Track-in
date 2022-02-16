# Push altitude and azimut of present time of the sun
from PyPDF2 import PdfFileReader


# Altitude: FLOAT
# Azimut: FLOAT

def check_suncalc():
    # pdf_file = open('sun data/suncalc data.pdf', 'rb')  # change pdf name, what is rb
    # read_pdf = PyPDF2.PdfFileReader(pdf_file)
    # number_of_pages = read_pdf.getNumPages()
    # page = read_pdf.getPage(0)
    # page_content = page.extracText()
    # print(page_content.encode('utf-8'), flush=True)
    pdfFile = open('sun data/suncalc data.pdf', 'rb')
    pdfReader = PdfFileReader(pdfFile)
    print("Printing the document info: " + str(pdfReader.getDocumentInfo()))
    print("- - - - - - - - - - - - - - - - - - - -")
    print("Number of Pages: " + str(pdfReader.getNumPages()))
    numofpages = pdfReader.getNumPages()
    for i in range(0, numofpages):
        print("Page Number: "+str(i))
        print("-----")
        pageobj = pdfReader.getPage(i)
        print(pageobj.getContents())
        print("-----")
    pdfFile.close()


check_suncalc()
