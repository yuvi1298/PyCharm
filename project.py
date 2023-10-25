import random
from time import sleep

mainChar = input("Main Character:")
rivalName = input("Rival's Name")
activity = input("daily Activity (e.g. watching T.V):")
posAdj = input("positive adjective(e.g. funny,happy):")
negAdj = input("negative adjective (e.g. Careless,Dishonest) :")

Sentence = [
    "Yesterday, while browsing chekTolearn and ",'activity', ' , ' ,'mainChar','noticed that','rivalName',
    'posted a new','word1','about','word2','He','word','it and challenged him','word3','battle.Then he posted his own',
    'posAdj',' ','word1','but','rivalName','retalian','negadj',' ','word1','about','word2','.'
]
word1 = ['questions','code','comment']
word2 = ['penguins','programmer jokes','text generation','another amazing fireworks','finding your partener']
word3 = ['c','c++','python','javascript','java','code']
word4 = ['liked','disliked','reported','deleted']

for item in Sentence:
    if item == "activity" : Sentence[Sentence.index(item)] = activity
    elif item == "mainChar" : Sentence[Sentence.index(item)] = mainChar
    elif item == "rivalName" : Sentence[Sentence.index(item)] = rivalName
    elif item == "posAdj" : Sentence[Sentence.index(item)] = posAdj
    elif item == "negAdj" : Sentence[Sentence.index(item)] = negAdj

    elif item == "word1" : Sentence[Sentence.index(item)] = random.choice(word1)
    elif item == "word2 " : Sentence[Sentence.index(item)] = random.choice(word2)
    elif item == "word2 ": Sentence[Sentence.index(item)] = random.choice(word2)

    else:continue

story=" ".join(item for item in Sentence )
print("\n story is generating\n")
sleep(1)
print (story)


