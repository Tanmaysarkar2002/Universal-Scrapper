
#========================================================================================================================================
# Description: This is the main interface of the Universal Scraper. It contains the welcome page, the project features page,
#                                                 and the scraper page.
# =====================================================================================================================================


#=========================================================================================================================================
#                                           Import the required libraries
#=========================================================================================================================================


import tkinter as tk
from tkinter import font as tkfont
from tkinter import messagebox
import random
import pyttsx3
import datetime
from tkinter import PhotoImage
from Pdfscraping.module_pdf_scraping import open_pdf_scraping_module
from Webscraping_design.module_webscraping import open_webscraping_module



#=========================================================================================================================================
#                                           Function to convert text to speech
#=========================================================================================================================================

def text_to_speech(user_text):
    engine = pyttsx3.init()
    engine.say(user_text)
    engine.runAndWait()

#=========================================================================================================================================
#                                              Function to destroy the main application window
#=========================================================================================================================================

def destroy_main_window():
    root.quit() 


#=========================================================================================================================================
#                                                Function to create a random RGB color
#=========================================================================================================================================

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f'#{r:02x}{g:02x}{b:02x}'  # Convert to hex format



    
#=========================================================================================================================================
#                                                Function to open the Excel scraping module
#=========================================================================================================================================

# Function to open the Excel scraping module
def open_excel_scraping_module():
    # Replace "module_excel_scraping.py" with the actual path to your Excel scraping module
    # import module_excel_scraping
    message_window = tk.Toplevel(root)

    # Create a label with the message
    message_label = tk.Label(message_window, text="Oops, not available yet.", font=("Arial", 20))
    message_label.pack(padx=20, pady=20)

    # Schedule the window to be closed after 5 seconds
    message_window.after(5000, message_window.destroy)

    



#=========================================================================================================================================
#                               >>>>>>>>>>>>>>>>>>>>>>>>>>> Random color function<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#=========================================================================================================================================


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f'#{r:02x}{g:02x}{b:02x}'  # Convert to hex format







#=========================================================================================================================================
#                               >>>>>>>>>>>>>>>>>>>>>>>>>>> OPEN SCRAPER PAGE<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#=========================================================================================================================================

def open_scraper():

#=========================================================================================================================================
#                               >>>>>>>>>>>>>>>>>>>>>>>>>>> Custom Button<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#=========================================================================================================================================


    class CustomButton(tk.Button):
        def __init__(self, master=None, cnf={}, **kw):
            tk.Button.__init__(self, master, cnf, **kw)
            self.original_bg = self.cget("background")
            self.bind("<Enter>", self.on_enter)
            self.bind("<Leave>", self.on_leave)
            self.tooltip = None

        def on_enter(self, event):
            self.configure(bg='lightgray')
            if self.tooltip:
                self.tooltip.show()

        def on_leave(self, event):
            self.configure(bg=self.original_bg)
            if self.tooltip:
                self.tooltip.hide()


#=========================================================================================================================================
#                               >>>>>>>>>>>>>>>>>>>>>>>>>>>Tooltip<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#=========================================================================================================================================


    class Tooltip:
        def __init__(self, widget, text):
            self.widget = widget
            self.text = text

        def show(self):
            x, y, _, _ = self.widget.bbox("insert")
            x += self.widget.winfo_rootx() + self.widget.winfo_width() + 10
            y += self.widget.winfo_rooty()

            self.tooltip = tk.Toplevel(self.widget)
            self.tooltip.wm_overrideredirect(True)
            self.tooltip.wm_geometry(f"+{x}+{y}")

            label = tk.Label(self.tooltip, text=self.text, background="lightyellow", relief="solid", borderwidth=1, font=("Helvetica", 14), wraplength=200)
            label.pack()

        def hide(self):
            if hasattr(self, 'tooltip') and self.tooltip:
                self.tooltip.destroy()

    def create_option_button(text, command, tooltip_text, text_color="white" , bg_color=None):
        if bg_color is None:
            bg_color = random_color()  # Use random color by default

        option_button = CustomButton(
            open_scraper_button_frame,
            text=text,
            command=command,
            fg="white",
            font=("Helvetica", 24),
            width=20,
            height=3,
            bg=bg_color,
        )
        option_button.pack(fill="x", padx=10)  # Pack buttons vertically
        
        option_button.tooltip = Tooltip(option_button, tooltip_text)






#=========================================================================================================================================
#                               >>>>>>>>>>>>>>>>>>>>>>>>>>> Open Scraper Window<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#=========================================================================================================================================

    # Remove previous content in the root window
    for widget in root.winfo_children():
        widget.destroy()

    root.title("Open Scraper")
    root.configure(bg="lightblue")

    current_date = datetime.datetime.now().strftime("%B %d, %Y")  # Get the current date in a formatted string

    header_label = tk.Label(root, text=f"Welcome to the Scraper Options Page - {current_date}", font=("Helvetica", 32), bg="lightblue", fg="blue")
    header_label.pack(pady=20)

    description_label = tk.Label(root, text="Select an option below to get started:", font=("Helvetica", 18), bg="lightblue")
    description_label.pack(pady=10)

    global open_scraper_button_frame
    # Create a frame to contain the buttons in the scraper page
    open_scraper_button_frame = tk.Frame(root , bg="lightblue")
    open_scraper_button_frame.pack(pady=30)

    
    

#=========================================================================================================================================
#                               >>>>>>>>>>>>>>>>>>>>>>>>>>> Create Option Button<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#=========================================================================================================================================


    create_option_button("Webscraping", lambda: open_webscraping_module(root, open_scraper), "Perform web scraping and data extraction from websites.")
    create_option_button("PDF Scraping", lambda: open_pdf_scraping_module(root, main_window, open_scraper), "Extract data from PDF files.")
    create_option_button("Excel Scraping", open_excel_scraping_module, "Extract data from Excel spreadsheets.")
    create_option_button("Previous Menu", show_project_features, "Go back to the previous menu.")
    create_option_button("Exit", destroy_main_window, "Exit the application.",bg_color="red")
    # This code keeps the option frame and displays the text on hover while having the button's text initially empty.

#=========================================================================================================================================
#                               >>>>>>>>>>>>>>>>>>>>>>>>>>> PROJECT FEATURES PAGE<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#=========================================================================================================================================

# Function to show the project features page


def show_project_features():



    # Define your project_features_window.destroy function
    def close_project_features_window():
        root.destroy()

    root.title("Open Scraper")
    root.configure(bg="lightblue")

    # Remove previous content in the root window

    for widget in root.winfo_children():
        widget.destroy()

    # Create a custom font for the project name
    project_name_font = tkfont.Font(family="Helvetica", size=30, weight="bold")

    # Create a label with the project name
    project_name_label = tk.Label(root, text="The Universal Scraper - Harvesting Data, One Source at a Time", font=project_name_font, fg="blue",bg="lightblue")
    project_name_label.pack(pady=20)

    # Create a custom font for the project description
    project_description_font = tkfont.Font(family="Helvetica", size=18)


#=========================================================================================================================================
#                               >>>>>>>>>>>>>>>>>>>>>>>>>>> PROJECT FEATURES LIST<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#=========================================================================================================================================

    # Create a list of project features with a description and a color
    project_features_list = [
        ("🌐 Unbounded Reach: The Universal Scraper navigates the digital realm, reaching out to websites, PDFs, Excel spreadsheets, and more. It harmoniously collects data from across the web's multiverse.", "green"),
        ("🕵️ Stealthy Intelligence: Equipped with intelligent algorithms, this scraper is not just efficient; it's discreet. It gathers information with the subtlety of a whisper in a crowded room.", "blue"),
        ("🌈 Customized Palette: Tailor the scraper's behavior to your precise needs. Whether it's mining product data for e-commerce, extracting research from academic journals, or parsing financial reports, the Universal Scraper adapts to your requirements.", "red"),
        ("🛠️ User-Friendly Interface: Beneath its formidable capabilities lies an intuitive interface designed with you in mind. Extracting data becomes a pleasurable journey, not a technical challenge.", "purple"),
        ("📈 Data-Driven Decisions: The Universal Scraper empowers you to make data-driven decisions. It's time to harness the power of data.", "orange"),
        ("📊 Data Visualization: The Universal Scraper is the first step in the data journey. Once you've collected your data, you can visualize it with the Universal Scraper's companion app, the Universal Visualizer.", "brown"),
        ("📚 Data Storage: The Universal Scraper is the first step in the data journey. Once you've collected your data, you can store it with the Universal Scraper's companion app, the Universal Storage.", "green"),
        ("📝 Data Analysis: The Universal Scraper is the first step in the data journey. Once you've collected your data, you can analyze it with the Universal Scraper's companion app, the Universal Analyzer.", "teal"),
    ]

    for feature, color in project_features_list:
        feature_label = tk.Label(root, text=feature, font=project_description_font, wraplength=1500, justify="left", fg=color , bg="lightblue")
        feature_label.pack(pady=10, anchor="w")

#=========================================================================================================================================
#                               >>>>>>>>>>>>>>>>>>>>>>>>>>> Custom Button<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#=========================================================================================================================================

    class CustomButton(tk.Button):
        def __init__(self, parent, text, command, width=20, height=2):
            super().__init__(parent, text=text, command=command, font=("Helvetica", 16), width=width, height=height)
            self.configure(bg=random_color(), fg="white")
            self.original_bg = self.cget("background")
            self.bind("<Enter>", self.on_enter)
            self.bind("<Leave>", self.on_leave)

        def on_enter(self, event):
            self.configure(bg="blue")  # Change background color on mouse hover

        def on_leave(self, event):
            self.configure(bg=self.original_bg)  # Restore original background color on mouse leave
    
    # Create a frame to contain the buttons in project_features_window
    project_features_button_frame = tk.Frame(root, bg="lightblue")
    project_features_button_frame.pack(pady=30)


    # Create the "Open Universal Scraper" button with a random color
    open_button = CustomButton(project_features_button_frame, text="Open Universal Scraper", command=open_scraper)
    open_button.grid(row=0, column=0, padx=10)

    # Define your on_enter and on_leave functions here

    

    # Create the "Back to Main Window" button with a random color
    main_window_button = CustomButton(project_features_button_frame, text="Back to Main Window", command=lambda: main_window())
    main_window_button.grid(row=0, column=1, padx=10)


#========================================================================================================================================
#                               >>>>>>>>>>>>>>>>>>>>>>>>>>> MAIN WINDOW<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#========================================================================================================================================




#=========================================================================================================================================
#                              >>>>>>>>>>>>>>>>>>>>>>> Create the main window<<<<<<<<<<<<<<<<<<<<<<<
#=========================================================================================================================================
def main_window():

    class CustomButton(tk.Button):
        def __init__(self, parent, text, command, width=20, height=2):
            super().__init__(parent, text=text, command=command, font=("Helvetica", 24), width=width, height=height)
            if text == "Exit":
                self.configure(bg="red", fg="white")
            else:
                self.configure(bg=random_color(), fg="white")
            self.original_bg = self.cget("background")
            self.bind("<Enter>", self.on_enter)
            self.bind("<Leave>", self.on_leave)

        def on_enter(self, event):
            self.configure(bg="blue")  # Change background color on mouse hover

        def on_leave(self, event):
            self.configure(bg=self.original_bg)  # Restore original background color on mouse leave

    
    for widget in root.winfo_children():
        widget.destroy()

    # Set the background color for the entire content area
    

    # Create a custom font for the project name
    project_name_font = tkfont.Font(family="Helvetica", size=36, weight="bold", underline=1)

    # Create a label with the project name on the welcome page
    project_name_label = tk.Label(root, text="The Universal Scraper - Harvesting Data, One Source at a Time", font=project_name_font, fg="blue", bg="lightblue")
    project_name_label.pack(pady=20)

    # Create a custom font for the project description on the welcome page
    project_description_font = tkfont.Font(family="Helvetica", size=18)

    # Create a frame to contain the description label, quote, and logo
    description_frame = tk.Frame(root, bg="lightblue")
    description_frame.pack(pady=20)

    # Create a label with the project description on the welcome page
    project_description_label = tk.Label(description_frame, text="Welcome to The Universal Scraper, your gateway to unlocking the power of data from diverse sources effortlessly and elegantly. Explore the features that make this scraper a data virtuoso:", font=project_description_font, wraplength=1000, justify="center", fg="green", bg="lightblue")
    project_description_label.pack(pady=20)

    # Add a quote related to scraping
    quote_label = tk.Label(description_frame, text='"Data is the new oil, and scraping is the drill."', font=("Helvetica", 18), fg="gray", bg="lightblue")
    quote_label.pack(pady=20)

   # Create a container to hold the PhotoImage object
    image_container = tk.Label(root, bg="lightblue")
    image_container.pack(fill=tk.BOTH, expand=True)

    # Load the image and retain a reference to it
    logo_image = PhotoImage(file=r"E:\projects_new\Major_Project\images\images.png")

    # Set the image in the container
    image_container.config(image=logo_image)
    image_container.image = logo_image  # Retain a reference to the image

#=========================================================================================================================================
#                               Create a frame to contain the buttons in the welcome page
#=========================================================================================================================================


    button_frame = tk.Frame(root, bg="lightblue")
    button_frame.pack(pady=30)

    # Create a button to show the project features page on the welcome page


    project_features_button = CustomButton(button_frame, text="Project Features", command=show_project_features)
    project_features_button.pack(side="left", padx=10)

    # Create the "Exit" button with a random color
    exit_button = CustomButton(button_frame, text="Exit", command=root.quit)
    exit_button.pack(side="left", padx=10)

    # Create the "Read Me" button with a random color


    speech_button = CustomButton(button_frame, text="Read Me", command=lambda: text_to_speech("Welcome to The Universal Scraper"))
    speech_button.pack(side="left", padx=10)

#=========================================================================================================================================
#                                               Start the Tkinter event loop
#========================================================================================================================================

def main():
    global root
    root = tk.Tk()
    root.title("Universal Scraper")
    root.state('zoomed')
    root.configure(bg="lightblue")
    main_window()
    root.mainloop()

if __name__ == "__main__":
    main()





#=========================================================================================================================================
#                                               END OF THE PROGRAM
#========================================================================================================================================