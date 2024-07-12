"""
This code sample shows Prebuilt Layout operations with the Azure Form Recognizer client library. 
The async versions of the samples require Python 3.6 or later.

To learn more, please visit the documentation - Quickstart: Document Intelligence (formerly Form Recognizer) SDKs
https://learn.microsoft.com/azure/ai-services/document-intelligence/quickstarts/get-started-sdks-rest-api?pivots=programming-language-python
"""
import json
from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import DocumentAnalysisClient

"""
Remember to remove the key from your code when you're done, and never post it publicly. For production, use
secure methods to store and access your credentials. For more information, see 
https://docs.microsoft.com/en-us/azure/cognitive-services/cognitive-services-security?tabs=command-line%2Ccsharp#environment-variables-and-application-configuration
"""
endpoint = "https://advait-afr.cognitiveservices.azure.com/"
key = "ee45e6f87b8a4657a4e453766ba7e6b3"

# sample document
# formUrl = "https://raw.githubusercontent.com/Azure-Samples/cognitive-services-REST-api-samples/master/curl/form-recognizer/sample-layout.pdf"
formUrl = "blk_rock.pdf"
document_analysis_client = DocumentAnalysisClient(
    endpoint=endpoint, credential=AzureKeyCredential(key)
)
    
# poller = document_analysis_client.begin_analyze_document_from_url("prebuilt-layout", formUrl)

with open("blk_rock.pdf", "rb") as f:
    poller = document_analysis_client.begin_analyze_document(
        "prebuilt-layout", document=f, locale="en-US"
    )
receipts = poller.result()
result = poller.result()
# Convert result to a dictionary
result_dict = result.to_dict()

# # Convert the dictionary to JSON
# result_json = json.dumps(result_dict, indent=2)

# # Print or save the JSON
# print(result_json)
# Save the dictionary to a JSON file
with open('result.json', 'w') as f:
    json.dump(result_dict, f, indent=2)

print("Result has been saved to result.json")
# for idx, style in enumerate(result.styles):
#     print(
#         "Document contains {} content".format(
#          "handwritten" if style.is_handwritten else "no handwritten"
#         )
#     )

# for page in result.pages:
#     for line_idx, line in enumerate(page.lines):
#         print(
#          "...Line # {} has text content '{}'".format(
#         line_idx,
#         line.content.encode("utf-8")
#         )
#     )

#     for selection_mark in page.selection_marks:
#         print(
#          "...Selection mark is '{}' and has a confidence of {}".format(
#          selection_mark.state,
#          selection_mark.confidence
#          )
#     )

# for table_idx, table in enumerate(result.tables):
#     print(
#         "Table # {} has {} rows and {} columns".format(
#         table_idx, table.row_count, table.column_count
#         )
#     )
        
#     for cell in table.cells:
#         print(
#             "...Cell[{}][{}] has content '{}'".format(
#             cell.row_index,
#             cell.column_index,
#             cell.content.encode("utf-8"),
#             )
#         )

print("----------------------------------------")

