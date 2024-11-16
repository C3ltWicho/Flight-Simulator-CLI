import unittest
from unittest.mock import patch
import logging
from test_simulation import FlightSimulator
from Logger import setup_logging

class TestFlightSimulator(unittest.TestCase):
    def test_increase_altitude(self):
        simulator = FlightSimulator(1000,300,20)
        simulator.increase_altitude(800)
        self.assertEqual(simulator.altitude,10500)

    def test_decrease_speed(self):
        simulator = FlightSimulator(10000,300,20)
        simulator.decrease_speed(50)
        self.assertEqual(simulator.speed,250)

    def test_invalid_command(self):
        simulator = FlightSimulator(10000,300,20)
        with self.assertRaises(ValueError):
            simulator.decrease_speed("not_a_number")

    
if __name__ == '__main__':
    unittest.main