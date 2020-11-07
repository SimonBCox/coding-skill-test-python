# Import modules #
import unittest
from text_processing_lib.word_frequency import WordFrequencyAnalyzer


# Unit tests #
class WordFrequencyAnalyzerTests(unittest.TestCase):
    def test_frequencies(self):
        """
        A test to check if the calculate_frequencies method returns the same list when using separation characters and
        random non alphabetical characters
        """

        # set test input
        test_text_1 = 'The sun shines over the lake'
        test_text_2 = 'The sun-shines @over & the lake'

        # call method
        frequencies_1 = WordFrequencyAnalyzer.calculate_frequencies(text=test_text_1)
        frequencies_2 = WordFrequencyAnalyzer.calculate_frequencies(text=test_text_2)

        # unittest
        self.assertEqual(str(frequencies_1), str(frequencies_2))

    def test_highest_frequency_single(self):
        """
        A test to check if the calculate_highest_frequency method is case insensitive and returns the correct highest
        frequency
        """

        # set test input
        test_text = 'The sun shines over the lake'

        # call method
        highest_frequency_word = WordFrequencyAnalyzer.calculate_highest_frequency(text=test_text)

        # unittest
        self.assertEqual(highest_frequency_word, 2)

    def test_highest_frequency_multiple(self):
        """
        A test to check if the calculate_highest_frequency method returns the correct highest frequencies when multiple
        words have the same frequency
        """

        # set test input
        test_text = 'The sun shines over the lake. It is a nice day with lots of sun shine. The sun shined all day'

        # call method
        highest_frequency_word = WordFrequencyAnalyzer.calculate_highest_frequency(text=test_text)

        # unittest, should return 3 since both [('the', 3), ('sun', 3)]
        self.assertEqual(highest_frequency_word, 3)

    def test_frequency_for_word(self):
        """
        A test to check if the calculate_frequency_for_word method returns the correct frequency
        """

        # set test input
        test_text = 'The sun shines over the lake. It is a nice day with lots of sun shine.'
        test_word = 'sun'

        # call method
        highest_frequency_word = WordFrequencyAnalyzer.calculate_frequency_for_word(text=test_text, word=test_word)

        # unittest
        self.assertEqual(highest_frequency_word, 2)

    def test_most_frequent_n_words(self):
        """
        A test to check if the calculate_most_frequent_n_words method returns the correct words and corresponding
        frequencies, and that the words are sorted primarily on frequency and secondarily on alphabet
        """

        # set test input
        test_text = 'The sun shines over the lake'
        test_n = 3

        # call method
        most_frequent_words = WordFrequencyAnalyzer.calculate_most_frequent_n_words(text=test_text, n=test_n)

        # unittest
        self.assertEqual(str(most_frequent_words),
                         "[WordFrequency ('the', 2), WordFrequency ('lake', 1), WordFrequency ('over', 1)]")


# Test harness #
if __name__ == '__main__':
    unittest.main()
