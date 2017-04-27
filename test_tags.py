import pickle
import matplotlib.pyplot as plt

student_list = pickle.load(open("student_all.set", "rb"))

personal_pronoun_counts = list()
article_counts = list()
preposition_counts = list()
possessive_counts = list()
placement_percentile_list = list()
placement_raw_list = list()
placement_percent_list = list()

for student in student_list:
    pp_count = 0
    art_count = 0
    prep_count = 0
    poss_count = 0

    placement_percentile_list.append(student.placement_percentile)
    placement_raw_list.append(student.placement_raw)
    placement_percent_list.append(student.placement_percent)

    for words in student.tagged_words:
        if "PP" in words[2][:2]:
            pp_count += 1
        if "DA" in words[2][:2]:
            art_count += 1
        if "SP" in words[2][:2]:
            prep_count += 1
        if "DP" in words[2][:2]:
            poss_count += 1

    personal_pronoun_counts.append(pp_count)
    article_counts.append(art_count)
    preposition_counts.append(prep_count)
    possessive_counts.append(poss_count)

y = placement_percentile_list
x1 = personal_pronoun_counts
x2 = article_counts
x3 = preposition_counts
x4 = possessive_counts

plt.title("number prepositions vs. placement percentile")
plt.xlabel("placement percentile")
plt.ylabel("prepositions used")
plt.plot(y, x4, 'g^')
plt.show()
