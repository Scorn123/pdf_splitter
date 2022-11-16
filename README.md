# PDF Splitter
This Python Module allows you to split folder of PDFs, where there are double and single pages.
It splits up the double pages to single pages and lets the single pages as they are.

## Usage
Primary usage is for a book pdf with some double pages, which might be hard to read on an e-reader.

## Deployment and Configuration

### Set Up Python Venv
```sh
python3.10 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Configurations
In the main.py file set the following macros to your file structure.
- FOLDER_PATH: Path to the folder where the pdfs are.
- OUTPUT_FOLDER_PATH: Path where you want the edited pdfs to be saved
- VOLUME_PATH_DIMENSION: A single pdf which has a double page you want to have split.
- PAGE_NUMBER: The Page within the Volume Path of the double page.
- PRE_FIX: Naming Prefix for the edited pdfs.

