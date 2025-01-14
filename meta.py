import tkinter as tk
from tkinter import filedialog
from tika import parser

# Set up the tkinter root window (it will not show, since we just need the dialog)
root = tk.Tk()
root.withdraw()  # Hide the main tkinter window

# Open the file dialog to select a file
file_path = filedialog.askopenfilename(
    title="Select a file",
    filetypes=[("All files", "*.*"), ("PDF files", "*.pdf"), ("Word files", "*.docx"), ("Text files", "*.txt")]
)

# Check if the user selected a file
if file_path:
    print(f"File selected: {file_path}")
    
    # Parse the selected file using Tika
    parsed = parser.from_file(file_path)

    # Print the content and metadata
    print("\nContent:")
    print(parsed['content'])

    print("\nMetadata:")
    print(parsed['metadata'])
else:
    print("No file selected.")
