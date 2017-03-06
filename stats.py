import pickle
from scipy import stats
import numpy

#load saved student training data from file
student_train_list = pickle.load(open("student_train.set", "rb"))

#empty list to store data
types_list = list()

#save each student's placement score to list
for student in student_train_list:
    types_list.append(student.types)

#calculate the mean using numpy
types_mean = numpy.mean(types_list)
#calculate the median using numpy
types_median = numpy.median(types_list)
#calculate the std_dev using numpy
types_stdev = numpy.std(types_list)

print('Types used - mean: ', types_mean)
print('Types used - median: ', types_median)
print('Types used - std dev: ', types_stdev)
