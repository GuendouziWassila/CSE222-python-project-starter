"""
Login Window - GUI Layer

This module creates a login window where users can enter their credentials.
Students should implement the login verification logic and error handling.
"""

import tkinter as tk
from tkinter import messagebox


class LoginWindow:
    """Login window for user authentication."""
    
    def __init__(self, parent):
        """
        Initialize the login window.
        
        Parameters:
        parent: The parent window
        """
        self.window = tk.Toplevel(parent)
        self.window.title("Login")
        self.window.geometry("300x200")
        
        # TODO: Create and implement the GUI components
        # - Add username label and entry field
        # - Add password label and entry field (with password masking)
        # - Add login button
        # - Add cancel button
        # - Display error messages for invalid credentials
        
        self.username_entry = None
        self.password_entry = None
        
        self.create_widgets()
    
    def create_widgets(self):
        """Create and place widgets on the login window."""
        # TODO: Implement this function to create the GUI components
        pass
    
    def on_login_clicked(self):
        """Handle login button click."""
        # TODO: Implement this function to verify credentials
        # - Get username and password from entry fields
        # - Call verify_login() from business layer
        # - Show error message if login fails
        # - Close window and show main interface if login succeeds
        pass
    
    def on_cancel_clicked(self):
        """Handle cancel button click."""
        self.window.destroy()
