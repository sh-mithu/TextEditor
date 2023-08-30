import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r') as file:
            text.delete('1.0', tk.END)
            text.insert(tk.END, file.read())

def save_file(event=None):
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text.get('1.0', tk.END))

def create_new_tab():
    new_text = tk.Text(notebook)
    new_text.pack(fill='both', expand=True)
    notebook.add(new_text, text="Untitled" + str(notebook.index("end")))

# Create the main application window
root = tk.Tk()
root.title("Text Pad")

# Create a Notebook widget to hold tabs
notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True)

# Create a Text widget for displaying and editing text in the first tab
text = tk.Text(notebook)
text.pack(fill='both', expand=True)

# Add the first tab to the notebook
notebook.add(text, text="Untitled")

# Bind Control + S to the save_file function
text.bind('<Control-s>', save_file)

# Bind Control + C to create a new tab
root.bind('<Control-n>', lambda event: create_new_tab())


# Create a menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Create a File menu
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="New Tab", command=create_new_tab)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Start the main event loop
root.mainloop()
