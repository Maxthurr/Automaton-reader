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


def automateCreator(fileLocation: str) -> dict:
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
            
AND = automateCreator("automate2.txt")

def checkWord(word: str, automate: dict ) -> bool:
    if word == '':
        return False
    statesToCheck = [[0]]
    for letter in word:
        statesToCheck = checkPaths(letter, automate, statesToCheck)
    for path in statesToCheck:
        if path[-1] in automate['finalStates']:
            return True
    return False


def checkPaths(letter: str, automate: dict, statesList: list) -> list:
    print(statesList)
    toReturn = []
    for i in range(len(statesList)):
        print(toReturn)
        print(letter, statesList[i][-1])
        try:
            automate[statesList[i][-1]][letter]
        except KeyError:
            continue
        else:            
            for elem in automate[statesList[i][-1]][letter]:
                toReturn.append(statesList[i] + [elem])
                print(toReturn)
    return toReturn

print(checkWord('cdlyzyzyzyzyzyz', AND))