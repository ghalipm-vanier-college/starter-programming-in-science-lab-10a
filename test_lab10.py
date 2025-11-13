## ✅ **test_lab10.py**

# DO NOT CHANGE THIS FILE, OR ZERO MARK WILL BE ASSIGNED.
import unittest
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from Lab10 import plot_curve, plot_trig_functions, plot_temperature_data, plot_population_data

class TestLab10(unittest.TestCase):
    def test_plot_curve(self):
        """Test that plot_curve executes without error."""
        try:
            plot_curve()
            success = True
        except Exception:
            success = False
        self.assertTrue(success, "plot_curve failed to execute correctly")

    def test_plot_trig_functions(self):
        """Test that plot_trig_functions executes without error."""
        try:
            plot_trig_functions()
            success = True
        except Exception:
            success = False
        self.assertTrue(success, "plot_trig_functions failed to execute correctly")

    def test_plot_temperature_data(self):
        """Test that plot_temperature_data executes without error."""
        filename = "temperature.txt"
        with open(filename, "w") as f:
            f.write("1 20\n2 21\n3 19\n4 23\n5 22")
        try:
            plot_temperature_data(filename)
            success = True
        except Exception:
            success = False
        self.assertTrue(success, "plot_temperature_data failed to execute correctly")

    def test_plot_population_data(self):
        """Test that plot_population_data executes without error."""
        filename = "population.csv"
        with open(filename, "w") as f:
            f.write("Year,Population\n2000,500\n2005,700\n2010,850\n2015,950\n2020,1200")
        try:
            plot_population_data(filename)
            success = True
        except Exception:
            success = False
        self.assertTrue(success, "plot_population_data failed to execute correctly")

if __name__ == "__main__":
    unittest.main()
