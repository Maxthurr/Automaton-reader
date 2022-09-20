# --- Atomaton Data Structure --- #
# first set of keys: states value: dictionary of all letters associated with this state
# values of letters: list of all states associated with this letter

# --- Example with the automaton of the file "automaton.txt" --- #
automaton = {
    0: {
        'a': [1, 2],
        'b': [1]
    },
    1: {
        'b': [1, 3, 0]
    },
    2: {
        'd': [3]
    },
    3: {
        'c': [2]
    },
    'finalStates': [2, 3]
}


def automatonCreator(fileLocation: str) -> dict:
    """ Creates an automaton based on a text file

    Args:
        fileLocation (str): self explanatory

    Returns:
        createdAutomaton (dict): the created automaton
    """

    with open(fileLocation) as f:
        lines = f.readlines()
        finalStates = lines[0]
        # The first line (containing the final states) if not needed anymore
        del lines[0]
        # Create all the keys and empty lists needed (example: {0: {'a': []}})
        createdAutomaton = {int(line.split()[0]): {lineA.split()[1]: [] for lineA in lines if line.split()[0] == lineA[0]} for line in lines}
        for line in lines:
            data = line.split()
            #! Je sais pas trop comment expliquer celle la
            createdAutomaton[int(data[0])][data[1]].append(int(data[2]))

        createdAutomaton["finalStates"] = [int(elem) for elem in finalStates.split()]
        return createdAutomaton
            
simpleNDA = automatonCreator("automaton.txt")
complexNDA = automatonCreator("automaton2.txt")

def checkWord(word: str, automaton: dict ) -> bool:
    """ Check if word is a valid word for the given automaton

    Args:
        word (str): word to verify
        automaton (dict): self explanatory

    Returns:
        bool: True --> The word is valid; False --> The word is not valid
    """

    # if word is an empty string
    if word == '' or type(word) is not str:
        return False
    # The first path is always just the state 0
    possibleStates = [[0]]
    for letter in word:
        possibleStates = checkPaths(letter, automaton, possibleStates)

    for path in possibleStates:
        # if at least one of the paths leads to one of the final states
        if path[-1] in automaton["finalStates"]:
            return True
    return False


def checkPaths(letter: str, automaton: dict, statesList: list) -> list:
    """ Generates the list of all the possible paths

    Args:
        letter (str): letter 
        automaton (dict): self explanatory
        statesList (list): the current state of the automaton

    Returns:
        paths (list): list of all possible paths
    """

    paths = []
    for i in range(len(statesList)):
        try:
            automaton[statesList[i][-1]][letter]
        except KeyError:
            continue
        else:            
            for state in automaton[statesList[i][-1]][letter]:
                paths.append(statesList[i] + [state])
    return paths

# Simple automaton tests
print("Simple automaton with valid word: ", checkWord("abbadcd", simpleNDA), end="\n") # -> True
print("Simple automaton with non valid word: ", checkWord("ad", simpleNDA), end="\n") # -> False
print("Simple automaton with non valid letters", checkWord("f", simpleNDA), end="\n") # -> False

# Complex automaton tests
print("Complex automaton with valid word: ", checkWord("cdcdakwc", complexNDA), end="\n") # -> True
print("Complex automaton with non word: ", checkWord("cdc", complexNDA), end="\n") # -> False
print("Complex automaton with non valid letter", checkWord('q', complexNDA), end="\n") # -> False

# Test for empty string and wrong type for word (not depending on Automaton)
print("Test with empty string: ", checkWord('', simpleNDA), end="\n") # -> False
print("Test with integer instead of string for the word", checkWord(4, simpleNDA), end="\n") # -> False
