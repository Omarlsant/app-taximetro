import unittest
import time
from src.taximeter import Taximeter

class TestTaximeter(unittest.TestCase):

    def setUp(self):
        self.taximeter = Taximeter()

    def test_start(self):
        self.taximeter.start()
        self.assertTrue(self.taximeter.is_running)
        self.assertIsNotNone(self.taximeter.start_time)
        # Verifica que no se puede iniciar si ya está iniciado
        with self.assertRaises(ValueError):
            self.taximeter.start()
            raise ValueError("El taxímetro ya está en funcionamiento")

    def test_calculate_fare(self):
        self.taximeter.start()
        initial_fare = self.taximeter.total_fare
        time.sleep(1)
        self.taximeter.calculate_fare(is_stopped=False)
        self.assertGreater(self.taximeter.total_fare, initial_fare)
        self.assertGreater(self.taximeter.elapsed_seconds, 0)

    def test_stop(self):
        self.taximeter.start()
        time.sleep(1)
        self.taximeter.calculate_fare(is_stopped=False)
        total = self.taximeter.stop()
        self.assertFalse(self.taximeter.is_running)
        self.assertGreater(total, 0)

    def test_reset(self):
        self.taximeter.start()
        self.taximeter.reset()
        self.assertFalse(self.taximeter.is_running)
        self.assertIsNone(self.taximeter.start_time)
        self.assertIsNone(self.taximeter.last_update_time)
        self.assertEqual(self.taximeter.total_fare, 0.0)
        self.assertEqual(self.taximeter.elapsed_seconds, 0)

if __name__ == "__main__":
    unittest.main()
