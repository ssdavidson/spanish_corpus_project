#Create a basic histogram showing the frequency distribution of
#student placement scores

import pickle
from matplotlib import pyplot

#load saved student training data from file
student_train_list = pickle.load(open("student_train.set", "rb"))

#empty list to store data to be graphed
placement = list()

#save each student's placement score to list
for student in student_train_list:
    placement.append(student.placement_raw)

#create frequency dist (normed = True) histgram with 20 bins    
pyplot.hist(placement, bins = 20, normed = True)

#label graph
pyplot.title("frequency dist of placement scores")
pyplot.xlabel("placement score")
pyplot.ylabel("frequency")
pyplot.show() #display graph
