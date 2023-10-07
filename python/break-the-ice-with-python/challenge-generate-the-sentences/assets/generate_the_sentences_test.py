import unittest
from io import StringIO
import sys

sys.path.append("/home/labex/project")
from generate_the_sentences import generate_the_sentences


class TestGenerateSentences(unittest.TestCase):
    def test_generate_sentences(self):
        # Redirect stdout to a buffer
        captured_output = StringIO()
        sys.stdout = captured_output

        # Call the function to generate sentences
        generate_the_sentences()

        # Get the printed output from the buffer
        output = captured_output.getvalue().strip()

        # Check that the output is a valid list of sentences
        try:
            sentences = output.split("\n")
            for sentence in sentences:
                words = sentence.split()
                self.assertIn(words[0], ["I", "You"])
                self.assertIn(words[1], ["Play", "Love"])
                self.assertIn(words[2], ["Hockey", "Football"])
        except (ValueError, TypeError):
            self.fail("Output is not a valid list of sentences")


if __name__ == "__main__":
    unittest.main()
