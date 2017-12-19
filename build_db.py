from pony.orm import *
import sys, io, csv, openpyxl, nltk

db = Database()
db.bind(provider='sqlite', filename='../data/spcorpus.sqlite', create_db=True)

class Essay(db.Entity):
  name = Required(str)
  assigned_id = Required(str)
  student_id = Required(str)
  course = Optional(str)
  secnum = Optional(str)
  instr = Optional(str)
  age = Optional(str)
  sex = Optional(str)
  lang1 = Optional(str)
  lang1other = Optional(str)
  langhome = Optional(str)
  langstudy = Optional(str)
  oralun = Optional(str)
  writun = Optional(str)
  oralex = Optional(str)
  writex = Optional(str)
  abroad = Optional(str)
  essay = Optional(str)
  quarter = Optional(str)

db.generate_mapping(create_tables=True)

fields = []
rows = []

with io.open('../data/corpus_111017.csv', encoding = 'utf-8') as wb:
  csvreader = csv.reader(wb)
  with db_session: 
    for row in csvreader:
      if row[17] != '' and row[17] != 'F17_Famous':
        essay1 = Essay(name=row[0], assigned_id=row[1], student_id=row[2], course=row[3], secnum=row[4], instr=row[5],
          age=row[6], sex=row[7], lang1=row[8], lang1other=row[9], langhome=row[10], langstudy=row[11], 
          oralun=row[12], writun=row[13], oralex=row[14], writex=row[15], abroad=row[16], essay=row[17],
          quarter="F17")

      if row[30] != '' and row[30] != 'S17_Famous':
        essay2 = Essay(name=row[0], assigned_id=row[1], student_id=row[2], course=row[18],
          age=row[19], sex=row[20], lang1=row[21], lang1other=row[22], langhome=row[23], langstudy=row[24],
          oralun=row[25], writun=row[26], oralex=row[27], writex=row[28], abroad=row[29], essay=row[30],
          quarter="S17")

      if row[31] != '' and row[31] != 'S17_Vacation':
        essay3 = Essay(name=row[0], assigned_id=row[1], student_id=row[2], course=row[18], 
          age=row[19], sex=row[20], lang1=row[21], lang1other=row[22], langhome=row[23], langstudy=row[24],
          oralun=row[25], writun=row[26], oralex=row[27], writex=row[28], abroad=row[29], essay=row[31],
          quarter="S17")

      if row[46] != '' and row[46] != 'SU17_Famous':
        essay4 = Essay(name=row[0], assigned_id=row[1], student_id=row[2], course=row[32], secnum=row[33], instr=row[34],
          age=row[35], sex=row[36], lang1=row[37], lang1other=row[38], langhome=row[39], langstudy=row[40],
          oralun=row[41], writun=row[42], oralex=row[43], writex=row[44], abroad=row[45], essay=row[46],
          quarter="SU17")

      if row[47] != '' and row[47] != 'SU17_Vacation':
        essay5 = Essay(name=row[0], assigned_id=row[1], student_id=row[2], course=row[32], secnum=row[33], instr=row[34],
          age=row[35], sex=row[36], lang1=row[37], lang1other=row[38], langhome=row[39], langstudy=row[40],
          oralun=row[41], writun=row[42], oralex=row[43], writex=row[44], abroad=row[45], essay=row[47],
          quarter="SU17")
