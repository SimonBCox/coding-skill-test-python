# Import modules #
import re
import warnings


# Class definitions #
class WordFrequency:
    """
    A class containing a word and its frequency of occurrence in a text
    ...

    Attributes
    ----------
    word        (str) : A word in a text
    frequency   (int) : The frequency of the word occurring in a text

    Methods
    -------
    No methods
    """

    def __init__(self, word: str, frequency: int):
        self.word = word
        self.frequency = frequency

    def __repr__(self):
        return f'WordFrequency (\'{self.word}\', {self.frequency})'


class WordFrequencyAnalyzer:
    """
    A class containing operations to analyse the words and their frequencies of occurrence in a text
    ...

    Attributes
    ----------
    No attributes

    Methods
    -------
    calculate_frequencies(text: str):
        This function calculates the frequency of all unique words in a text

    calculate_highest_frequency(text: str):
        This function calculates which word(s) have the highest frequency in a text

    calculate_frequency_for_word(text: str, word: str):
        This function calculates the frequency of a specific word in a text

    calculate_most_frequent_n_words(text: str, n: int):
        This function calculates the n most frequent words in a text
    """

    def __init__(self):
        pass

    @staticmethod
    def calculate_frequencies(text: str):
        """
        This function calculates the frequency of all unique words in a text

        :param text: a string containing the text to be analyzed
        :return word_frequency_dict: a dictionary containing all unique words as keys and their corresponding frequency
        in the text as values
        """

        # transform text to all lower case and split text on alphanumeric
        text = text.lower()
        words_list = re.split("\W+", text)

        # get unique words and calculate frequency per unique word
        unique_words = set(words_list)
        word_frequencies = [words_list.count(w) for w in unique_words]

        # create WordFrequency for all unique word - frequency pairs
        word_frequency_list = [WordFrequency(word, freq) for word, freq in zip(unique_words, word_frequencies)]

        return word_frequency_list

    @staticmethod
    def calculate_highest_frequency(text: str):
        """
        This function calculates which word(s) have the highest frequency in a text

        :param text: a string containing the text to be analyzed
        :return highest_frequency: an integer describing the highest frequency of (a) word(s) in the text
        """

        # get frequencies for all unique words
        word_frequencies = WordFrequencyAnalyzer.calculate_frequencies(text)

        # get highest frequency
        highest_frequency = max([wordfreq.frequency for wordfreq in word_frequencies])

        return highest_frequency

    @staticmethod
    def calculate_frequency_for_word(text: str, word: str):
        """
        This function calculates the frequency of a specific word in a text

        :param text: a string containing the text to be analyzed
        :param word: a string containing a word for which the frequency must be calculated
        :return word_frequency: an integer describing the frequency of the word in the text
        """

        # get frequencies for all unique words
        word_frequencies = WordFrequencyAnalyzer.calculate_frequencies(text)

        # get frequency of word in text, if word not in text return None and raise warning
        word_frequency = next((wordfreq.frequency for wordfreq in word_frequencies if wordfreq.word == word), None)

        if not word_frequency:
            warnings.warn("The specified word is not in the text")

        return word_frequency

    @staticmethod
    def calculate_most_frequent_n_words(text: str, n: int):
        """
        This function calculates the n most frequent words in a text

        :param text: a string containing the text to be analyzed
        :param n: an integer describing the number of most frequent words to be calculated
        :return word_frequencies_sorted: a list containing word - frequency pairs for the n most frequent words,
        primarily sorted by frequency and secondarily sorted alphabetically
        """

        # get frequencies for all unique words
        word_frequencies = WordFrequencyAnalyzer.calculate_frequencies(text)

        # sort words by frequency and in alphabetical order and get top n words
        word_frequencies_sorted = sorted(word_frequencies, key=lambda x: (-x.frequency, x.word), reverse=False)[:n]

        return word_frequencies_sorted
