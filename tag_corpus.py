# much of this code is the FreeLing project - https://github.com/TALP-UPC/FreeLing/blob/master/APIs/python/

import freeling
import sys
import string
import pickle
from student_class import Student #student class definition

#load data from file
student_train_list = pickle.load(open("student_train.set", "rb"))
student_test_list = pickle.load(open("student_test.set", "rb"))
student_list = pickle.load(open("student_all.set", "rb"))

## -----------------------------------------------
## Do whatever is needed with analyzed sentences
## -----------------------------------------------
def ProcessSentences(ls):
    result_list = list()
    # for each sentence in list
    for s in ls :
        # for each word in sentence
        for w in s :
            if w.get_lemma() not in string.punctuation:
                word_tuple = (w.get_form().lower(), w.get_lemma(), w.get_tag())
                result_list.append(word_tuple)
        # sentence separator
    return result_list


## -----------------------------------------------
## Set desired options for morphological analyzer
## -----------------------------------------------
def my_maco_options(lang,lpath) :

    # create options holder
    opt = freeling.maco_options(lang);

    # Provide files for morphological submodules. Note that it is not
    # necessary to set file for modules that will not be used.
    opt.UserMapFile = "";
    opt.LocutionsFile = lpath + "locucions.dat";
    opt.AffixFile = lpath + "afixos.dat";
    opt.ProbabilityFile = lpath + "probabilitats.dat";
    opt.DictionaryFile = lpath + "dicc.src";
    opt.NPdataFile = lpath + "np.dat";
    opt.PunctuationFile = lpath + "../common/punct.dat";
    return opt;



## ----------------------------------------------
## -------------    MAIN PROGRAM  ---------------
## ----------------------------------------------

# set locale to an UTF8 compatible locale
freeling.util_init_locale("default");

# get requested language from arg1, or English if not provided
lang = "es"
if len(sys.argv)>1 : lang=sys.argv[1]

# get installation path to use from arg2, or use /usr/local if not provided
ipath = "/usr/local/Cellar/freeling/4.0_4";
if len(sys.argv)>2 : ipath=sys.argv[2]

# path to language data
lpath = ipath + "/share/freeling/" + lang + "/"

# create analyzers
tk=freeling.tokenizer(lpath+"tokenizer.dat");
sp=freeling.splitter(lpath+"splitter.dat");

# create the analyzer with the required set of maco_options
morfo=freeling.maco(my_maco_options(lang,lpath));
#  then, (de)activate required modules
morfo.set_active_options (False,  # UserMap
                          True,  # NumbersDetection,
                          True,  # PunctuationDetection,
                          True,  # DatesDetection,
                          True,  # DictionarySearch,
                          True,  # AffixAnalysis,
                          False, # CompoundAnalysis,
                          True,  # RetokContractions,
                          True,  # MultiwordsDetection,
                          True,  # NERecognition,
                          False, # QuantitiesDetection,
                          True); # ProbabilityAssignment

# create tagger
tagger = freeling.hmm_tagger(lpath+"tagger.dat",True,2)

def process_list(student_list):
    for student in student_list:
        # tokenize input line into a list of words
        lw = tk.tokenize(student.essay)
        # split list of words in sentences, return list of sentences
        ls = sp.split(lw)

        # perform morphosyntactic analysis and disambiguation
        ls = morfo.analyze(ls)
        ls = tagger.analyze(ls)

        # do whatever is needed with processed sentences
        student.tagged_words = ProcessSentences(ls)

process_list(student_list)
process_list(student_train_list)
process_list(student_test_list)

#save the data sets to file for futher use
pickle.dump(student_list, open('student_all.set', 'wb'))
pickle.dump(student_test_list, open('student_test.set', 'wb'))
pickle.dump(student_train_list, open('student_train.set', 'wb'))
