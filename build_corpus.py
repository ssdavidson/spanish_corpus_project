# This is an example of building a corpus based on conditions applied to
# student data.  In this case, we are creating a single string of all essays
# for student's in the top quartile who used more than 300 types in their essay.

import pickle
import nltk

#load data from file
student_train_list = pickle.load(open("student_train.set", "rb"))

#initialize empty string to hold result
result_string = ''

# iterate through student data.  If data meets contitions, add essay
# to the result string.
for student in student_train_list:
    if student.placement_percentile > 75 and student.types > 300:
        result_string += (student.essay + ' ')

#print the resulting string.  To save to file, use '>' in cmd lin to redirect
print(result_string)
