import pickle
import nltk

#load data from file
student_list = pickle.load(open("student_all.set", "rb"))

result1, result2, result3, result4 = "", "", "", ""
count1, count2, count3, count4 = 0, 0, 0, 0

print(len(student_list))

for student in student_list:
    if student.number_composition == 1:
        if student.placement_percentile <= 25:
            result1 += (student.essay + ' ')
            count1 += 1
        elif student.placement_percentile > 25 and student.placement_percentile <= 50:
            result2 += (student.essay + ' ')
            count2 += 1
        elif student.placement_percentile > 50 and student.placement_percentile <= 75:
            result3 += (student.essay + ' ')
            count3 +=1
        else:
            result4 += (student.essay + ' ')
            count4 +=1

print("Number of students in each placement score quartile")
print(count1, count2, count3, count4)
print()

def most_common(corpus):
    words = nltk.word_tokenize(corpus)
    fd = nltk.FreqDist(words)
    num_words = len(words)
    fd_50 = fd.most_common(50)
    words = [tup[0] for tup in fd_50]
    return words

print("50 most common words for 1st quartile students")
print(most_common(result1))
print()
print("50 most common words for 2nd quartile students")
print(most_common(result2))
print()
print("50 most common words for 3rd quartile students")
print(most_common(result3))
print()
print("50 most common words for 4th quartile students")
print(most_common(result4))
