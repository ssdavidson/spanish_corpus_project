import pickle
import nltk

student_train_list = pickle.load(open("student_train.set", "rb"))

result_string = ''

for student in student_train_list:
    if student.placement_raw > 40 and len(set(nltk.word_tokenize(student.essay))) > 300:
        result_string += (student.essay + ' ')
        
print(result_string)
