import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords


class StopwordRemoval():
    def fromList(self, text):
        """
		Sentence Segmentation using the Punkt Tokenizer

		Parameters
		----------
		arg1 : list
			A list of lists where each sub-list is a sequence of tokens
			representing a sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of tokens
			representing a sentence with stopwords removed
		"""
		# Fill in code here
        stopwordRemovedText = []
        stop_words = set(stopwords.words('english'))
        for i in range(len(text)):
            filtered_sentence = []
            for w in text[i]:
                if w not in stop_words:
                    filtered_sentence.append(w)
            stopwordRemovedText.append(filtered_sentence)

        return stopwordRemovedText


#Testing
# input=[['good', 'muffin', 'cost', '$3.88\\nin', 'new', 'york.', 'pleas', 'buy', 'me\\ntwo', 'of', 'them.\\nthank'], ['good', 'muffin', 'to','him','cost', '$3.88\\nin', 'new', 'york.', 'pleas', 'buy', 'me\\ntwo', 'of', 'them.\\nthank']]
# object = StopwordRemoval()
# output=object.fromList(input)
# print(output)