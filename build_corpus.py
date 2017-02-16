#This is an example of how the data structure allows you to write conditional statements
#to filter data.  In this case, building a corpus from student essay only if they scored
#over 40 on placement and use more than 300 types in their essay.

import pickle
import nltk

student_train_list = pickle.load(open("student_train.set", "rb"))

result_string = ''

for student in student_train_list:
    if student.placement_raw > 40 and len(set(nltk.word_tokenize(student.essay))) > 300:
        result_string += (student.essay + ' ')
        
print(result_string)
