#This class definition sets a data member for a student object for
#each field in our Excel spreadsheet.  Whenever possible, I tried to
#convert strings into useful data types, such as int and float for
#numbers, and booleans for columns which had binary options.

class Student:
    'Class to contain each student\'s data'

    def __init__(self):
        self.filename = ''
        self.initials = ''
        self.university = ''
        self.sex = ''
        self.department = ''
        self.age = 0
        self.degree = ''
        self.year_of_course = 0
        self.native_language = ''
        self.additional_l1 = ''
        self.stay_spanish_country = False
        self.stay_spanish_where = ''
        self.stay_spanish_when = ''
        self.stay_spanish_how_long = ''
        self.stay_months = 0.0
        self.fathers_native_language = ''
        self.mothers_native_language = ''
        self.language_spoken_at_home = ''
        self.age_started_spanish = 0
        self.years_studying_spanish = 0
        self.ability_speaking_spanish = ''
        self.ability_understanding_spanish = ''
        self.ability_reading_spanish = ''
        self.ability_writing_spanish = ''
        self.other_languages = False
        self.ability_language1 = ''
        self.ability_speaking_language1 = ''
        self.ability_understanding_language1 = ''
        self.ability_reading_language1 = ''
        self.ability_writing_language1 = ''
        self.ability_language2 = ''
        self.ability_speaking_language2 = ''
        self.ability_understanding_language2 = ''
        self.ability_reading_language2 = ''
        self.ability_writing_language2 = ''
        self.placement_raw = 0
        self.placement_percent = 0.0
        self.title_composition = ''
        self.number_composition = 0
        self.research_for_essay = False
        self.hours_research = ''
        self.source_spanish_other = False
        self.source_spanish_internet = False
        self.source_spanish_books = False
        self.source_spanish_other_text = ''
        self.how_long_write = 0.0
        self.where_write_essay = ''
        self.language_tools = False
        self.spellchecker = False
        self.native_help = False
        self.bilingual_dictionary = False
        self.thesaurus = False
        self.grammar = False
        self.other_resources = ''
        self.essay = ''
