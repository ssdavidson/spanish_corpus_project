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
    student.filename = sheet.cell(row=i, column=1).value
    student.initials = sheet.cell(row=i, column=2).value
    student.university = sheet.cell(row=i, column=3).value
    student.sex = sheet.cell(row=i, column=4).value
    student.department = sheet.cell(row=i, column=5).value
    if sheet.cell(row=i, column=6).value != ' ' and sheet.cell(row=i, column=6).value != None:
        student.age = int(sheet.cell(row=i, column=6).value)
    student.degree = sheet.cell(row=i, column=7).value
    student.year_of_course = int((sheet.cell(row=i, column=8).value)[0:1])
    student.native_language = sheet.cell(row=i, column=9).value
    student.additional_l1 = sheet.cell(row=i, column=10).value
    if sheet.cell(row=i, column=11).value == 'Yes':
        student.stay_spanish_country = True
    else: student.stay_spanish_country = False
    student.stay_spanish_where = sheet.cell(row=i, column=12).value
    student.stay_spanish_when = sheet.cell(row=i, column=13).value
    student.stay_spanish_how_long = sheet.cell(row=i, column=14).value
    if sheet.cell(row=i, column=15).value != None:
        student.stay_months = float(sheet.cell(row=i, column=15).value)
    student.fathers_native_language = sheet.cell(row=i, column=16).value
    student.mothers_native_language = sheet.cell(row=i, column=17).value
    student.language_spoken_at_home = sheet.cell(row=i, column=18).value
    if sheet.cell(row=i, column=19).value != ' ' and sheet.cell(row=i, column=19).value != None:
        student.age_started_spanish = int(sheet.cell(row=i, column=19).value)
    if sheet.cell(row=i, column=20).value != ' 'and sheet.cell(row=i, column=20).value != None:
        student.years_studying_spanish = int(sheet.cell(row=i, column=20).value)
    student.ability_speaking_spanish = sheet.cell(row=i, column=21).value
    student.ability_understanding_spanish = sheet.cell(row=i, column=22).value
    student.ability_reading_spanish = sheet.cell(row=i, column=23).value
    student.ability_writing_spanish = sheet.cell(row=i, column=24).value
    if sheet.cell(row=i, column=25).value == 'Yes':
        student.other_languages = True
    else: student.other_languages = False
    student.ability_language1 = sheet.cell(row=i, column=26).value
    student.ability_speaking_language1 = sheet.cell(row=i, column=27).value
    student.ability_understanding_language1 = sheet.cell(row=i, column=28).value
    student.ability_reading_language1 = sheet.cell(row=i, column=29).value
    student.ability_writing_language1 = sheet.cell(row=i, column=30).value
    student.ability_language2 = sheet.cell(row=i, column=31).value
    student.ability_speaking_language2 = sheet.cell(row=i, column=32).value
    student.ability_understanding_language2 = sheet.cell(row=i, column=33).value
    student.ability_reading_language2 = sheet.cell(row=i, column=34).value
    student.ability_writing_language2 = sheet.cell(row=i, column=35).value
    student.placement_raw = int(sheet.cell(row=i, column=36).value)
    student.placement_percent = float(sheet.cell(row=i, column=37).value)
    student.title_composition = sheet.cell(row=i, column=38).value
    student.number_composition = int(sheet.cell(row=i, column=39).value)
    if sheet.cell(row=i, column=40).value == 'Yes':
        student.research_for_essay = True
    else: student.research_for_essay = False
    student.hours_research = sheet.cell(row=i, column=41).value
    if sheet.cell(row=i, column=42).value == 'ON':
        student.source_spanish_other = True
    else: student.source_spanish_other = False
    if sheet.cell(row=i, column=43).value == 'ON':
        student.source_spanish_internet = True
    else: student.source_spanish_internet = False
    if sheet.cell(row=i, column=44).value == 'ON':
        student.source_spanish_books = True
    else: student.source_spanish_books = False
    student.source_spanish_other_text = sheet.cell(row=i, column=45).value
    if sheet.cell(row=i, column=46).value != None:
        student.how_long_write = sheet.cell(row=i, column=46).value
    student.where_write_essay = sheet.cell(row=i, column=47).value
    if sheet.cell(row=i, column=48).value == 'Yes':
        student.language_tools = True
    else: student.language_tools = False
    if sheet.cell(row=i, column=49).value == 'ON':
        student.spellchecker = True
    else: student.spellchecker = False
    if sheet.cell(row=i, column=50).value == 'ON':
        student.native_help = True
    else: student.native_help = False
    if sheet.cell(row=i, column=51).value == 'ON':
        student.bilingual_dictionary = True
    else: student.bilingual_dictionary = False
    if sheet.cell(row=i, column=52).value == 'ON':
        student.thesaurus = True
    else: student.thesaurus = False
    if sheet.cell(row=i, column=53).value == 'ON':
        student.grammar = True
    else: student.grammar = False
    student.other_resources = sheet.cell(row=i, column=54).value
    student.essay = sheet.cell(row=i, column=55).value

    if i==1 or i%15 == 0:
        student_test_list.append(student)
    else: student_train_list.append(student)

print(len(student_test_list))
print(len(student_train_list))

pickle.dump(student_test_list, open('student_test.set', 'wb'))
pickle.dump(student_train_list, open('student_train.set', 'wb'))
