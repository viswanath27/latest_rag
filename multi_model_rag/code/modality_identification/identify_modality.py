import fitz  # PyMuPDF
import pdfplumber
import os
import json
import base64

class tableData:
    def __init__(self, file_path):
        self.file_path = file_path

    def get_tables(self):
        # with pdfplumber.open(self.file_path) as pdf:
        #     tables = {page_num: page.extract_tables() for page_num, page in enumerate(pdf.pages, start=1) if page.extract_tables()}
        # return tables
        tables = {}
        count = 1
        with pdfplumber.open(self.file_path) as pdf:
            for page_num, page in enumerate(pdf.pages, start=1):
                page_data={}
                page_data["pg_num"] = page_num
                page_data["tables"] = page.extract_tables()
                tables[count] = page_data
                count += 1
        print(tables)
        return tables

    def extract_tables_to_json(self):
        tables = self.get_tables()
        tables_json = json.dumps(tables, indent=4)
        return tables_json
    
class imageData:
    def __init__(self, file_path):
        self.file_path = file_path  
    
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
                images.append((image_filename, image_bytes, page_num + 1))
        return images
    
    def process_img_data(self):
        # Extract images
        images_content = self.extract_images()
        print("\nExtracted Images:")

        # Initialize a dictionary to hold image data
        image_data = {"image_count": len(images_content)}

        # Use enumerate to loop through images_content with an index
        for count, (img_name, img_bytes, pg_num) in enumerate(images_content):
            img_base64 = base64.b64encode(img_bytes).decode('utf-8')
            img_node = {
                "img_name": img_name,
                "img_bytes": img_base64,
                "img_size": len(img_bytes),
                "page_num": pg_num
            }
            image_data[count] = img_node

            # Print summary of the image
            # print(f"Image {count}: {img_name}, Size: {img_node['img_size']} bytes, Page: {pg_num}")
        # print(image_data)
        # Convert the image_data dictionary to a JSON string
        image_data_json = json.dumps(image_data, indent=4)
        return image_data_json

class textData:
    def __init__(self, file_path):
        self.file_path = file_path 

    def extract_text(self):
        # Open the PDF file
        doc = fitz.open(self.file_path)
        text = ""
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            text += page.get_text()
        return text



    

# Path to the PDF file
pdf_path = "report.pdf"
data_process = textData(pdf_path)
# Extract text
# text_content = data_process.extract_text()
# print("Extracted Text:")
# print(text_content[:500])  # Print the first 500 characters of the text


# Extract tables
processed_table_data = tableData(pdf_path)
tables_content = processed_table_data.extract_tables_to_json()
print(tables_content)


# Extract Images
# processed_img_data = imageData(pdf_path)
# img_data = processed_img_data.process_img_data()

# Print the JSON string
# print(img_data)