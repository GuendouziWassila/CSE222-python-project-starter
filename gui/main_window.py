"""
Main Window - GUI Layer

This module creates the main window of the application.
Students should implement the login and create account buttons and their functionality.
"""

import tkinter as tk


class MainWindow:
    """Main application window with login and create account options."""
    
    def __init__(self, root):
        """
        Initialize the main window.
        
        Parameters:
        root: The root tkinter window
        """
        self.root = root
        self.root.title("Main Window")
        self.root.geometry("400x300")
        
        # TODO: Create and implement the GUI components
        # - Add a title label
        # - Add a login button that opens LoginWindow
        # - Add a create account button that opens AccountCreationWindow
        # - Add an exit button
        
        self.create_widgets()
    
    def create_widgets(self):
        """Create and place widgets on the main window."""
        # TODO: Implement this function to create the GUI components
        pass
    
    def on_login_clicked(self):
        """Handle login button click."""
        # TODO: Implement this function to open the login window
        pass
    
    def on_create_account_clicked(self):
        """Handle create account button click."""
        # TODO: Implement this function to open the account creation window
        pass
