import nltk
import re
nltk.download('punkt')

class SentenceSegmentation():
    def naive(self, text):
        """
		Sentence Segmentation using a Naive Approach

		Parameters
		----------
		arg1 : str
			A string (a bunch of sentences)

		Returns
		-------
		list
			A list of strings where each string is a single sentence
		"""
        segmentedText = None
        # Fill in code here
        #segmentedText = text.split(".")
        segmentedText = re.split('\.|!|\?', text)
        segmentedText = segmentedText[0:-1]
        #segmentedText = [item + '.' for item in segmentedText]
        return segmentedText

    def punkt(self, text):
        """
		Sentence Segmentation using the Punkt Tokenizer

		Parameters
		----------
		arg1 : str
			A string (a bunch of sentences)

		Returns
		-------
		list
			A list of strings where each strin is a single sentence
		"""
        segmentedText = None
        # Fill in code here
        # Loading PunktSentenceTokenizer using English pickle file
        tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
        segmentedText = tokenizer.tokenize(text)
        return segmentedText


# testing
# sentenceseg = SentenceSegmentation()
# output = sentenceseg.naive("A list of strings where! each strin. is a single sentence? each strin is a single sentence.")
# print(output)
# output = sentenceseg.punkt("A list of strings where! each strin. is a single sentence? each strin is a single sentence.")
# print(output)
