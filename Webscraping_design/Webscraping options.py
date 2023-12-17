
import tkinter as tk
from tkinter import ttk

def show_url_entry():
    if selected_task.get() == "scrape_url":
        url_label.grid(row=4, column=0, columnspan=col_count, padx=20, pady=(10, 0), sticky="w")
        url_entry.grid(row=5, column=0, columnspan=col_count, padx=20, pady=(0, 10), sticky="ew")
    else:
        url_label.grid_forget()
        url_entry.grid_forget()

root = tk.Tk()
root.title("Web Scraping Tool")

content_frame = ttk.Frame(root)
content_frame.grid(row=0, column=0, padx=20, pady=20)

# Create a label for selecting the scraping task
task_label = tk.Label(content_frame, text="Select the scraping task:", font=("Helvetica", 14), fg="purple", bg="lightblue")
task_label.grid(row=0, column=0, columnspan=4, padx=20, pady=(0, 10), sticky="w")

# Variable to store the selected task
selected_task = tk.StringVar()

# Create a LabelFrame to wrap the radio buttons for better layout
task_frame = ttk.LabelFrame(content_frame, text="Scraping Options", padding=(20, 10))
task_frame.grid(row=1, column=0, columnspan=4, padx=20, pady=(0, 10), sticky="w")

# Create Radio Buttons for task selection using ttk with larger text size
style = ttk.Style()
style.configure("TRadiobutton", font=("Helvetica", 18))  # Increase text size
style.configure("TRadiobutton", background="lightblue")  # Change background color

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

# Create a grid layout for the first three radio buttons
row, col = 0, 0
for rb in radio_buttons[:4]:
    rb.grid(row=row, column=col, padx=20, pady=(0, 10), sticky="w")
    col += 1

# Calculate the number of columns for the last row
col_count = len(radio_buttons) - 4

# Center the options in the second row
row = 1
col = (4 - col_count) // 2
for rb in radio_buttons[4:]:
    rb.grid(row=row, column=col, padx=20, pady=(0, 10), sticky="w")
    col += 1

# Create an entry widget for entering the URL (visible only when "Scrape data for a URL" is selected)
url_label = tk.Label(content_frame, text="Enter the URL you want to scrape:", font=("Helvetica", 14), fg="purple", bg="lightblue")
url_entry = tk.Entry(content_frame, width=50, font=("Helvetica", 14))

selected_task.trace_add("write", lambda *args: show_url_entry())

root.mainloop()
