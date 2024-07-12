import fitz  # PyMuPDF
import pdfplumber
import os

class modalityData:
    def __init__(self, file_path):
        self.file_path = file_path 
        pass

    def extract_text(self):
        # Open the PDF file
        doc = fitz.open(self.file_path)
        text = ""
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            text += page.get_text()
        return text

    def extract_tables(self):
        tables = []
        with pdfplumber.open(self.file_path) as pdf:
            for page in pdf.pages:
                tables.extend(page.extract_tables())
        return tables

    def extract_images(self):
        doc = fitz.open(self.file_path)
        images = []
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            for img_index, img in enumerate(page.get_images(full=True)):
                xref = img[0]
                base_image = doc.extract_image(xref)
                image_bytes = base_image["image"]
                image_ext = base_image["ext"]
                image_filename = f"page{page_num + 1}_img{img_index + 1}.{image_ext}"
                images.append((image_filename, image_bytes))
        return images

# Path to the PDF file
pdf_path = "report.pdf"

data_process = modalityData(pdf_path)
# Extract text
text_content = data_process.extract_text()
print("Extracted Text:")
print(text_content[:500])  # Print the first 500 characters of the text

# Extract tables
tables_content = data_process.extract_tables()
print("\nExtracted Tables:")
for table in tables_content:
    for row in table:
        print(row)
    print("\n")

# Extract images
images_content = data_process.extract_images()
print("\nExtracted Images:")
for img_name, img_bytes in images_content:
    print(f"Image: {img_name}, Size: {len(img_bytes)} bytes")
