import time
import logging
from src.taximeter import Taximeter
from src.utils import setup_logging, validate_input

# Logging configuration
setup_logging()

# Welcome function
def welcome():
    print("Welcome to the Digital Taximeter in Python")
    print("This program will calculate the fare for your trips based on the elapsed time.")
    print("Use the numeric options to operate the taximeter:")
    print("1. Start trip")
    print("2. Stop the taxi")
    print("3. Show trip status")
    print("4. End trip and show total")

# Main function
def main():
    taximeter = Taximeter()
    welcome()
    
    while True:
        option = validate_input(input("\nSelect an option (1: Start, 2: Stop, 3: Show Status, 4: End): "), [1, 2, 3, 4])
        
        if option is not None:
            if option == 1:
                taximeter.start_trip()
                print("Trip started.")

            elif option == 2:
                taximeter.state = "stopped"
                logging.info("Taxi stopped.")
                print("The taxi is stopped.")

            elif option == 3:
                status = taximeter.get_status()
                print(status)

            elif option == 4:
                total_cost = taximeter.end_trip()
                print(f"Trip ended. Total cost: {total_cost:.2f}")
                break

if __name__ == "__main__":
    main()
