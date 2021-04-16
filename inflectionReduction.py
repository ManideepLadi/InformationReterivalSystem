from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer


class InflectionReduction:

	def reduce(self, text):
		"""
		Stemming/Lemmatization

		Parameters
		----------
		arg1 : list
			A list of lists where each sub-list a sequence of tokens
			representing a sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of
			stemmed/lemmatized tokens representing a sentence
		"""

		reducedText = list()

		#Fill in code here
		# porter = PorterStemmer()
		# for ls in text:
		# 	sentence_list=list()
		# 	for word in ls:
		# 		sentence_list.append(porter.stem(word))
		# 	reducedText.append(sentence_list)

		lemmatizer = WordNetLemmatizer()
		for ls in text:
			sentence_list=list()
			for word in ls:
				sentence_list.append(lemmatizer.lemmatize(word))
			reducedText.append(sentence_list)
		
		return reducedText


#Inflection Reduction test
# stemming=InflectionReduction()
# output=stemming.reduce([['Good', 'muffins', 'cost', '$3.88\\nin', 'New', 'York.', 'Please', 'buy', 'me\\ntwo', 'of', 'them.\\nThanks']
# ,['Good', 'muffins', 'cost', '$3.88\\nin', 'New', 'York.', 'Please', 'buy', 'me\\ntwo', 'of', 'them.\\nThanks']])
# print(output)