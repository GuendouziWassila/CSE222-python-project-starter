"""
Main entry point for the application.
This file initializes and runs the GUI application.
"""

from gui.main_window import MainWindow
from tkinter import Tk


def main():
    """Initialize and start the application."""
    # Create the root window
    root = Tk()
    root.title("Project Application")
    root.geometry("600x400")
    
    # Create and display the main window
    app = MainWindow(root)
    
    # Start the application
    root.mainloop()


if __name__ == "__main__":
    main()
