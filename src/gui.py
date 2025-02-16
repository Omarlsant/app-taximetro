import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from src.taximeter import Taximeter
from src.utils import save_history, load_config


class TaximeterGUI:
    def __init__(self, master):
        self.master = master
        master.title("Taxímetro Digital")

        self.taximeter = Taximeter()
        self.is_stopped = False
        
        self.create_widgets()
        self.load_initial_config()

        self.update_display()


    def create_widgets(self):
        """Crea y posiciona todos los widgets en la interfaz."""

        main_frame = ttk.Frame(self.master, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        ttk.Label(main_frame, text="Tarifa:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.fare_display = ttk.Label(main_frame, text="0.00 €")
        self.fare_display.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=5, pady=5)

        ttk.Label(main_frame, text="Tiempo:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.time_display = ttk.Label(main_frame, text="0 s")
        self.time_display.grid(row=1, column=1, sticky=(tk.W, tk.E), padx=5, pady=5)

        ttk.Label(main_frame, text="Estado:").grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
        self.status_display = ttk.Label(main_frame, text="Detenido")
        self.status_display.grid(row=2, column=1, sticky=(tk.W, tk.E), padx=5, pady=5)

        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=3, column=0, columnspan=2, pady=10)

        self.start_button = ttk.Button(button_frame, text="Iniciar", command=self.start_trip)
        self.start_button.pack(side=tk.LEFT, padx=5)

        self.stop_button = ttk.Button(button_frame, text="Parar/Reanudar", command=self.toggle_stop)
        self.stop_button.pack(side=tk.LEFT, padx=5)
        self.stop_button.config(state=tk.DISABLED)

        self.end_button = ttk.Button(button_frame, text="Finalizar", command=self.end_trip)
        self.end_button.pack(side=tk.LEFT, padx=5)
        self.end_button.config(state=tk.DISABLED)

        self.reset_button = ttk.Button(button_frame, text="Reiniciar", command=self.reset_trip)
        self.reset_button.pack(side=tk.LEFT, padx=5)

        config_frame = ttk.Frame(main_frame)
        config_frame.grid(row=4, column=0, columnspan=2, pady=5)
        self.config_button = ttk.Button(config_frame, text="Configurar Tarifas", command=self.configure_rates)
        self.config_button.pack(side=tk.LEFT, padx=5)

        history_frame = ttk.Frame(main_frame)
        history_frame.grid(row=5, column=0, columnspan=2, pady=5, sticky=(tk.W, tk.E, tk.N, tk.S))

        ttk.Label(history_frame, text="Historial:").pack(side=tk.TOP, anchor=tk.W)
        self.history_text = tk.Text(history_frame, height=10, width=40, wrap=tk.WORD, state=tk.DISABLED)
        self.history_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = ttk.Scrollbar(history_frame, command=self.history_text.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.history_text['yscrollcommand'] = scrollbar.set

        self.load_history()

        main_frame.columnconfigure(1, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)


    def load_initial_config(self):
        """Carga la configuración inicial desde el archivo."""
        self.update_rate_labels()

    def start_trip(self):
        """Inicia el taxímetro."""
        if not self.taximeter.is_running:
            self.taximeter.start()
            self.is_stopped = False
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)
            self.end_button.config(state=tk.NORMAL)
            self.status_display.config(text="En Movimiento")
            self.update_display()
            messagebox.showinfo("Taxímetro", "Viaje iniciado.")
        else:
            messagebox.showwarning("Taxímetro", "Ya hay un viaje en curso.")

    def toggle_stop(self):
        """Pausa o reanuda el taxímetro (cambia el estado)."""
        if self.taximeter.is_running:
            self.is_stopped = not self.is_stopped
            self.status_display.config(text="Parado" if self.is_stopped else "En Movimiento")
            messagebox.showinfo("Taxímetro", f"Viaje {'Pausado' if self.is_stopped else 'Reanudado'}.")

    def end_trip(self):
        if self.taximeter.is_running:
            # 1. Calcula la tarifa FINAL *antes* de detener:
            self.taximeter.calculate_fare(self.is_stopped)
            # 2. Detiene el taxímetro:
            final_fare = self.taximeter.stop()

            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)
            self.end_button.config(state=tk.DISABLED)
            save_history(final_fare)
            self.load_history()
            messagebox.showinfo("Taxímetro", f"Viaje finalizado. Tarifa total: {final_fare:.2f}€")
            self.update_display()  # Actualiza la GUI para reflejar la tarifa final.
        else:
            messagebox.showwarning("Taxímetro", "No hay un viaje en curso.")

    def reset_trip(self):
        """Reinicia el taxímetro."""
        self.taximeter.reset()
        self.is_stopped = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.end_button.config(state=tk.DISABLED)
        self.status_display.config(text="Detenido")
        self.update_display()
        messagebox.showinfo("Taxímetro", "Taxímetro reiniciado.")

    def update_display(self):
        if self.taximeter.is_running:
            fare = self.taximeter.calculate_fare(self.is_stopped)
            self.fare_display.config(text=f"{fare:.2f} €")
            self.time_display.config(text=f"{self.taximeter.elapsed_seconds} s")
            self.master.after(1000, self.update_display)

    def configure_rates(self):
        """Abre un diálogo para configurar las tarifas."""
        dialog = tk.Toplevel(self.master)
        dialog.title("Configurar Tarifas")
        dialog.transient(self.master)
        dialog.grab_set()

        ttk.Label(dialog, text="Tarifa por segundo (parado):").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        stopped_rate_entry = ttk.Entry(dialog)
        stopped_rate_entry.grid(row=0, column=1, padx=5, pady=5, sticky=(tk.W, tk.E))
        stopped_rate_entry.insert(0, str(self.taximeter.config['stopped_rate']))


        ttk.Label(dialog, text="Tarifa por segundo (en movimiento):").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        moving_rate_entry = ttk.Entry(dialog)
        moving_rate_entry.grid(row=1, column=1, padx=5, pady=5, sticky=(tk.W, tk.E))
        moving_rate_entry.insert(0, str(self.taximeter.config['moving_rate']))

        def save_rates():
            """Función interna para guardar las tarifas."""
            try:
                new_stopped_rate = float(stopped_rate_entry.get())
                new_moving_rate = float(moving_rate_entry.get())
                if new_stopped_rate < 0 or new_moving_rate < 0:
                    raise ValueError("Las tarifas no pueden ser negativas.")

                self.taximeter.config['stopped_rate'] = new_stopped_rate
                self.taximeter.config['moving_rate'] = new_moving_rate
                self.update_rate_labels()
                load_config()
                save_history(0)

                messagebox.showinfo("Tarifas", "Tarifas actualizadas correctamente.")
                dialog.destroy()

            except ValueError as e:
                messagebox.showerror("Error", str(e))

        save_button = ttk.Button(dialog, text="Guardar", command=save_rates)
        save_button.grid(row=2, column=0, columnspan=2, pady=10)

        dialog.columnconfigure(1, weight=1)
        dialog.resizable(False, False)
        dialog.wait_window(dialog)

    def update_rate_labels(self):
        """Actualiza las etiquetas de las tarifas (si las tuvieras)."""
        pass

    def load_history(self):
        """Carga y muestra el historial en el widget Text."""
        try:
            with open("data/history.txt", "r", encoding="utf-8") as f:
                history_content = f.read()
                self.history_text.config(state=tk.NORMAL)
                self.history_text.delete("1.0", tk.END)
                self.history_text.insert(tk.END, history_content)
                self.history_text.config(state=tk.DISABLED)
                self.history_text.see(tk.END)

        except FileNotFoundError:
            self.history_text.config(state=tk.NORMAL)
            self.history_text.delete("1.0", tk.END)
            self.history_text.insert(tk.END, "Historial vacío.")
            self.history_text.config(state=tk.DISABLED)

def main():
    root = tk.Tk()
    gui = TaximeterGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()