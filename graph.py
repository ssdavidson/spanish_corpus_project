import pickle
from matplotlib import pyplot
import nltk

student_train_list = pickle.load(open("student_train.set", "rb"))

x = list()
y = list()

for item in student_train_list:
    types = len(set(nltk.word_tokenize(item.essay)))
    x.append(types)
    y.append(item.placement_raw)

pyplot.plot(x, y, 'g^')
pyplot.show()
