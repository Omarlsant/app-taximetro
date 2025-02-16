import unittest
import tkinter as tk
from src.gui import TaximeterGUI
import os  # Importa os


class TestTaximeterGUI(unittest.TestCase):

    def setUp(self):
        self.root = tk.Tk()
        self.root.withdraw()
        self.gui = TaximeterGUI(self.root)
        self.after_id = None  # Para almacenar el ID de after

        # Limpia el archivo de historial (solución temporal).
        with open("data/history.txt", "w", encoding="utf-8") as f:
            f.write("")

    def tearDown(self):
        if self.after_id is not None:  # Cancela la llamada a after
            self.root.after_cancel(self.after_id)
        self.root.destroy()

    def tearDown(self):
        if self.after_id is not None:  # Cancela la llamada a after
            self.root.after_cancel(self.after_id)
        self.root.destroy()

if __name__ == '__main__':
    unittest.main()