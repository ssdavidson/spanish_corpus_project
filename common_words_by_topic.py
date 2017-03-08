import pickle
import nltk

#load data from file
student_list = pickle.load(open("student_all.set", "rb"))

def analyze_topic(topic_id, topic_id2=0, topic_id3=0, topic_id4=0):
    corpus = ''
    students_result = list()

    for student in student_list:
        if student.number_composition == topic_id or student.number_composition == topic_id2 or student.number_composition == topic_id3 or student.number_composition == topic_id4:
            corpus += (student.essay + ' ')
            students_result.append(student)

    words = nltk.word_tokenize(corpus)
    fd = nltk.FreqDist(words)
    num_words = len(words)
    fd_50 = fd.most_common(50)
    count_list = [0] * 50
    num_students = len(students_result)

    for student in students_result:
        words = nltk.word_tokenize(student.essay)
        for i in range(50):
            if fd_50[i][0] in words:
                count_list[i] += 1

    print("Word frequencies for topic", topic_id)
    print('{:<10}'.format("word"), '{:<10}'.format("frequency"), "percent students")
    for i in range(50):
        print('{:<11}'.format(str(fd_50[i][0])), '{:<10}'.format(str("%.5f" % (fd_50[i][1]/num_words))), "%.5f" % (count_list[i]/num_students))
    print()

analyze_topic(1, 2, 4, 5)
analyze_topic(1)
analyze_topic(2)
analyze_topic(4)
analyze_topic(5)
