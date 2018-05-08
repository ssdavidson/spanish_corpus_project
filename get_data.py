import csv, io
from collections import defaultdict

L1 = defaultdict(int)
L1_students = list()
students = defaultdict()

with io.open('CORPUS_050718.csv', encoding = 'utf-8') as wb:
  csvreader = csv.reader(wb)
  for row in csvreader:
    SID = row[2]
    if SID not in students:
      students[SID] = []
    if (row[16] != '' and row[16] != "S18_Famous"):
      students[SID].append("S18")
    if (row[30] != '' and row[30] != "W18_Famous") or (row[31] != '' and row[31] != "W18_Vacation"):
      students[SID].append("W18")
    if (row[46] != '' and row[46] != "F17_Famous") or (row[47] != '' and row[47] != "F17_Vacation"):
      students[SID].append("F17")
    if (row[60] != '' and row[60] != "S17_Famous") or (row[61] != '' and row[61] != "S17_Vacation"):
      students[SID].append("S17")
    if (row[76] != '' and row[76] != "SU17_Famous") or (row[77] != '' and row[77] != "SU17_Vacation"):
      students[SID].append("SU17")

    if row[7] != '' and row[7] != 'S18_lang1':
      if SID not in L1_students:
          L1_students.append(SID)
          L1[row[7]] += 1
    if row[21] != '' and row[21] != 'W18_lang1':
      if SID not in L1_students:
          L1_students.append(SID)
          L1[row[21]] += 1
    if row[37] != '' and row[37] != 'F17_lang1':
      if SID not in L1_students:
          L1_students.append(SID)
          L1[row[37]] += 1
    if row[51] != '' and row[51] != 'S17_lang1':
      if SID not in L1_students:
          L1_students.append(SID)
          L1[row[51]] += 1
    if row[67] != '' and row[67] != 'SU17_Lang1':
      if SID not in L1_students:
          L1_students.append(SID)
          L1[row[67]] += 1

zero = 0
one = 0
two = 0
three = 0
four = 0
fourplus = 0

for k,v in students.items():
  if len(students[k]) == 0:
    zero += 1
  elif len(students[k]) == 1:
    one += 1
  elif len(students[k]) == 2:
    two += 1
  elif len(students[k]) == 3:
    three += 1
  elif len(students[k]) == 4:
    four += 1
  else:
    fourplus += 1

print("total students: " + str(len(students)))
print("students with no essays: " + str(zero))
print("students with essays in 1 quarter: " + str(one))
print("students with essays in 2 quarters: " + str(two))
print("students with essays in 3 quarters: " + str(three))
print("students with essays in 4 quarters: " + str(four))
print("students with essays in 5+ quarters: " + str(fourplus))
print(L1)
