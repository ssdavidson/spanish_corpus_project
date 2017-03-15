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
    fd_50 = fd.most_common(50)
    return fd_50

mc1 = [tup[0] for tup in most_common(result1)]
mc2 = [tup[0] for tup in most_common(result2)]
mc3 = [tup[0] for tup in most_common(result3)]
mc4 = [tup[0] for tup in most_common(result4)]

shared_words = list()

for word in mc1:
    if (word in mc2) and (word in mc3) and (word in mc4):
        shared_words.append(word)

print("Tokens shared by all quartiles")
print(shared_words, "\n")

def frequencies(result):
    words = nltk.word_tokenize(result)
    fd = nltk.FreqDist(words)
    for word in shared_words:
        freq = fd.freq(word)
        print('{:<10}'.format(word), "%.7f" % freq)

print("Token frequencies for 1st quartile students")
frequencies(result1)
print()
print("Token frequencies for 2nd quartile students")
frequencies(result2)
print()
print("Token frequencies for 3rd quartile students")
frequencies(result3)
print()
print("Token frequencies for 4th quartile students")
frequencies(result4)
