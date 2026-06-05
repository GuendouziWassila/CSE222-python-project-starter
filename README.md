# Python Project Starter - Three-Layer Architecture

A template repository for student projects.

## Project Structure

```
.
├── main.py                 # Entry point - starts the application
├── requirements.txt        # Python dependencies
├── data/                  # Data Layer - handles storage and retrieval
│   ├── __init__.py
│   └── database.py        # Implement account storage logic here
├── gui/                   # GUI Layer - handles user interface
│   ├── __init__.py
│   ├── main_window.py     # Main application window
│   ├── login_window.py    # Login window class
│   └── account_creation_window.py  # Account creation window class
└── business/              # Business Layer - handles core logic
    ├── __init__.py
    └── user_manager.py    # Implement authentication logic here
```

## Three-Layer Architecture

This project uses a three-layer architecture to organize code:

- **Data Layer** - Handles all data storage and retrieval
- **GUI Layer** - Handles the user interface and display
- **Business Layer** - Handles the core logic and business rules

### Data Layer (`data/`)
Responsible for:
- Storing and retrieving account information
- File I/O operations
- Data persistence

**Example Implementation:**
- Implement functions to save accounts to a file
- Implement functions to load accounts from storage
- Implement functions to retrieve account data when needed

### GUI Layer (`gui/`)
Responsible for:
- Creating and managing windows
- Displaying user interface components
- Capturing user input
- Triggering business logic through buttons/events

**Example Implementation:**
- Implement the main window with login and create account buttons
- Implement the login window with username and password entry
- Implement the account creation window with validation feedback
- Implement event handlers for buttons and entry fields
- Connect GUI components to business layer functions

### Business Layer (`business/`)
Responsible for:
- Account creation logic
- Login verification
- Password validation
- Business rules enforcement

**Example Implementation:**
- Implement account creation logic (validation, uniqueness check, storage)
- Implement login verification (checking credentials)
- Implement password strength validation (minimum 9 characters, uppercase, lowercase, digit)
- Handle business logic errors and return appropriate feedback

## Getting Started

1. **Open the project folder in Python IDLE**
   - Open IDLE
   - Go to File → Open and select the `main.py` file

2. **Run the application**
   - Press F5 or go to Run → Run Module

## Common Requirements (All Projects)

All student projects must implement the following core features:

### 1. Account Creation
- Username and password entry in a separate window
- Password strength validation (minimum 9 characters, uppercase letter, lowercase letter, digit)
- Unique username check (no duplicate usernames)
- Store account information
- User-friendly error messages for invalid input

### 2. Login
- Username and password verification in a separate window
- Check credentials against stored accounts
- Clear error messages for invalid credentials
- Access to main application interface after successful login
- Handle Enter key for submission

### 3. Main Interface
- Accessible only after successful login
- Project-specific functionality implemented here
- User logout capability

## Getting Help

Each module includes docstrings describing what needs to be implemented.
Refer to function parameters and return value descriptions for guidance on your implementation.

---

**Complete this starter code with your project features!** 
