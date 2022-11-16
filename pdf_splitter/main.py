from pathlib import Path
from pdf_splitter.split_pages import PageSplitter

# FOLLOWING PARAMETERS NEED TO BE CHANGED
# --------------------------------------
FOLDER_PATH = Path('.')
OUTPUT_FOLDER_PATH = Path('')
VOLUME_PATH_DIMENSION = Path('')
PAGE_NUMBER = 3
PRE_FIX = 'Single '
# --------------------------------------


if __name__ == '__main__':
    assert FOLDER_PATH != Path(''), "Need to set Path to the PDF Folder"
    assert OUTPUT_FOLDER_PATH != Path(''), "Need to set Path to the Output Folder"
    assert VOLUME_PATH_DIMENSION != Path(''), "Need to set Path to the Volume which determines the Dimensions"

    page_splitter = PageSplitter(FOLDER_PATH, OUTPUT_FOLDER_PATH, PRE_FIX)
    page_splitter.set_double_page_dimension_from_page(VOLUME_PATH_DIMENSION, PAGE_NUMBER)
    page_splitter.split_all_pdf_files_in_folder(left_page_first=True)

    exit()
