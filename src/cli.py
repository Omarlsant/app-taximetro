import time
from src.taximeter import Taximeter
from src.utils import save_history, load_config, update_config

class CLI:
    def __init__(self):
        self.taximeter = Taximeter()
        self.is_stopped = False

    def display_menu(self):
        print("\n--- Menú Principal ---")
        print("1. Iniciar trayecto")
        print("2. Cambiar estado")
        print("3. Finalizar trayecto")
        print("4. Historial")
        print("5. Configurar tarifas")
        print("6. Estado del trayecto")
        print("7. Salir")

    def run(self):
        print("Bienvenido al Taxímetro Digital...")

        while True:
            self.display_menu()
            choice = input("Elige: ")
            try:
                if choice == '1':
                    if not self.taximeter.is_running:
                        self.taximeter.start()
                        self.is_stopped = False
                        print("Trayecto iniciado.")
                    else:
                        print("Ya hay un trayecto en curso.")
                elif choice == '2':
                    if self.taximeter.is_running:
                        self.is_stopped = not self.is_stopped
                        self.taximeter.calculate_fare(self.is_stopped)
                        print(f"Estado: {'Parado' if self.is_stopped else 'En Movimiento'}")
                    else:
                        print("No hay trayecto activo.")
                elif choice == '3':
                    if self.taximeter.is_running:
                        self.taximeter.stop()
                        fare = self.taximeter.total_fare
                        print(f"Trayecto finalizado. Tarifa: {fare:.2f}€")
                        save_history(fare)
                        self.taximeter.reset()
                        self.is_stopped = False
                    else:
                        print("No hay trayecto activo.")
                elif choice == '4':
                    self.show_history()
                elif choice == '5':
                    self.configure_rates()
                elif choice == '6':
                    self.show_trip_status()
                elif choice == '7':
                    break
                else:
                    print("Opción no válida.")
            except Exception as e:
                print(f"Error: {e}")

    def show_trip_status(self):
        if self.taximeter.is_running:
            # Actualiza los valores antes de mostrarlos
            self.taximeter.calculate_fare(self.is_stopped)

            elapsed_time = self.taximeter.elapsed_seconds
            current_fare = self.taximeter.total_fare
            status = "Parado" if self.is_stopped else "En Movimiento"
            print("\n--- Estado del Trayecto ---")
            print(f"Tiempo: {elapsed_time}s")
            print(f"Estado: {status}")
            print(f"Tarifa: {current_fare:.2f}€")
        else:
            print("No hay trayecto activo.")

    def show_history(self):
        try:
            with open("data/history.txt", "r", encoding="utf-8") as f: # Encoding
                print("\n--- Historial ---")
                for line in f:
                    print(line.strip())
        except FileNotFoundError:
            print("Historial vacío.")

    def configure_rates(self):
        print("\n--- Configurar Tarifas ---")
        current_config = self.taximeter.config
        print(f"Tarifa actual (parado): {current_config['stopped_rate']} €/s")
        print(f"Tarifa actual (movimiento): {current_config['moving_rate']} €/s")
        try:
            new_stopped_rate = float(input("Nueva tarifa (parado) o Enter: ").strip() or current_config['stopped_rate'])
            new_moving_rate = float(input("Nueva tarifa (movimiento) o Enter: ").strip() or current_config['moving_rate'])
            update_config(new_stopped_rate, new_moving_rate)
            self.taximeter.config = load_config()
            print("Tarifas actualizadas.")
        except ValueError:
            print("Error: Valores no válidos.")