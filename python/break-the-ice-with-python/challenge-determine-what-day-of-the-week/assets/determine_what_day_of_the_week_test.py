import unittest
import sys
sys.path.append("/home/labex/project")
from io import StringIO
from determine_what_day_of_the_week import determine_what_day_of_the_week

class TestDetermineWhatDayOfTheWeek(unittest.TestCase):
    def test_determine_what_day_of_the_week(self):
        # Set up the input data
        input_data = "08 05 2015\n"
        sys.stdin = StringIO(input_data)

        # Call the function to determine the day of the week
        captured_output = StringIO()
        sys.stdout = captured_output
        determine_what_day_of_the_week()

        # Get the printed output from the buffer
        output = captured_output.getvalue().strip()

        # Check that the output is correct
        expected_output = "WEDNESDAY"
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()
