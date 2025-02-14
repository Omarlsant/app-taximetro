import unittest
import os
from src.utils import load_config, update_config, save_history
from unittest.mock import patch, mock_open
import json
from datetime import datetime

class TestUtils(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data='{"stopped_rate": 0.02, "moving_rate": 0.05}')
    def test_load_config(self, mock_file):
        config = load_config()
        self.assertEqual(config['stopped_rate'], 0.02)
        self.assertEqual(config['moving_rate'], 0.05)

    @patch("builtins.open", new_callable=mock_open)
    def test_update_config(self, mock_file):
        update_config(0.03, 0.06)
        mock_file.assert_called_with("data/config.json", "w", encoding="utf-8")

    @patch("builtins.open", new_callable=mock_open)
    def test_save_history(self, mock_file):
        fare = 10.0
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        save_history(fare)
        mock_file().write.assert_called_with(f"Fecha y Hora: {timestamp}, Tarifa: {fare:.2f}€\n")

if __name__ == "__main__":
    unittest.main()
