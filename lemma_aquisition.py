import pickle

#load data from file
student_list = pickle.load(open("student_all.set", "rb"))

result1, result2, result3, result4 = list(), list(), list(), list()
count1, count2, count3, count4 = 0, 0, 0, 0

for student in student_list:
    if student.number_composition == 1:
        if student.placement_percentile <= 25:
            for tup in student.tagged_words:
                result1.append(tup[1])
            count1 += 1
        elif student.placement_percentile > 25 and student.placement_percentile <= 50:
            for tup in student.tagged_words:
                result2.append(tup[1])
            count2 += 1
        elif student.placement_percentile > 50 and student.placement_percentile <= 75:
            for tup in student.tagged_words:
                result3.append(tup[1])
            count3 +=1
        else:
            for tup in student.tagged_words:
                result4.append(tup[1])
            count4 +=1

print("Number of students in each placement score quartile")
print(count1, count2, count3, count4)
print()

q1_set = set([x for x in result1 if result1.count(x) >= 2])
q2_set = set([x for x in result2 if result2.count(x) >= 2])
q3_set = set([x for x in result3 if result3.count(x) >= 2])
q4_set = set([x for x in result4 if result4.count(x) >= 2])

q2_new = [x for x in q2_set if x not in q1_set]
q3_new = [x for x in q3_set if x not in q1_set and x not in q2_new]
q4_new = [x for x in q4_set if x not in q1_set and x not in q2_new and x not in q3_new]

print("Number of new lemmas acquired by quartile: ")
print("Quartile 1: ", len(q1_set))
print("Quartile 2: ", len(q2_new))
print("Quartile 3: ", len(q3_new))
print("Quartile 4: ", len(q4_new))
