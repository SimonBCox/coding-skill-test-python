# Import modules #
import unittest
from text_processing_lib.word_frequency import WordFrequency


# Unit tests #
class WordFrequencyTests(unittest.TestCase):
    def test_type(self):
        """
        Two tests to check if the WordFrequency class stores the input word as a string and the input frequency as
        an integer
        """

        # set test input
        test_word = "test"
        test_frequency = 10

        # call method
        word = WordFrequency(word=test_word, frequency=test_frequency)

        # unittest
        self.assertIsInstance(word.word, str)
        self.assertIsInstance(word.frequency, int)

    def test_representation(self):
        """
        A test to check if the WordFrequency class is represented correctly
        """

        # set test input
        test_word = 'we'
        test_frequency = 10

        # call method
        word = WordFrequency(word=test_word, frequency=test_frequency)

        self.assertEqual(str(word), "WordFrequency ('we', 10)")


# Test harness #
if __name__ == '__main__':
    unittest.main()
