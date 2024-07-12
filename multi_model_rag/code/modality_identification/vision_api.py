# import os
# from google.cloud import vision
# from google.cloud import documentai_v1 as documentai

# def process_pdf(project_id, location, processor_id, file_path, mime_type):

#     # Instantiate clients
#     opts = {"api_endpoint": f"{location}-documentai.googleapis.com"}
#     documentai_client = documentai.DocumentProcessorServiceClient(client_options=opts)
#     vision_client = vision.ImageAnnotatorClient()

#     # Create processor name
#     name = f"projects/{project_id}/locations/{location}/processors/{processor_id}"

#     # Read the file into memory
#     with open(file_path, "rb") as image:
#         image_content = image.read()

#     # Create raw document for processing
#     raw_document = documentai.types.RawDocument(content=image_content, mime_type=mime_type)

#     # Process the document
#     request = documentai.types.ProcessRequest(name=name, raw_document=raw_document)
#     result = documentai_client.process_document(request=request)

#     document = result.document

#     # Extract information
#     for page in document.pages:
#         for block in page.blocks:
#             block_text = ""
#             for paragraph in block.paragraphs:
#                 for word in paragraph.words:
#                     for symbol in word.symbols:
#                         block_text += symbol.text

#             # Extract block type and bounding box
#             block_type = block.layout.block_type
#             bounding_box = block.layout.bounding_poly

#             # Process information (example: print to console)
#             print(f"Block Type: {block_type}")
#             print(f"Bounding Box: {bounding_box}")
#             print(f"Text: {block_text}")

#         for image in page.images:
#             image_request = vision.AnnotateImageRequest(
#                 image=vision.Image(content=image.content),
#                 features=[vision.Feature(type_=vision.Feature.Type.TEXT_DETECTION)],
#             )
#             response = vision_client.annotate_image(request=image_request)
#             text = response.text_annotations[0].description

#             # Extract image bounding box
#             bounding_box = image.layout.bounding_poly

#             # Process information (example: print to console)
#             print(f"Image Bounding Box: {bounding_box}")
#             print(f"Text: {text}")
        
#         # Extract table information
#         for table in page.tables:
#             num_rows = len(table.header_rows) + len(table.body_rows)
#             num_columns = len(table.columns)
#             table_data = []

#             # Process header rows
#             for header_row in table.header_rows:
#                 row_data = []
#                 for cell in header_row.cells:
#                     row_data.append(cell.layout.text)
#                 table_data.append(row_data)

#             # Process body rows
#             for body_row in table.body_rows:
#                 row_data = []
#                 for cell in body_row.cells:
#                     row_data.append(cell.layout.text)
#                 table_data.append(row_data)

#             # Extract table bounding box
#             bounding_box = table.layout.bounding_poly

#             # Process information (example: print to console)
#             print(f"Table Bounding Box: {bounding_box}")
#             print(f"Table Data: {table_data}")

# # Set up your Google Cloud credentials and project information
# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "your_credentials_file.json"
# project_id = "custom-point-408112"
# location = "in"  # e.g., 'us' or 'eu'
# processor_id = "your_processor_id"
# file_path = "report.pdf"
# mime_type = "application/pdf"

# process_pdf(project_id, location, processor_id, file_path, mime_type)
