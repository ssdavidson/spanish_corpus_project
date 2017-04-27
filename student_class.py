#This class definition sets a data member for a student object for
#each field in our Excel spreadsheet.  Whenever possible, I tried to
#convert strings into useful data types, such as int and float for
#numbers, and booleans for columns which had binary options.

class Student:
    'Class to contain each student\'s data'

    def __init__(self):
        self.sex = ''
        self.age = 0
        self.degree = ''
        self.native_language = ''
        self.stay_spanish_country = False
        self.age_started_spanish = 0.0
        self.years_studying_spanish = 0.0
        self.other_languages = False
        self.placement_raw = 0
        self.placement_percent = 0.0
        self.placement_percentile = 0.0
        self.tokens = 0
        self.types = 0
        self.number_composition = 0
        self.essay = ''
        self.data_set = ''
        self.tagged_words = []
