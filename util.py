# Add your import statements here
from numpy import dot
from numpy.linalg import norm


def removeDuplicates(unigramsList):
    return list(dict.fromkeys(unigramsList))


def cosineSimilarityMeasure(QueryVector, documentVector):
    if norm(QueryVector)  != 0:
        return dot(QueryVector, documentVector) / (norm(QueryVector) * norm(documentVector))
    else:
        return 0

# Add any utility functions here
