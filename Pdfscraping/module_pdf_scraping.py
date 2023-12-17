
#?=========================================================================================================================
#?                  Description: This module contains the code for the PDF scraping module of the GUI.
#?              This module is a placeholder, and you should replace it with your actual PDF scraping module.
#?=========================================================================================================================

#?=========================================================================================================================
#?                      Import the pdf_scraping module (replace with your actual PDF scraping module)
#?=========================================================================================================================

from Pdfscraping.pdf_scraping_module import pdf_scrape
import tkinter as tk
from tkinter import filedialog
import uuid
# from interface_main import main_window




#?=========================================================================================================================
#?                                       Function to start PDF scraping
#?=========================================================================================================================
# Create a function to perform PDF scraping when a button is clicked
def start_pdf_scraping(pdf_entry , root ,open_scraper):

    # Remove previous content in the PDF scraping window
    for widget in root.winfo_children():
        widget.destroy()
    # Get the PDF file path from the entry widget
    pdf_path = pdf_entry

    # Call the pdf_scrape function from pdf_scraping_module.py
    scraped_text = pdf_scrape(pdf_path)

    # pdf_scraping_window = tk.Toplevel()
    # Create a label to display the scraped PDF text
    pdf_scraping_result_window = tk.Frame(root, bg="lightblue")
    pdf_scraping_result_window.pack(fill=tk.BOTH, expand=True)
    # pdf_scraping_result_window.title("Open Scraper")
    # pdf_scraping_result_window.configure(bg="lightblue")
    # Create a Text widget to display the scraped PDF text with a scrollbar
    pdf_text = tk.Text(pdf_scraping_result_window, wrap=tk.WORD, width=80, height=20)
    pdf_text.insert(tk.END, scraped_text)
    pdf_text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    # Create a label to display the file location
    file_location_label = tk.Label(pdf_scraping_result_window, text="", font=("Helvetica", 14) , bg="lightblue")
    file_location_label.pack(side="bottom", padx=10, pady=20)

    # Create a button to save the PDF text to a file
    save_button = tk.Button(pdf_scraping_result_window, text="Save Text to File", command=lambda: save_pdf_text_to_file(scraped_text , file_location_label), font=("Helvetica", 14), bg="blue", fg="white")
    save_button.pack(side="bottom", padx=10, pady=20)
    

    # Create a button to go back to the previous menu
    back_button = tk.Button(pdf_scraping_result_window, text="Back to Previous Menu", command=open_scraper, font=("Helvetica", 14), bg="red", fg="white")
    back_button.pack(side="bottom", padx=10, pady=20)

#?=========================================================================================================================
#?                                       Function to open the PDF scraping module
#?=========================================================================================================================
def browse_pdf_file(pdf_entry):
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    pdf_entry.delete(0, tk.END)  # Clear the current entry text
    pdf_entry.insert(0, file_path)  # Insert the selected file path into the entry



def open_pdf_scraping_module(root , main_window , open_scraper):
    # Create a new window for PDF scraping


    # Function to open a file dialog and select a PDF file


    # Remove previous content in the root window
    for widget in root.winfo_children():
        widget.destroy()

    # Create a frame to contain the PDF scraping module content
    root.title("Pdf Scraping")
    pdf_scraping_window = tk.Frame(root)
    pdf_scraping_window.configure(bg="lightblue")
    pdf_scraping_window.pack(fill=tk.BOTH, expand=True)
    

    # # Create a frame to contain the content
    # content_frame = tk.Frame(pdf_scraping_window, padx=20, pady=20)
    # content_frame.pack(expand=True, fill="both")

    info_text = (
    "Our PDF scraping tool extracts text and tables from PDFs efficiently:\n\n"
    "• Extracts structured text content from PDFs, including paragraphs and headings.\n"
    "• Detects and extracts tabular data from PDFs, providing structured table data.\n"
    "• Utilizes OCR for images within PDFs, converting images to text for scanned documents.\n"
    "• Returns content in a versatile format suitable for various data processing needs.\n"
    "• Easy to use – just provide the PDF file you want to scrape.\n\n"
    "We are continuously working to enhance and improve our tool to provide you with even better results.\n\n"
    "Whether your PDFs contain text, tables, images, or a combination, our tool handles it all."
)


    content_frame = tk.Frame(pdf_scraping_window, padx=30, pady=30)
    content_frame.pack(expand=True, fill="both")

    # info_label = tk.Label(content_frame, text=info_text, font=("Helvetica", 14), justify="left", wraplength=600, fg="blue")
    # info_label.pack(pady=10)    
    # Create a text widget with formatted text and colored lines
    text_widget = tk.Text(content_frame, wrap="word", font=("Helvetica", 12), height=15, width=80,)
    text_widget.pack(pady=10)

    # Apply different colors to specific lines
    text_widget.tag_configure("blue", foreground="blue")
    text_widget.insert("1.0", info_text)
    text_widget.tag_add("blue", "1.0", "1.33")  # Apply blue color to the first line
    text_widget.tag_add("blue", "3.0", "3.29")  # Apply blue color to the third line
    text_widget.tag_add("blue", "5.0", "5.37")  # Apply blue color to the fifth line
    text_widget.tag_add("blue", "7.0", "7.36")  # Apply blue color to the seventh line
    text_widget.tag_add("blue", "9.0", "9.39")  # Apply blue color to the ninth line
    text_widget.tag_add("blue", "11.0", "11.46")  # Apply blue color to the eleventh line
    text_widget.configure(state="disabled")  # Make the text widget read-only
    # Create an entry widget for entering the PDF file path
    pdf_entry = tk.Entry(content_frame, width=50, font=("Helvetica", 14))
    pdf_entry.pack(pady=10)

        # Create a "Browse" button to select a PDF file
    browse_button = tk.Button(content_frame, text="Browse", command=lambda :browse_pdf_file(pdf_entry), font=("Helvetica", 14), bg="cyan", fg="white")
    browse_button.pack(pady=10)




    # Create a frame to contain the buttons in one row
    button_frame = tk.Frame(content_frame)
    button_frame.pack(side="bottom")

    # Create a button to start PDF scraping with a green background and white text
    start_button = tk.Button(button_frame, text="Start PDF Scraping", command=lambda: start_pdf_scraping(pdf_entry.get(), root, open_scraper), font=("Helvetica", 16), bg="green", fg="white")
    start_button.pack(side="left", padx=10, pady=20)

    # Create a button to go back to the previous menu
    back_button1 = tk.Button(button_frame, text="Back to Previous Menu", command=open_scraper, font=("Helvetica", 14), bg="red", fg="white")
    back_button1.pack(side="left", padx=10, pady=20)

    # Create a button to go back to the main menu with a red background and white text
    back_button2 = tk.Button(button_frame, text="Back to Main Menu", command=main_window, font=("Helvetica", 16), bg="red", fg="white")
    back_button2.pack(side="left", padx=10, pady=20)


#?=========================================================================================================================
#?                                       Function to save PDF text to a file
#?=========================================================================================================================
# Function to save PDF text to a file (implement as needed)
def save_pdf_text_to_file(text_list , file_location_label):
    # Implement the code to save the PDF text to a file here
    # This function is a placeholder, and you should add the actual code to save the text to a file.
    text = '\n'.join(text_list)
    filename = f"{uuid.uuid4()}.txt"

    with open(filename, 'w') as f:
        f.write(text)


    file_location_label.config(text=f"Saved File Name: {filename}")

#?=========================================================================================================================
#?                                   End of PDF scraping module
#?=========================================================================================================================