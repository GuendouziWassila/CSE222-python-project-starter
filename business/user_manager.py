"""
Business Logic module - Business Layer

This module handles account creation, login verification, and password validation.

TODO: Implement the following functions:
- create_account(username, password): Create a new account with validation
- verify_login(username, password): Verify user credentials
- validate_password(password): Check if password meets requirements
- is_username_unique(username): Check if username is unique
"""


def create_account(username, password):
    """
    Create a new account with username and password.
    
    Parameters:
    username (str): The username for the new account
    password (str): The password for the new account
    
    Returns:
    bool: True if account created successfully, False otherwise
    
    Requirements:
    - Username must be unique
    - Password must be at least 9 characters
    - Password must contain at least one uppercase letter
    - Password must contain at least one lowercase letter
    - Password must contain at least one digit
    """
    pass


def verify_login(username, password):
    """
    Verify that the username and password match a stored account.
    
    Parameters:
    username (str): The username to verify
    password (str): The password to verify
    
    Returns:
    bool: True if login credentials are valid, False otherwise
    """
    pass


def validate_password(password):
    """
    Check if a password meets the strength requirements.
    
    Parameters:
    password (str): The password to validate
    
    Returns:
    bool: True if password is valid, False otherwise
    
    Requirements:
    - At least 9 characters long
    - Contains at least one uppercase letter
    - Contains at least one lowercase letter
    - Contains at least one digit
    """
    pass


def is_username_unique(username):
    """
    Check if a username is unique (not already in use).
    
    Parameters:
    username (str): The username to check
    
    Returns:
    bool: True if username is unique, False if it already exists
    """
    pass
