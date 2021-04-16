import math

import numpy as np

from util import *


# Add your import statements here


class InformationRetrieval():

    def __init__(self):
        self.index = None
        self.uniqueUnigrams=None
        self.df_list=None
        self.noOfDoc=None
        self.docIDs=None

    def buildIndex(self, docs, docIDs):
        """
        Builds the document index in terms of the document
        IDs and stores it in the 'index' class variable

        Parameters
        ----------
        arg1 : list
            A list of lists of lists where each sub-list is
            a document and each sub-sub-list is a sentence of the document
        arg2 : list
            A list of integers denoting IDs of the documents
        Returns
        -------
        None
        """

        index = None

        # Fill in code here
        # implementing vector space model the index will contain term document matrix with weights as tf*IDF
        # collect all unigrams in all the sentences of documents
        unigrams_list = list()
        print(unigrams_list)
        for i in range(len(docs)):
            for j in range(len(docs[i])):
                for k in range(len(docs[i][j])):
                    unigrams_list.append(docs[i][j][k])

        self.unique_unigrams = removeDuplicates(unigrams_list)
        print(self.unique_unigrams)
        # build term-document matrix
        termDocument_Matrix = np.zeros((len(self.unique_unigrams), len(docIDs)))
        print(termDocument_Matrix.shape)
        for l in range(len(self.unique_unigrams)):
            for i in range(len(docs)):
                count = 0
                for j in range(len(docs[i])):
                    for k in range(len(docs[i][j])):
                        if docs[i][j][k] == self.unique_unigrams[l]:
                            count = count + 1
                termDocument_Matrix[l][i] = count
        print(termDocument_Matrix.shape)
        # calculate df for each term
        df_list = list()
        for i in range(len(self.unique_unigrams)):
            countdocuments = 0
            for j in range(len(docIDs)):
                if termDocument_Matrix[i][j] > 0:
                    countdocuments = countdocuments + 1
            df_list.append(countdocuments)
        print(df_list)
        # calculate IDF for each term
        for i in range(len(self.unique_unigrams)):
            for j in range(len(docIDs)):
                idf = len(docIDs) / df_list[i]
                termDocument_Matrix[i][j] = termDocument_Matrix[i][j] * (math.log10(idf))
        print(termDocument_Matrix.shape)

        # store document matrix with weiths as tf*IDF
        index = termDocument_Matrix
        self.index = index
        self.df_list=df_list
        self.noOfDoc=len(docIDs)
        self.docIDs=docIDs

    def rank(self, queries):
        """
        Rank the documents according to relevance for each query

        Parameters
        ----------
        arg1 : list
            A list of lists of lists where each sub-list is a query and
            each sub-sub-list is a sentence of the query


        Returns
        -------
        list
            A list of lists of integers where the ith sub-list is a list of IDs
            of documents in their predicted order of relevance to the ith query
        """

        doc_IDs_ordered = []

        # Fill in code here
        # for each query we have to calculate cosine similarity
        # Take a query and generate np vector of unigrams and docment vector and find cosine similarity
        queriesVector = np.zeros((len(self.unique_unigrams),len(queries)))
        for l in range(len(self.unique_unigrams)):
            for i in range(len(queries)):
                count = 0
                for j in range(len(queries[i])):
                    for k in range(len(queries[i][j])):
                        if queries[i][j][k] == self.unique_unigrams[l]:
                            count = count + 1
                queriesVector[l][i] = count
        print("queries")
        print(queriesVector)
        for i in range(len(self.unique_unigrams)):
            idf = self.noOfDoc / self.df_list[i]
            for j in range(len(queries)):
                queriesVector[i][j] = queriesVector[i][j] * (math.log10(idf))
        #print(queriesVector)
        cosineSimilarites=np.zeros((len(queries),self.noOfDoc))
        for i in range(len(queries)):
            queryVector=queriesVector[:,i]
            #print(queryVector)
            for j in range(self.noOfDoc):
                cosineSimilarites[i][j]=max(0,cosineSimilarityMeasure(queryVector,self.index[:,j]))

        #print(cosineSimilarites)
        #print(np.sort(cosineSimilarites))
        #print(np.argsort(cosineSimilarites))
        orderedSimilarities=np.argsort(cosineSimilarites)
        for i in range(len(queries)):
            queryOrderlist=list()
            for j in range(self.noOfDoc):
                queryOrderlist.append(self.docIDs[orderedSimilarities[i][self.noOfDoc-1-j]])
            doc_IDs_ordered.append(queryOrderlist)

        print(doc_IDs_ordered[0])

        return doc_IDs_ordered


#Test
# Input = [[["similar", "law", "must", "obey", "construct", "aeroelast", "model", "heat", "high", "speed", "aircraft",
#            "speed"],["problem", "heat", "conduct", "composit", "slab", "solv", "far"]],
#          [["structur", "aeroelast", "problem", "associ", "flight", "high", "speed", "aircraft"]],
#          [["problem", "heat", "conduct", "composit", "slab", "solv", "far"]], ]
# ir = InformationRetrieval()
# ir.buildIndex(Input, [1, 2,3])
# ir.rank(Input)

# python main.py -dataset /Users/ram/Desktop/Manideep/NLP_Assignment1/Input/cranfield/ -out_folder /Users/ram/Desktop/Manideep/NLP_Assignment1/output/ -segmenter punkt -tokenizer ptb

