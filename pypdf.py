import os
from pathlib import Path
from decimal import Decimal 
# import third party libraries:
from borb.pdf import Document
from borb.pdf.page.page import Page
from borb.pdf.canvas.layout.page_layout.multi_column_layout import SingleColumnLayout
from borb.pdf.canvas.layout.image.image import Image
from borb.pdf.pdf import PDF

# NOTICE BELOW THE TYPE IS CONVERTED TO Path using pathlib
IMAGE_PATH = Path(r"C:\Users\...\image.png") #change to fit your path

def create_pdf (pdf_filename , outp_folder):
    os.makedirs(outp_folder, exist_ok=True)
    pdf_filepath = os.path.join(outp_folder, pdf_filename + ".pdf")
    pdf = Document()
    page = Page()
    pdf.add_page(page)
    page_layout = SingleColumnLayout(page)
    page_layout.vertical_margin = page.get_page_info().get_height() *     Decimal(0.02)
    page_layout.add(
         Image("http://foo.bar/image.jpg", width=1, height=1)) #change the size as you wish
    LayoutElement = Image
    with open(pdf_filepath, "wb") as pdf_file_handle:
        PDF.dumps(pdf_file_handle, pdf)


if __name__ == "__main__":
    ##### DECLARE CONSTANTS FOR THE TEST CODE
    TEST_FILE_NAME = "your_file_name.pdf" #here would go the name of your pdf file
    TEST_OUTP_FOLDER = "your_output_folder"
    create_pdf(pdf_filename = TEST_FILE_NAME, outp_folder = TEST_OUTP_FOLDER)