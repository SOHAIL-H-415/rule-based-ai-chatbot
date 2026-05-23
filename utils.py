"""
utils.py

Provides utility and helper functions for the Rule-Based AI Chatbot.
Handles terminal styling, input sanitization, dynamic timestamps, and cross-platform terminal controls.
Designed for clean separation of concerns and high readability.
"""

import os
from datetime import datetime

# ANSI Escape Sequences for terminal styling
COLOR_CYAN = "\033[96m"
COLOR_GREEN = "\033[92m"
COLOR_YELLOW = "\033[93m"
COLOR_RED = "\033[91m"
COLOR_GRAY = "\033[90m"
COLOR_BOLD = "\033[1m"
COLOR_RESET = "\033[0m"

def sanitize_input(text: str) -> str:
    """
    Cleans up user input for robust pattern matching.
    Converts text to lower case and strips leading/trailing whitespaces.
    
    Args:
        text (str): The raw input string from the user.
        
    Returns:
        str: The sanitized and normalized input string.
    """
    if text is None:
        return ""
    return text.strip().lower()

def get_timestamp() -> str:
    """
    Retrieves the current local system time formatted as HH:MM:SS.
    
    Returns:
        str: Formatted time string.
    """
    return datetime.now().strftime("%H:%M:%S")

def clear_screen() -> None:
    """
    Clears the terminal screen. Handles both Windows ('cls') and Unix-like ('clear') systems.
    """
    os.system("cls" if os.name == "nt" else "clear")

def print_banner() -> None:
    """
    Displays a professional, clean terminal banner introducing the chatbot.
    """
    banner = f"""
{COLOR_CYAN}{COLOR_BOLD}=============================================================================
  ____       _             ____                       _     _   ___  
 |  _ \\ _  _| | ___       | __ )  __ _ ___  ___  __| |   / \\ |_ _| 
 | |_) | | | | |/ _ \\_____|  _ \\ / _` / __|/ _ \\/ _` |  / _ \\ | |  
 |  _ <| |_| | |  __/_____| |_) | (_| \\__ \\  __/ (_| | / ___ \\| |  
 |_| \\_\\\\__,_|_|\\___|      |____/ \\__,_|___/\\___|\\__,_|/_/   \\_\\___| 
                                                                    
              --- Deterministic Rule-Based Assistant (v1.0) ---
============================================================================={COLOR_RESET}
Type {COLOR_GREEN}'help'{COLOR_RESET} to view all system commands and capabilities.
Type {COLOR_YELLOW}'clear'{COLOR_RESET} to clear the terminal window.
Type {COLOR_RED}'exit'{COLOR_RESET}, {COLOR_RED}'quit'{COLOR_RESET}, or {COLOR_RED}'bye'{COLOR_RESET} to safely exit the application.
"""
    print(banner)

def format_bot_response(response_text: str) -> str:
    """
    Formats the chatbot's output to include a dynamic timestamp and a stylized prefix.
    
    Args:
        response_text (str): The raw response text.
        
    Returns:
        str: The formatted response ready for the console.
    """
    timestamp = get_timestamp()
    prefix = f"{COLOR_GRAY}[{timestamp}]{COLOR_RESET} {COLOR_CYAN}{COLOR_BOLD}Bot:{COLOR_RESET} "
    return f"{prefix}{response_text}"

def format_user_prefix() -> str:
    """
    Returns a stylized input prompt prefix for the user.
    """
    timestamp = get_timestamp()
    return f"{COLOR_GRAY}[{timestamp}]{COLOR_RESET} {COLOR_GREEN}{COLOR_BOLD}You >{COLOR_RESET} "
