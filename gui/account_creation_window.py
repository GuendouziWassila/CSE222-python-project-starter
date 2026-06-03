"""
Account Creation Window - GUI Layer

This module creates a window for new users to create an account.
Students should implement account creation logic with password strength validation.
"""

import tkinter as tk
from tkinter import messagebox


class AccountCreationWindow:
    """Window for creating a new user account."""
    
    def __init__(self, parent):
        """
        Initialize the account creation window.
        
        Parameters:
        parent: The parent window
        """
        self.window = tk.Toplevel(parent)
        self.window.title("Create Account")
        self.window.geometry("300x250")
        
        # TODO: Create and implement the GUI components
        # - Add username label and entry field
        # - Add password label and entry field (with password masking)
        # - Add confirm password label and entry field
        # - Add create account button
        # - Add cancel button
        # - Display error messages for invalid input
        # - Display success message when account is created
        
        self.username_entry = None
        self.password_entry = None
        self.confirm_password_entry = None
        
        self.create_widgets()
    
    def create_widgets(self):
        """Create and place widgets on the account creation window."""
        # TODO: Implement this function to create the GUI components
        pass
    
    def on_create_clicked(self):
        """Handle create account button click."""
        # TODO: Implement this function to create a new account
        # - Get username, password, and confirm password from entry fields
        # - Validate that passwords match
        # - Call create_account() from business layer
        # - Show error message if account creation fails
        # - Show success message and close window if account is created
        pass
    
    def on_cancel_clicked(self):
        """Handle cancel button click."""
        self.window.destroy()
