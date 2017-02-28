#This program uses the Student class to import data from the Excel spreadsheet
#and save the data as a list of Student objects which can then be used
#for further analysis of the data.  Also, divides data into test and training
#sets, and saved data sets to file.

import openpyxl
import pickle
from student_class import Student

wb = openpyxl.load_workbook('Learners_ALL_FINAL.xlsx')

sheet = wb.get_sheet_by_name('Good Data')
student_train_list = list()
student_test_list = list()

row_count = sheet.max_row

for i in range(2, row_count):
    student = Student()
    student.sex = sheet.cell(row=i, column=4).value
    if sheet.cell(row=i, column=6).value != ' ' and sheet.cell(row=i, column=6).value != None:
        student.age = int(sheet.cell(row=i, column=6).value)
    student.degree = sheet.cell(row=i, column=7).value
    student.native_language = sheet.cell(row=i, column=9).value
    if sheet.cell(row=i, column=11).value == 'Yes':
        student.stay_spanish_country = True
    else: student.stay_spanish_country = False
    if sheet.cell(row=i, column=19).value != ' ' and sheet.cell(row=i, column=19).value != None:
        student.age_started_spanish = int(sheet.cell(row=i, column=19).value)
    if sheet.cell(row=i, column=20).value != ' 'and sheet.cell(row=i, column=20).value != None:
        student.years_studying_spanish = int(sheet.cell(row=i, column=20).value)
    if sheet.cell(row=i, column=25).value == 'Yes':
        student.other_languages = True
    else: student.other_languages = False
    student.placement_raw = int(sheet.cell(row=i, column=36).value)
    student.placement_percent = float(sheet.cell(row=i, column=37).value)
    student.number_composition = int(sheet.cell(row=i, column=39).value)
    student.essay = sheet.cell(row=i, column=55).value

    if i==1 or i%15 == 0:
        student_test_list.append(student)
    else: student_train_list.append(student)

print(len(student_test_list))
print(len(student_train_list))

pickle.dump(student_test_list, open('student_test.set', 'wb'))
pickle.dump(student_train_list, open('student_train.set', 'wb'))
