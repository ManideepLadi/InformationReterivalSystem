from nltk import TreebankWordTokenizer

from util import *

# Add your import statements here



class Tokenization():

	def naive(self, text):
		"""
		Tokenization using a Naive Approach

		Parameters
		----------
		arg1 : list
			A list of strings where each string is a single sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of tokens
		"""

		tokenizedText = list()

		#Fill in code here
		for ls in text:

			tokenList = ls.split()
			tokenizedText.append(tokenList)

		return tokenizedText



	def pennTreeBank(self, text):
		"""
		Tokenization using the Penn Tree Bank Tokenizer

		Parameters
		----------
		arg1 : list
			A list of strings where each string is a single sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of tokens
		"""
		# tokenList = list()
		# tokenList.append(TreebankWordTokenizer().tokenize(ls))
		# tokenizedText.append(tokenList)
		# tokenizedText = list()

		#Fill in code here
		tokenizedText = list()

		# Fill in code here
		for ls in text:
			tokenList=TreebankWordTokenizer().tokenize(ls)
			tokenizedText.append(tokenList)

		return tokenizedText



#Test
tokenization = Tokenization()
tokenizedText1=tokenization.pennTreeBank(['Up to the 1980s, most: "natural language processing" systems were based on complex sets of hand-written rules.'])
tokenizedText2 = tokenization.naive(['Up to the 1980s, most: "natural language processing" systems were based on complex sets of hand-written rules.'])
print(tokenizedText1)
print(tokenizedText2)
