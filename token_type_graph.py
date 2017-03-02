# This is another example of using the student data to create graphs
# In this case, we are graphing the number of types used against
# the number of tokens used.

import pickle #used to load data
from matplotlib import pyplot #used for graphing

#load saved student training data from file
student_train_list = pickle.load(open("student_train.set", "rb"))

#initialize empty lists to hold date for your x and y values
x = list()
y = list()

# iterate through student trainging data.  For each student, add the student's
# data tokens value to the x list, and types to the y list.
for student in student_train_list:
    x.append(student.tokens)
    y.append(student.types)

# build graph
pyplot.title("number of types vs. placement score")
pyplot.xlabel("number of tokens")
pyplot.ylabel("number of types")
pyplot.plot(x, y, 'ro') #this is a scatterplat, using green(r) circles(o)
pyplot.show() #display graph
