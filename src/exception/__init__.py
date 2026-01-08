import sys
import logging

def error_message_detail(error: Exception) -> str:
    """
    Extracts detailed error information including file name, line number,
    and the error message. Must be called from within an except block.
    """
    _, _, exc_tb = sys.exc_info()

    assert exc_tb is not None, "error_message_detail must be called inside an except block"

    # Get the file name where the exception occurred
    file_name = exc_tb.tb_frame.f_code.co_filename

    # Create a formatted error message string with file name, line number, and the actual error
    line_number = exc_tb.tb_lineno
    error_message = f"Error occurred in python script: [{file_name}] at line number [{line_number}]: {str(error)}"
    
    # Log the error for better tracking
    logging.error(error_message)
    
    return error_message

class MyException(Exception):
    """
    Custom exception class for handling errors in the US visa application.
    """
    def __init__(self, error: Exception):
        # Call the base class constructor with the error message
        super().__init__(error)

        # Format the detailed error message using the error_message_detail function
        self.error_message = error_message_detail(error)

    def __str__(self) -> str:
        # Returns the string representation of the error message.
        return self.error_message