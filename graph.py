# This is an example of using the student data to create graphs
# In this case, we are graphing the number of types used against
# the student's placement score.

import pickle #used to load data
from matplotlib import pyplot #used for graphing

#load saved student training data from file
student_train_list = pickle.load(open("student_train.set", "rb"))

#initialize empty lists to hold date for your x and y values
x = list()
y = list()

# iterate through student trainging data.  For each student, add the student's
# data types value to the x list, and placement score to the y list.
for student in student_train_list:
    x.append(student.types)
    y.append(student.placement_raw)

# build graph
pyplot.title("number of types vs. placement score")
pyplot.xlabel("number of types")
pyplot.ylabel("placement score")
pyplot.plot(x, y, 'g^') #this is a scatterplat, using green(g) triangles(^)
pyplot.show() #display graph
