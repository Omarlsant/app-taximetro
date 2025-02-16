import time
import logging
from src.utils import load_config

class Taximeter:
    def __init__(self):
        self.config = load_config()
        self.is_running = False
        self.start_time = None
        self.last_update_time = None
        self.total_fare = 0.0
        self.elapsed_seconds = 0
        self.logger = self.setup_logger()

    def setup_logger(self):
        logger = logging.getLogger("taximeter")
        logger.setLevel(logging.DEBUG)
        log_file_handler = logging.FileHandler("logs/taximeter.log")
        log_file_handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        log_file_handler.setFormatter(formatter)
        logger.addHandler(log_file_handler)
        return logger

    def start(self):
        if not self.is_running:
            self.is_running = True
            self.start_time = time.time()
            self.last_update_time = self.start_time
            self.total_fare = 0.0
            self.elapsed_seconds = 0
            self.logger.info("Taxímetro iniciado.")
        else:
            self.logger.warning("El taxímetro ya está en funcionamiento.")

    def calculate_fare(self, is_stopped=False):
        if self.is_running:
            now = time.time()
            elapsed_since_last_update = now - self.last_update_time

            if elapsed_since_last_update >= 1.0:
                seconds_to_add = int(elapsed_since_last_update)
                self.elapsed_seconds += seconds_to_add

                if is_stopped:
                    self.total_fare += seconds_to_add * self.config["stopped_rate"]
                else:
                    self.total_fare += seconds_to_add * self.config["moving_rate"]

                self.last_update_time += seconds_to_add

            self.logger.debug(f"Tarifa: {self.total_fare:.2f}€, Tiempo: {self.elapsed_seconds}s, Parado: {is_stopped}")
            return self.total_fare
        else:
            self.logger.error("El taxímetro no está en funcionamiento.")
            return 0.0

    def stop(self):
        if self.is_running:
            self.is_running = False
            #  Elimina COMPLETAMENTE esta línea:
            # self.calculate_fare(self.is_stopped)  <-  ESTO CAUSA EL ERROR
            self.logger.info(f"Taxímetro detenido. Tarifa total: {self.total_fare:.2f}€")
            return self.total_fare
        else:
            self.logger.warning("El taxímetro no está en funcionamiento.")
            return 0.0

    def reset(self):
        self.is_running = False
        self.start_time = None
        self.last_update_time = None
        self.total_fare = 0.0
        self.elapsed_seconds = 0
        self.logger.info("Taxímetro reiniciado.")