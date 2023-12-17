
# #?=====================================================================================================================================
# #?          This module is used to extract text from PDF files. It uses the pdfplumber library to extract text from PDF files.
# #?=====================================================================================================================================

import pdfplumber
import pytesseract
from PIL import Image
from io import BytesIO

# #?=====================================================================================================================================
# #?          This function is used to extract text from PDF files. It uses the pdfplumber library to extract text from PDF files.
# #?=====================================================================================================================================

def pdf_scrape(pdf_path):
    try:
        # Initialize a variable to store the extracted content
        extracted_content = []

        # Open the PDF file
        with pdfplumber.open(pdf_path) as pdf:
            # Iterate through each page of the PDF
            for page in pdf.pages:
                # Extract text from the current page
                page_text = page.extract_text()

                # Extract tables from the page
                tables = page.extract_tables()

                # Check if there is any structured text content on the page
                if page_text.strip():
                    # Append the text to the extracted content
                    extracted_content.append(page_text)
                else:
                    # If no structured text content, check for tables
                    if tables:
                        # Append the table data to the extracted content
                        extracted_content.extend(tables)
                    else:
                        # If neither text nor tables are found, perform OCR
                        # Convert the PDF page to an image
                        page_image = page.to_image()

                        # Use pytesseract to perform OCR on the image
                        ocr_text = pytesseract.image_to_string(page_image)

                        # Append the OCR text to the extracted content
                        extracted_content.append(ocr_text)

        # Return the extracted content
        return extracted_content
    except Exception as e:
        # Handle any exceptions that may occur during PDF parsing
        return str(e)
# #?=====================================================================================================================================
# #?                                                        End of module
# #?=====================================================================================================================================



