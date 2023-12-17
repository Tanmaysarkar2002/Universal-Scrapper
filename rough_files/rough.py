import tkinter as tk

def open_scraper_window():
    # Remove previous content in the root window
    for widget in root.winfo_children():
        widget.destroy()

    root.title("Open Scraper")
    root.configure(bg="lightblue")

    label = tk.Label(root, text="Select an option:", font=("Helvetica", 24), bg="lightblue", fg=random_color())
    label.pack(pady=20)

def random_color():
    # Replace this with your random color generation logic
    pass

root = tk.Tk()
root.state('zoomed')  # Maximize the window

open_scraper_window_button = tk.Button(root, text="Open Scraper Window", command=open_scraper_window)
open_scraper_window_button.pack(pady=20)

root.mainloop()
