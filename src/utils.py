import logging
import time

def setup_logging():
    """Sets up the logging configuration."""
    logging.basicConfig(filename='logs/taximeter.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logging.info("Logging setup complete.")

def format_currency(amount):
    """Formats a number as a currency string."""
    return f"€{amount:.2f}"

def get_elapsed_time(start_time):
    """Calculates the elapsed time since the start_time."""
    return time.time() - start_time

def validate_input(input_str, valid_options):
    """Validates that the input is one of the valid options."""
    try:
        option = int(input_str.strip())
        if option in valid_options:
            return option
        else:
            print("Invalid option. Please select a valid option.")
            return None
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None
