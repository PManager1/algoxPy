
#Question:  Can you gnereate the docuemnt using those chars ?  Capital A is different than a.
# characters = "Bste!hetsi ogEAxpelrt x ";
# document = "AlgoExpert is the Best!";


#it works, dont be confused. All we are doing is
# we check that each char in Document is greater than in the Charlist
def generateDocument(characters, document):
    alreadyCounted = set()

    for char in document:
        if char in alreadyCounted:
           continue

        FreqofCharInDocument = countCharacterFrequency(char, document)
        print("documentFreq For char=", char, "=",  FreqofCharInDocument)
        FreqofCharInCharList  = countCharacterFrequency(char, characters)
        print("FreqofCharInCharList= for char=", char, "=",  FreqofCharInCharList)

        if FreqofCharInDocument > FreqofCharInCharList:
            print("calling 22 return False")
            return False

        print("set value =", alreadyCounted)
        alreadyCounted.add(char)
    print("calling 22 return True")
    return True


def countCharacterFrequency(character, targetString):
    frequencey = 0;
    for ch in targetString:
        if ch == character:
            frequencey +=1;
    # print("frequencey of=", ch, "equals", frequencey)
    return frequencey


characters = "Bste!hetsi ogEAxpelrt x ";
document = "AlgoExpert is the Best!";
generateDocument(characters , document)





















'''
def generateDocument(characters, document):
    for character in document:
        documentFreq = countCharacterFrequency(character, document)
        chararctersFreq = countCharacterFrequency(character, characters)
        if documentFreq > chararctersFreq:
            return False
    return True

#returns the frequence of the character in this target.

def countCharacterFrequency(character, targetString):
    frequencey = 0;
    for ch in targetString:
        if ch == character:
            frequencey +=1;
    print("frequencey of=", ch, "equals", frequencey)
    return frequencey

*/
characters = "Bste!hetsi ogEAxpelrt x ";
document = "AlgoExpert is the Best!";
generateDocument(characters , document)
'''







