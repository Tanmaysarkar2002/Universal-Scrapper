
#?======================================================================================================================================
#?                          1. Import the web_scrape function from the webscraping_module.py file
#?======================================================================================================================================
# Import the webscraping module
from webscrapers.scraper_main import unscrapper

import re
import tkinter as tk
from tkinter import ttk , Frame , Text  , Entry , Label




class CustomButton(tk.Button):
    def __init__(self, master, text, command=None, font=None, bg=None, fg=None, hover_bg=None, hover_fg=None, **kwargs):
        super().__init__(master, text=text, command=command, font=font, bg=bg, fg=fg, **kwargs)
        self.default_bg = bg
        self.default_fg = fg
        self.hover_bg = hover_bg
        self.hover_fg = hover_fg
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, event):
        self.configure(bg=self.hover_bg, fg=self.hover_fg)

    def on_leave(self, event):
        self.configure(bg=self.default_bg, fg=self.default_fg)



def news_scrapper_window(root , open_scraper ):
        # Create a new window for web scraping

    new_sc = unscrapper()


    for widget in root.winfo_children():
        widget.destroy()

    # Create a frame to contain the PDF scraping module content

    root.title("Web Scraping")
    webscraping_window = tk.Frame(root)
    # webscraping_window.state('zoomed')  # Maximize the window
    webscraping_window.configure(bg="lightblue")
    webscraping_window.pack(fill=tk.BOTH, expand=True)

        # Create a frame to contain the content with a background color
    content_frame = tk.Frame(webscraping_window, padx=20, pady=20, bg="lightblue")
    content_frame.pack(expand=True, fill="both")





    # Create a label with styled text (bold and colored)
    info_text = (
        "Web scraping on our platform is currently undergoing optimization to enhance its functionality.\n\n"
        "Key Points:\n"
        # "• Users can currently scrape paragraph text and table data.\n"
        "• Our team is actively working to expand scraping capabilities.\n"
        "• Thank you for your patience and support as we improve your experience."
    )

    # Apply different colors to specific lines
    text_widget = tk.Text(content_frame, wrap="word", font=("Helvetica", 16), height=10, width=50, bg="lightblue")
    text_widget.pack(pady=10)

    # Apply different colors to specific lines
    text_widget.tag_configure("blue", foreground="blue")
    text_widget.insert("1.0", info_text)
    text_widget.tag_add("blue", "4.0", "4.22")  # Apply blue color to the "Key Points" line
    text_widget.tag_add("blue", "6.0", "6.49")  # Apply blue color to the first bullet point
    text_widget.tag_add("blue", "7.0", "7.52")  # Apply blue color to the second bullet point
    text_widget.tag_add("blue", "8.0", "8.46")  # Apply blue color to the third bullet point
    text_widget.configure(state="disabled")

    # Create a Scrollbar widget
    scrollbar = tk.Scrollbar(content_frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    url_frame = tk.Frame(content_frame, bg="lightblue")
    url_frame.pack(pady=10)

    # Create a label and entry for the URL input
    url_label = tk.Label(url_frame, text="Kind Of News:", font=("Helvetica", 16), bg="lightblue")
    url_label.pack(side="left")
    url_entry = tk.Entry(url_frame, font=("Helvetica", 16), width=50)
    url_entry.pack(side="left")

    data_text = tk.Text(content_frame, wrap="word", font=("Arial", 20), height=10, width=85, bg="lightblue" ,fg="black", padx=10, pady=10, bd=2, relief="groove")
    
    data_text.pack(padx=0, pady=0)
    # Configure the Scrollbar to scroll the Text widget
    scrollbar.config(command=data_text.yview)

    button_frame = tk.Frame(content_frame, bg="lightblue")
    button_frame.pack()

    start_button = CustomButton(
        button_frame,
        text="Start Scraping",
        command=lambda: (
        data_text.delete('1.0', tk.END),
        data_text.insert(tk.END, '\n'.join(f'• {item}' for item in new_sc.news_scrapper(url_entry.get())))
        ),
        font=("Helvetica", 16),
        bg="green",
        fg="white",
        hover_bg="darkgreen",  # Change background color on hover
        hover_fg="white",      # Change text color on hover
    )

    back_button = CustomButton(
        button_frame,
        text="Previous Menu",
        command=lambda: open_webscraping_module(root , open_scraper),
        font=("Helvetica", 16),
        bg="red",
        fg="white",
        hover_bg="darkred",    # Change background color on hover
        hover_fg="white",      # Change text color on hover
    )
    button_frame.pack(side="top", pady=20)
    start_button.pack(side="left", padx=10)
    back_button.pack(side="left", padx=10)

def scrape_related_word(root, open_scraper):

    new_sc = unscrapper()

    for widget in root.winfo_children():
        widget.destroy()

    # Create a frame to contain the PDF scraping module content

    root.title("Web Scraping")
    webscraping_window = tk.Frame(root)
    # webscraping_window.state('zoomed')  # Maximize the window
    webscraping_window.configure(bg="lightblue")
    webscraping_window.pack(fill=tk.BOTH, expand=True)

        # Create a frame to contain the content with a background color
    content_frame = tk.Frame(webscraping_window, padx=20, pady=20, bg="lightblue")
    content_frame.pack(expand=True, fill="both")

    info_text = (
        "Web scraping on our platform is currently undergoing optimization to enhance its functionality.\n\n"
        "Key Points:\n"
        # "• Users can currently scrape paragraph text and table data.\n"
        "• Our team is actively working to expand scraping capabilities.\n"
        "• Thank you for your patience and support as we improve your experience."
    )

    # Apply different colors to specific lines
    text_widget = tk.Text(content_frame, wrap="word", font=("Helvetica", 16), height=10, width=50, bg="lightblue")
    text_widget.pack(pady=10)

    # Apply different colors to specific lines
    text_widget.tag_configure("blue", foreground="blue")
    text_widget.insert("1.0", info_text)
    text_widget.tag_add("blue", "4.0", "4.22")  # Apply blue color to the "Key Points" line
    text_widget.tag_add("blue", "6.0", "6.49")  # Apply blue color to the first bullet point
    text_widget.tag_add("blue", "7.0", "7.52")  # Apply blue color to the second bullet point
    text_widget.tag_add("blue", "8.0", "8.46")  # Apply blue color to the third bullet point
    text_widget.configure(state="disabled")

    # Create a frame for the URL input
    url_frame = tk.Frame(content_frame, bg="lightblue")
    url_frame.pack(pady=10)

    # Create a label and entry for the URL input
    url_label = tk.Label(url_frame, text="URL:", font=("Helvetica", 16), bg="lightblue")
    url_label.pack(side="left")
    url_entry = tk.Entry(url_frame, font=("Helvetica", 16), width=50)
    url_entry.pack(side="left")

    # Create a frame for the wanted list input
    wanted_list_frame = tk.Frame(content_frame, bg="lightblue")
    wanted_list_frame.pack(pady=10)

    # Create a label and entry for the wanted list input
    wanted_list_label = tk.Label(wanted_list_frame, text="Wanted List:", font=("Helvetica", 16), bg="lightblue")
    wanted_list_label.pack(side="left")
    wanted_list_entry = tk.Entry(wanted_list_frame, font=("Helvetica", 16), width=50)
    wanted_list_entry.pack(side="left")

    # Create a Text widget for the result
    result_text = tk.Text(content_frame, wrap="word", font=("Helvetica", 20), height=10, width=85, bg="lightblue", fg="black")
    result_text.pack(padx=0, pady=0)

    button_frame = tk.Frame(content_frame, bg="lightblue")
    button_frame.pack()
    

    start_button = CustomButton(
        button_frame,
        text="Select Scraping",
        command=lambda: result_text.insert(tk.END, '\n'.join(new_sc.scrape_list(url_entry.get(), wanted_list_entry.get()))),
        font=("Helvetica", 16),
        bg="green",
        fg="white",
        hover_bg="darkgreen",  # Change background color on hover
        hover_fg="white",      # Change text color on hover
    )

    back_button = CustomButton(
        button_frame,
        text="Previous Menu",
        command=lambda: open_webscraping_module(root , open_scraper),
        font=("Helvetica", 16),
        bg="red",
        fg="white",
        hover_bg="darkred",    # Change background color on hover
        hover_fg="white",      # Change text color on hover
    )
    button_frame.pack(side="top", pady=20)
    start_button.pack(side="left", padx=10)
    back_button.pack(side="left", padx=10)

def open_google_search(root , open_scraper):
    new_sc = unscrapper()

    for widget in root.winfo_children():
        widget.destroy()

    # Create a frame to contain the PDF scraping module content

    root.title("Web Scraping")
    webscraping_window = tk.Frame(root)
    # webscraping_window.state('zoomed')  # Maximize the window
    webscraping_window.configure(bg="lightblue")
    webscraping_window.pack(fill=tk.BOTH, expand=True)

        # Create a frame to contain the content with a background color
    content_frame = tk.Frame(webscraping_window, padx=20, pady=20, bg="lightblue")
    content_frame.pack(expand=True, fill="both")

    # Create a Scrollbar widget
    scrollbar = tk.Scrollbar(content_frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    url_frame = tk.Frame(content_frame, bg="lightblue")
    url_frame.pack(pady=10)

    # Create a label and entry for the URL input
    url_label = tk.Label(url_frame, text="Enter The Query String::", font=("Helvetica", 16), bg="lightblue")
    url_label.pack(side="left")
    url_entry = tk.Entry(url_frame, font=("Helvetica", 16), width=50)
    url_entry.pack(side="left")

    data_text = tk.Text(content_frame, wrap="word", font=("Arial", 20), height=20, width=85, bg="lightblue" ,fg="black", padx=10, pady=10, bd=2, relief="groove")
    
    data_text.pack(padx=0, pady=0)
    # Configure the Scrollbar to scroll the Text widget
    scrollbar.config(command=data_text.yview)

    button_frame = tk.Frame(content_frame, bg="lightblue")
    button_frame.pack()

    start_button = CustomButton(
        button_frame,
        text="Start Scraping",
        command=lambda: (
        data_text.delete('1.0', tk.END),
        data_text.insert(tk.END, '\n'.join(f'• {item}' for item in new_sc.scrape_page(url_entry.get()))),
        data_text.configure(state="disabled")
        ),
        font=("Helvetica", 16),
        bg="green",
        fg="white",
        hover_bg="darkgreen",  # Change background color on hover
        hover_fg="white",      # Change text color on hover
    )

    back_button = CustomButton(
        button_frame,
        text="Previous Menu",
        command=lambda: google_search(root , open_scraper),
        font=("Helvetica", 16),
        bg="red",
        fg="white",
        hover_bg="darkred",    # Change background color on hover
        hover_fg="white",      # Change text color on hover
    )
    button_frame.pack(side="top", pady=20)
    start_button.pack(side="left", padx=10)
    back_button.pack(side="left", padx=10)

#Url search
def open_url_search(root , open_scraper):
    new_sc = unscrapper()

    for widget in root.winfo_children():
        widget.destroy()

    # Create a frame to contain the PDF scraping module content

    root.title("Web Scraping")
    webscraping_window = tk.Frame(root)
    # webscraping_window.state('zoomed')  # Maximize the window
    webscraping_window.configure(bg="lightblue")
    webscraping_window.pack(fill=tk.BOTH, expand=True)

        # Create a frame to contain the content with a background color
    content_frame = tk.Frame(webscraping_window, padx=20, pady=20, bg="lightblue")
    content_frame.pack(expand=True, fill="both")

    # Create a Scrollbar widget
    scrollbar = tk.Scrollbar(content_frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    url_frame = tk.Frame(content_frame, bg="lightblue")
    url_frame.pack(pady=10)

    # Create a label and entry for the URL input
    url_label = tk.Label(url_frame, text="Enter The Query KeyWord:", font=("Helvetica", 16), bg="lightblue")
    url_label.pack(side="left")
    url_entry = tk.Entry(url_frame, font=("Helvetica", 16), width=50)
    url_entry.pack(side="left")

    data_text = tk.Text(content_frame, wrap="word", font=("Arial", 20), height=20, width=85, bg="lightblue" ,fg="black", padx=10, pady=10, bd=2, relief="groove")
    
    data_text.pack(padx=0, pady=0)
    # Configure the Scrollbar to scroll the Text widget
    scrollbar.config(command=data_text.yview)

    button_frame = tk.Frame(content_frame, bg="lightblue")
    button_frame.pack()

    start_button = CustomButton(
        button_frame,
        text="Start Scraping",
        command=lambda: (
        data_text.delete('1.0', tk.END),
        data_text.insert(tk.END, '\n'.join(f'• {item}' for item in new_sc.scrape_url(url_entry.get()))),
        data_text.configure(state="disabled")
        ),
        font=("Helvetica", 16),
        bg="green",
        fg="white",
        hover_bg="darkgreen",  # Change background color on hover
        hover_fg="white",      # Change text color on hover
    )

    back_button = CustomButton(
        button_frame,
        text="Previous Menu",
        command=lambda: google_search(root , open_scraper),
        font=("Helvetica", 16),
        bg="red",
        fg="white",
        hover_bg="darkred",    # Change background color on hover
        hover_fg="white",      # Change text color on hover
    )
    button_frame.pack(side="top", pady=20)
    start_button.pack(side="left", padx=10)
    back_button.pack(side="left", padx=10)


def google_search(root , open_scraper ):


    for widget in root.winfo_children():
        widget.destroy()

    # Create a frame to contain the PDF scraping module content

    root.title("Web Scraping")
    webscraping_window = tk.Frame(root)
    # webscraping_window.state('zoomed')  # Maximize the window
    webscraping_window.configure(bg="lightblue")
    webscraping_window.pack(fill=tk.BOTH, expand=True)

        # Create a frame to contain the content with a background color
    content_frame = tk.Frame(webscraping_window, padx=20, pady=20, bg="lightblue")
    content_frame.pack(expand=True, fill="both")

    info_text = (
    "Web scraping on our platform is currently undergoing optimization to enhance its functionality.\n\n"
    "Key Points:\n"
    "• In Google Search, users can currently perform two primary actions:\n"
    "    1. Search for a keyword and retrieve the URL of the corresponding website.\n"
    "        • This feature aids users in quickly obtaining the web address associated with their search query.\n"
    "    2. Search for a keyword and obtain accurate results related to that keyword from a web page.\n"
    "        • Users can extract precise information directly from web pages, improving search efficiency.\n"
    "• Our roadmap includes the addition of more advanced features.\n"
    "    • Forthcoming features may include location-based searches, allowing users to tailor results based on geography.\n"
    "    • Additional enhancements are in the pipeline, promising an even more comprehensive user experience.\n"
    "• The development team is actively working to expand the platform's scraping capabilities.\n"
    "    • Ongoing efforts involve optimizing performance, ensuring reliability, and addressing user feedback.\n"
    "• Your patience and support are greatly appreciated as we strive to enhance your user experience.\n"
    "    • We understand the importance of a seamless user experience and are dedicated to continuous improvement.\n"
    "• Stay tuned for further updates and improvements!\n"
    "    • We are committed to delivering a robust and user-friendly web scraping experience, with regular updates to meet evolving user needs."
    )

    # Apply different colors to specific lines
    text_widget = tk.Text(content_frame, wrap="word", font=("Helvetica", 16), height=25, width=80, bg="lightblue")
    text_widget.pack(pady=20)

    # Apply different colors to specific lines
    pattern = pattern = r"•\s*\w+\s+\w+"

    # Find all matches of the pattern in the text
    matches = re.finditer(pattern, info_text)

    # Apply different colors to the bullet points
    text_widget.tag_configure("blue", foreground="blue")
    text_widget.insert("1.0", info_text)

    for match in matches:
        start, end = match.span()
        end = start + len(match.group().split(" ", 2)[0]) + len(match.group().split(" ", 2)[1]) + 1
        start_index = f"{start // 80 + 1}.{start % 80}"
        end_index = f"{end // 80 + 1}.{end % 80}"
        text_widget.tag_add("blue", start_index, end_index)

    text_widget.configure(state="disabled")


    button_frame = tk.Frame(content_frame, bg="lightblue")
    button_frame.pack()
    

    start_button = CustomButton(
        button_frame,
        text="Get Set Of urls on Based On search",
        command=lambda: open_url_search(root , open_scraper),
        font=("Helvetica", 16),
        bg="green",
        fg="white",
        hover_bg="darkgreen",  # Change background color on hover
        hover_fg="white",      # Change text color on hover
    )

    start1_button = CustomButton(
        button_frame,
        text="Get Related urls And Sepcific Data",
        command=lambda: open_google_search(root , open_scraper),
        font=("Helvetica", 16),
        bg="green",
        fg="white",
        hover_bg="darkgreen",  # Change background color on hover
        hover_fg="white",      # Change text color on hover
    )

    back_button = CustomButton(
        button_frame,
        text="Previous Menu",
        command=lambda: open_webscraping_module(root , open_scraper),
        font=("Helvetica", 16),
        bg="red",
        fg="white",
        hover_bg="darkred",    # Change background color on hover
        hover_fg="white",      # Change text color on hover
    )
    button_frame.pack(side="top", pady=30)
    start_button.pack(side="left", padx=20)
    start1_button.pack(side="left", padx=20)
    back_button.pack(side="left", padx=20)


def oops_still_not_available(root):


    root.title("Web Scraping")
    webscraping_window = tk.Frame(root)
    # webscraping_window.state('zoomed')  # Maximize the window
    webscraping_window.configure(bg="lightblue")
    webscraping_window.pack(fill=tk.BOTH, expand=True)

        # Create a frame to contain the content with a background color
    content_frame = tk.Frame(webscraping_window, padx=20, pady=20, bg="lightblue")
    content_frame.pack(expand=True, fill="both")

    # Create a label with the message
    message_label = tk.Label(content_frame, text="Oops, not found. Working on it...", font=("Arial", 20) , bg="lightblue")
    message_label.pack(padx=20, pady=20)


    content_frame.after(2000, content_frame.destroy)  # Destroy the frame after 5 seconds
    
#?======================================================================================================================================
#?                                       Function to start web scraping
#?======================================================================================================================================
def start_web_scraping(url_entry , root , open_scraper):
    # Get the URL and data type from the entry widgets and radio buttons
    
    if url_entry == "scrape_news":
        news_scrapper_window(root , open_scraper)
    elif url_entry == "scrape_keyword":
        scrape_related_word(root, open_scraper)
    elif url_entry == "search_google":
        google_search(root , open_scraper)
    elif url_entry == "scrape_url":
        oops_still_not_available(root)
    elif url_entry == "scrape_images":
        oops_still_not_available(root)
    elif url_entry == "scrape_jobs":
        oops_still_not_available(root)
    
#?======================================================================================================================================
#?                                       Function to open the web scraping module
#?======================================================================================================================================

def open_webscraping_module(root , open_scraper):
    
    # Create a new window for web scraping

    for widget in root.winfo_children():
        widget.destroy()

    # Create a frame to contain the PDF scraping module content

    root.title("Web Scraping")
    webscraping_window = tk.Frame(root)
    # webscraping_window.state('zoomed')  # Maximize the window
    webscraping_window.configure(bg="lightblue")
    webscraping_window.pack(fill=tk.BOTH, expand=True)

     # Create a frame to contain the content with a background color
    content_frame = tk.Frame(webscraping_window, padx=20, pady=20, bg="lightblue")
    content_frame.pack(expand=True, fill="both")

    # Create a label with styled text (bold and colored)
    info_text = (
        "Web scraping on our platform is currently undergoing optimization to enhance its functionality.\n\n"
        "Key Points:\n"
        "• Users can currently scrape paragraph text and table data.\n"
        "• Our team is actively working to expand scraping capabilities.\n"
        "• Thank you for your patience and support as we improve your experience."
    )

     # Create a text widget with a bold and colored font
    text_widget = tk.Text(content_frame, wrap="word", font=("Helvetica", 16), height=10, width=50, bg="lightblue")
    text_widget.pack(pady=10)

    # Apply different colors to specific lines
    text_widget.tag_configure("blue", foreground="blue")
    text_widget.insert("1.0", info_text)
    text_widget.tag_add("blue", "4.0", "4.22")  # Apply blue color to the "Key Points" line
    text_widget.tag_add("blue", "6.0", "6.49")  # Apply blue color to the first bullet point
    text_widget.tag_add("blue", "7.0", "7.52")  # Apply blue color to the second bullet point
    text_widget.tag_add("blue", "8.0", "8.46")  # Apply blue color to the third bullet point
    text_widget.configure(state="disabled")  # Make the text widget read-only



    content_frame = tk.Frame(webscraping_window, padx=20, pady=20, bg="lightblue")
    content_frame.pack(expand=True, fill="both")

    task_label = tk.Label(content_frame, text="Select the scraping task:", font=("Helvetica", 14), fg="purple", bg="lightblue")
    task_label.grid(row=0, column=0, columnspan=4, padx=20, pady=(0, 10), sticky="w")

    selected_task = tk.StringVar()

    task_frame = ttk.LabelFrame(content_frame, text="Scraping Options", padding=(20, 10))
    task_frame.grid(row=1, column=0, columnspan=4, padx=20, pady=(0, 10), sticky="w")

    style = ttk.Style()
    style.configure("TRadiobutton", font=("Helvetica", 18), background="lightblue")
    style.configure("TRadiobutton", background="lightblue")

    radio_buttons = [
        ttk.Radiobutton(task_frame, text="Discover Fresh News", variable=selected_task, value="scrape_news", style="TRadiobutton"),
        ttk.Radiobutton(task_frame, text="Find Specific Website Keywords", variable=selected_task, value="scrape_keyword", style="TRadiobutton"),
        ttk.Radiobutton(task_frame, text="Explore Google Search", variable=selected_task, value="search_google", style="TRadiobutton"),
        ttk.Radiobutton(task_frame, text="Harvest Data from a Web Address", variable=selected_task, value="scrape_url", style="TRadiobutton"),
        ttk.Radiobutton(task_frame, text="Gather Images", variable=selected_task, value="scrape_images", style="TRadiobutton"),
        ttk.Radiobutton(task_frame, text="Hunt for Job Listings", variable=selected_task, value="scrape_jobs", style="TRadiobutton")
    ]

    # Calculate the number of columns needed
  
    col_count = 4

    row, col = 0, 0
    for rb in radio_buttons[:4]:
        rb.grid(row=row, column=col, padx=20, pady=(0, 10), sticky="w")
        col += 1

    col_count = len(radio_buttons) - 4

    row = 1
    col = (4 - col_count) // 2
    for rb in radio_buttons[4:]:
        rb.grid(row=row, column=col, padx=20, pady=(0, 10), sticky="w")
        col += 1






#?======================================================================================================================================
#?                                       Custom Buttons
#?======================================================================================================================================
    button_text_var = tk.StringVar()

# Initial button label
    
    def update_button_labels():
        global selected_task_value
        selected_task_value = selected_task.get()

        # Update button labels based on the selected task
        # start_button.config(text=f"Start {selected_task_value.capitalize()} Scraping")
        start_button.config(text=f"Start {selected_task_value.capitalize()} Scraping")
        # back_button.config(text=f"Back to {selected_task_value.capitalize()} Menu")
    
    def radio_button_selected():
        update_button_labels()

    # Create a frame to contain the content
    button_text_var.set(lambda: update_button_labels())
    print(button_text_var)
    content_frame = tk.Frame(webscraping_window, padx=20, pady=20 , bg="lightblue")
    content_frame.pack(expand=True, fill="both")

    # Create a container frame to center-align the buttons
    button_frame = tk.Frame(content_frame, bg="lightblue")
    button_frame.pack()

    

    # Create a button to start web scraping with a green background and white text
    start_button = CustomButton(
        button_frame,
        text="Select A option",
        command=lambda:start_web_scraping(selected_task_value , root , open_scraper),
        font=("Helvetica", 16),
        bg="green",
        fg="white",
        hover_bg="darkgreen",  # Change background color on hover
        hover_fg="white",      # Change text color on hover
    )

    # Create a button to go back to the previous menu with a red background and white text
    back_button = CustomButton(
        button_frame,
        text="Previous Menu",
        command=open_scraper,
        font=("Helvetica", 16),
        bg="red",
        fg="white",
        hover_bg="darkred",    # Change background color on hover
        hover_fg="white",      # Change text color on hover
    )
    for radio_button in radio_buttons:
        radio_button.config(command=radio_button_selected)
    # Pack the container frame (center-aligned) and buttons
    button_frame.pack(side="top", pady=20)
    start_button.pack(side="left", padx=10)
    back_button.pack(side="left", padx=10)



#?======================================================================================================================================
#?                                                  End of web scraping module
#?======================================================================================================================================





