#This is an example of how you can use the data to graph using pylot
#in this case, graphing tokens used against placement score

import pickle
from matplotlib import pyplot
import nltk

student_train_list = pickle.load(open("student_train.set", "rb"))

results_list = list()

for item in student_train_list:
    essay_tokens = len(set(nltk.word_tokenize(item.essay)))
    tup = (essay_tokens, item.placement_raw)
    results_list.append(tup)

pyplot.plot(*zip(*results_list), 'g^')
pyplot.show()
