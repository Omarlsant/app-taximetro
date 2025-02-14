import unittest
from src.cli import CLI
from src.taximeter import Taximeter
from unittest.mock import patch, MagicMock

class TestCLI(unittest.TestCase):
    @patch('builtins.input', side_effect=['1', '3', '7'])
    def test_run(self, mock_input):
        cli = CLI()
        # Correctly mock is_running behavior
        with patch.object(Taximeter, 'start', side_effect=lambda: setattr(cli.taximeter, 'is_running', True)), \
             patch.object(Taximeter, 'stop', side_effect=lambda: setattr(cli.taximeter, 'is_running', False)), \
             patch.object(Taximeter, 'reset', return_value=None) , \
             patch('src.cli.save_history', MagicMock()) as mock_save_history, \
             patch('src.cli.CLI.show_history', MagicMock()), \
             patch('src.cli.CLI.configure_rates', MagicMock()), \
             patch('src.cli.CLI.show_trip_status', MagicMock()):

            cli.run()

            mock_save_history.assert_called_once()
            cli.taximeter.stop.assert_called_once() # Stop se llama mediante el cli.
            cli.taximeter.start.assert_called_once()


    @patch('builtins.input', side_effect=['4', '7'])
    def test_run_show_history(self, mock_input):
        cli = CLI()
        with patch('src.cli.CLI.show_history') as mock_show_history:
            cli.run()
            mock_show_history.assert_called_once()


    @patch('builtins.input', side_effect=['5', '11', '22', '7'])
    def test_run_configure_rates(self, mock_input):
        cli = CLI()
        with patch('src.cli.CLI.configure_rates', wraps=cli.configure_rates) as mock_configure_rates, \
             patch('src.cli.update_config') as mock_update_config, \
             patch('src.taximeter.load_config', return_value={'stopped_rate': 11.0, 'moving_rate': 22.0}):

            cli.run()
            mock_configure_rates.assert_called_once()
            # Correctly assert the arguments passed to update_config:
            mock_update_config.assert_called_once_with(11.0, 22.0)


    @patch('builtins.input', side_effect=['6', '7'])
    def test_run_show_trip_status_no_active(self, mock_input):
        cli = CLI()
        with patch('src.cli.CLI.show_trip_status', wraps=cli.show_trip_status) as mock_show_trip_status:
            cli.run()
            mock_show_trip_status.assert_called_once()



    @patch('builtins.input', side_effect=['1', '6', '7'])
    def test_run_show_trip_status_active(self, mock_input):
        cli = CLI()
        # Mock is_running and calculate_fare
        with patch.object(Taximeter, 'start', side_effect=lambda: setattr(cli.taximeter, 'is_running', True)), \
             patch.object(Taximeter, 'calculate_fare') as mock_calculate_fare, \
             patch('src.cli.CLI.show_trip_status', wraps=cli.show_trip_status) as mock_show_trip_status:

            cli.run()
            cli.taximeter.start.assert_called_once()
            mock_show_trip_status.assert_called_once()
            mock_calculate_fare.assert_called()



    @patch('builtins.input', side_effect=['1', '2', '6', '7'])  # Start, Change to stopped, show, Exit
    def test_run_change_status_to_stopped_then_show(self, mock_input):
        cli = CLI()
        with patch.object(Taximeter, 'start', side_effect=lambda: setattr(cli.taximeter, 'is_running', True)), \
             patch.object(Taximeter, 'calculate_fare') as mock_calculate_fare, \
             patch('src.cli.CLI.show_trip_status', wraps=cli.show_trip_status) as mock_show_trip_status:

            cli.run()
            mock_calculate_fare.assert_called()
            mock_show_trip_status.assert_called_once()
            self.assertTrue(cli.is_stopped)



    @patch('builtins.input', side_effect=['1', '2', '2', '6', '7'])
    def test_run_change_status_twice_then_show(self, mock_input):
        cli = CLI()
        with patch.object(Taximeter, 'start', side_effect=lambda: setattr(cli.taximeter, 'is_running', True)), \
             patch.object(Taximeter, 'calculate_fare') as mock_calculate_fare, \
             patch('src.cli.CLI.show_trip_status', wraps = cli.show_trip_status) as mock_show_trip_status:

            cli.run()
            mock_calculate_fare.assert_called()
            mock_show_trip_status.assert_called_once()
            self.assertFalse(cli.is_stopped)  # Should be back to running


if __name__ == "__main__":
    unittest.main()