import os

from PyPDF2 import PdfFileWriter, PdfFileReader
from pathlib import Path

DOUBLE_PAGE_PIXELS = (1560, 1200)


class PageSplitter:
    """""
    Class to split the pdf pages which have the set dimensions.
    """

    def __init__(self, folder_name: Path, output_folder: Path, prefix: str):
        """
        :param folder_name: path to the folder where the pdfs are located.
        :param output_folder: path to the folder where the split pdfs will be saved.
        :param prefix: name prefix for the split pdfs.
        """
        self.double_page_pixels = DOUBLE_PAGE_PIXELS
        self.folder_name = folder_name
        self.output_folder = output_folder
        self.prefix = prefix

    def set_double_page_dimension_from_page(self, file: Path, page: int):
        """
        Sets the dimension for splitting the double pages for the every pdf in the folder.
        This is necessary, because typically there are some single pages and some double pages in a pdf.
        :param file: path to the file for which the page dimension will be used
        :param page: page number to be used as the dimensions
        """
        with open(file, 'rb') as f:
            pdf = PdfFileReader(f)
            example_page = pdf.getPage(page)
            self.double_page_pixels = example_page.trimbox.getUpperRight()

    def split_all_pdf_files_in_folder(self, left_page_first: bool):
        """
        Splits all pdf files in a folder
        :param left_page_first: Determines if the left half comes first or not.
        """
        for pdf_files in self.folder_name.glob('*.pdf'):
            self._split_pages(pdf_files, left_page_first)

    def _split_pages(self, file, left_page_first: bool):
        temporary_file = Path('tmp.pdf')
        self._sort_out_double_pages(file, temporary_file)

        with open(temporary_file, "rb") as f:
            pdf = PdfFileReader(f)
            output = PdfFileWriter()
            left_page = left_page_first
            for i in range(pdf.getNumPages()):
                page = pdf.getPage(i)
                if page.trimbox.getUpperRight() == self.double_page_pixels:
                    if left_page:
                        page.cropBox.lowerLeft = (0, 0)
                        page.cropBox.upperRight = ((self.double_page_pixels[0] / 2), self.double_page_pixels[1])
                        output.addPage(page)
                        left_page = False
                    else:
                        page.cropBox.lowerLeft = (self.double_page_pixels[0] / 2, 0)
                        page.cropBox.upperRight = self.double_page_pixels
                        output.addPage(page)
                        left_page = True
                else:
                    output.addPage(page)
            output_folder = self.output_folder.joinpath(file.parent.name)
            Path.mkdir(output_folder, exist_ok=True)
            output_name = output_folder.joinpath(f'{self.prefix} {file.name}')
            output.write(output_name)

        os.remove(temporary_file)

    def _sort_out_double_pages(self, file: Path, temporary_file: Path):
        with open(file, "rb") as f:
            pdf = PdfFileReader(f)
            double_output = PdfFileWriter()

            for i in range(pdf.getNumPages()):
                page = pdf.getPage(i)
                if page.trimbox.getUpperRight() == self.double_page_pixels:
                    double_output.addPage(page)
                    double_output.addPage(page)
                else:
                    double_output.addPage(page)

            double_output.write(temporary_file)
