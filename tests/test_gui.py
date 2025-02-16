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

    def test_initial_state(self):
        self.assertEqual(self.gui.fare_display['text'], "0.00 €")
        self.assertEqual(self.gui.time_display['text'], "0 s")
        self.assertEqual(self.gui.status_display['text'], "Detenido")
        self.assertEqual(str(self.gui.start_button['state']), 'normal')  # Corregido
        self.assertEqual(str(self.gui.stop_button['state']), 'disabled')  # Corregido
        self.assertEqual(str(self.gui.end_button['state']), 'disabled')  # Corregido

    def test_start_stop_end_trip(self):
        self.gui.start_button.invoke()
        self.root.update()  # ¡Importante! Procesa los eventos.
        self.assertEqual(str(self.gui.start_button['state']), 'disabled')
        self.assertEqual(str(self.gui.stop_button['state']), 'normal')
        self.assertEqual(str(self.gui.end_button['state']), 'normal')
        self.assertEqual(self.gui.status_display['text'], "En Movimiento")
        self.assertTrue(self.gui.taximeter.is_running)
        self.assertFalse(self.gui.is_stopped)

        self.gui.stop_button.invoke()
        self.root.update()  # ¡Importante!
        self.assertEqual(self.gui.status_display['text'], "Parado")
        self.assertTrue(self.gui.is_stopped)

        self.gui.stop_button.invoke()
        self.root.update()  # ¡Importante!
        self.assertEqual(self.gui.status_display['text'], "En Movimiento")
        self.assertFalse(self.gui.is_stopped)

        self.gui.end_button.invoke()
        self.root.update()  # ¡Importante!  <--  AQUÍ estaba el problema.
        self.assertEqual(str(self.gui.start_button['state']), 'normal')
        self.assertEqual(str(self.gui.stop_button['state']), 'disabled')
        self.assertEqual(str(self.gui.end_button['state']), 'disabled')
        self.assertFalse(self.gui.taximeter.is_running)

    def test_reset_trip(self):
        self.gui.reset_button.invoke()  # Reinicia
        self.root.update()  #  <--  ¡MUY IMPORTANTE! Procesa el evento.

        self.assertEqual(self.gui.fare_display['text'], "0.00 €")
        self.assertEqual(self.gui.time_display['text'], "0 s")
        self.assertEqual(self.gui.status_display['text'], "Detenido")
        self.assertEqual(str(self.gui.start_button['state']), 'normal')
        self.assertEqual(str(self.gui.stop_button['state']), 'disabled')
        self.assertEqual(str(self.gui.end_button['state']), 'disabled')
        self.assertFalse(self.gui.taximeter.is_running)

    def tearDown(self):
        if self.after_id is not None:  # Cancela la llamada a after
            self.root.after_cancel(self.after_id)
        self.root.destroy()

    def test_load_history(self):
        self.gui.load_history()
        self.root.update()
        self.assertEqual(self.gui.history_text.get("1.0", "end-1c"), "") # Corregido

if __name__ == '__main__':
    unittest.main()