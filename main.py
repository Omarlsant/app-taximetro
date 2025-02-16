from src.cli import CLI
from src.gui import main as run_gui  # Importa la función main de la GUI
import argparse

def main():
    parser = argparse.ArgumentParser(description="Taxímetro Digital")
    parser.add_argument('--cli', action='store_true', help='Ejecutar en modo CLI')
    args = parser.parse_args()

    if args.cli:
        cli = CLI()
        cli.run()  # Ejecuta la interfaz de línea de comandos
    else:
        run_gui()  # Ejecuta la interfaz gráfica

if __name__ == "__main__":
    main()