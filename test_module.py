import unittest
import sea_level_predictor
import matplotlib.pyplot as plt

class SeaLevelTestCase(unittest.TestCase):
    def setUp(self):
        self.ax = sea_level_predictor.draw_plot()

    def test_plot_lines(self):
        # Check number of lines plotted (should be 2 best-fit lines)
        actual = len(self.ax.lines)
        expected = 2
        self.assertEqual(actual, expected, f"Expected 2 lines to be plotted, got {actual}")

    def test_plot_labels(self):
        actual_title = self.ax.get_title()
        expected_title = "Rise in Sea Level"
        self.assertEqual(actual_title, expected_title, f"Expected title to be '{expected_title}', got '{actual_title}'")
        
        actual_xlabel = self.ax.get_xlabel()
        expected_xlabel = "Year"
        self.assertEqual(actual_xlabel, expected_xlabel, f"Expected xlabel to be '{expected_xlabel}', got '{actual_xlabel}'")
        
        actual_ylabel = self.ax.get_ylabel()
        expected_ylabel = "Sea Level (inches)"
        self.assertEqual(actual_ylabel, expected_ylabel, f"Expected ylabel to be '{expected_ylabel}', got '{actual_ylabel}'")

if __name__ == "__main__":
    unittest.main()