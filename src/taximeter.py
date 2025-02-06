import time
import logging
from src.utils import format_currency, get_elapsed_time

class Taximeter:
    def __init__(self):
        self.state = "stopped"
        self.trip_start_time = None
        self.total_cost = 0.0
        self.current_cost = 0.0

    def start_trip(self):
        self.trip_start_time = time.time()
        self.state = "moving"
        logging.info("Trip started.")

    def calculate_fare(self):
        elapsed_time = get_elapsed_time(self.trip_start_time)
        elapsed_seconds = int(elapsed_time)  # Calculate full seconds only
        if self.state == "stopped":
            self.current_cost = 0.02 * elapsed_seconds
        elif self.state == "moving":
            self.current_cost = 0.05 * elapsed_seconds
        self.total_cost += self.current_cost
        logging.debug(f"Fare calculated. Elapsed time: {elapsed_seconds} seconds, Current cost: {format_currency(self.current_cost)}, Total cost: {format_currency(self.total_cost)}")
        return self.current_cost

    def end_trip(self):
        self.calculate_fare()
        self.state = "stopped"
        self.trip_start_time = None
        logging.info(f"Trip ended. Total cost: {format_currency(self.total_cost)}")
        return self.total_cost

    def get_status(self):
        if self.trip_start_time is not None:
            elapsed_time = get_elapsed_time(self.trip_start_time)
            elapsed_seconds = int(elapsed_time)  # Calculate full seconds only
            self.calculate_fare()
            status_message = (f"Current state: {self.state}\n"
                              f"Elapsed time: {elapsed_seconds} seconds\n"
                              f"Current cost: {format_currency(self.current_cost)}\n"
                              f"Total cost so far: {format_currency(self.total_cost)}")
            logging.debug(status_message)
            return status_message
        else:
            return "No trip in progress."
