# --- Structure données automate --- #
automate = {
    0: {
        'a': [1, 2],
        'b': [1]
    },
    1: {
        'b': [1, 3, 0]
    },
    3: {
        'c': [2]
    },
    'finalStates': [2, 3]
}


def automateCreator(fileLocation):
    with open(fileLocation) as f:
        lines = f.readlines()
        finalStates = lines[0]
        del lines[0]
        # Create all the keys and empty lists needed (example: {0: {'a': []}})
        createdAutomate = {int(line.split()[0]): {lineA.split()[1]: [] for lineA in lines if line.split()[0] == lineA[0]} for line in lines}
        for line in lines:
            data = line.split()
            createdAutomate[int(data[0])][data[1]].append(int(data[2]))
        createdAutomate['finalStates'] = [int(elem) for elem in finalStates.split()]
        return createdAutomate
            
AND = automateCreator("automate.txt")

# TODO Wordcheking function + tests
##! Jpense que jme complique la vie mais j'ai commencé par ca meme si c'est pas beau
def checkWord(word, automate):
    statesToCheck = [0]
    goodLetters = 0
    for letter in word:
        print(statesToCheck, letter)
        wrongStates = 0
        for state in statesToCheck  :
            print(letter, state, wrongStates)
            try: 
                automate[state][letter]
            except KeyError:
                wrongStates += 1
                print('error', wrongStates)
                if wrongStates == len(statesToCheck):
                    return False
                continue
            else:
                statesToCheck = automate[state][letter]
                goodLetters += 1
                print(statesToCheck)
            
    print(statesToCheck, automate['finalStates'])
    for state in statesToCheck:
        if state in automate['finalStates'] and goodLetters == len(word):
            return True
    return False

print(checkWord('abb', AND))