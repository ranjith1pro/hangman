from hangman import is_word_guessed, get_guessed_word
import unittest

class TestHangman(unittest.TestCase):
	def test_is_word_guessed(self):
		self.assertTrue(is_word_guessed('ranjith',['r','i','k','l','t','h','j']))
	def test_get_guessed_word(self):
		
		self.assertTrue(get_guessed_word('ranjith',['r','k','l','t','h','n','a','i','j']))

if __name__ == '__main__':
	unittest.main()


