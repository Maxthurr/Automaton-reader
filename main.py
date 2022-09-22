# ROBERT MAXIME, MECE NICOLAS, DEFONTAINE Emilien - BIG W GROUP
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


def automatonCreator(filePath: str) -> dict:
    """ 
    Creates an automaton based on a text file

    Args:
        fileLocation (str): self explanatory

    Returns:
        createdAutomaton (dict): the created automaton
    """

    with open(filePath) as file:
        lines = file.readlines()
        finalStates = lines[0]
        del lines[0] # The first line (containing the final states) if not needed anymore
        
        # Create all the keys and empty lists needed (example: {0: {'a': []}})
        createdAutomaton = {
            int(line.split()[0]): {data.split()[1]: [] for data in lines if line.split()[0] == data[0]} for line in lines
            }
        
        for line in lines:
            data = line.split()
            # Filling the automaton
            createdAutomaton[int(data[0])][data[1]].append(int(data[2]))

        createdAutomaton["finalStates"] = [int(state) for state in finalStates.split()]
        return createdAutomaton

# NDA stands for Non-Deterministic Automaton
simpleNDA = automatonCreator("automaton.txt")
complexNDA = automatonCreator("automaton2.txt")

def pathsRetriever(letter: str, automaton: dict, statesList: list) -> list:
    """ 
    Generates the list of all the possible paths

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
        for state in automaton[statesList[i][-1]][letter]:
            paths.append(statesList[i] + [state])
    return paths


def checkWord(word: str, automaton: dict ) -> bool:
    """
    Check if word is a valid word for the given automaton

    Args:
        word (str): word to verify
        automaton (dict): self explanatory

    Returns:
        bool: True --> The word is valid; False --> The word is not valid
    """

    # if word is an empty string
    if word == '' or type(word) is not str:
        return False

    # The first step of the path is always 0
    possibleStates = [[0]]
    for letter in word:
        print(possibleStates)
        possibleStates = pathsRetriever(letter, automaton, possibleStates)

    print(possibleStates)
    for path in possibleStates:
        # if at least one of the paths leads to one of the final states
        if path[-1] in automaton["finalStates"]:
            return True
    return False


# Simple automaton tests
print("Simple automaton with valid word: ", checkWord("abbadcd", simpleNDA)) # -> True
print("Simple automaton with non valid word: ", checkWord("ac", simpleNDA)) # -> False
print("Simple automaton with non valid letters", checkWord("f", simpleNDA), "\n") # -> False

# Complex automaton tests
print("Complex automaton with valid word: ", checkWord("cdccdakwc", complexNDA)) # -> True
print("Complex automaton with non valid word: ", checkWord("cdc", complexNDA)) # -> False
print("Complex automaton with non valid letter", checkWord('q', complexNDA), "\n") # -> False

# Test for empty string and wrong type for word (not depending on Automaton)
print("Test with empty string: ", checkWord('', simpleNDA)) # -> False
print("Test with integer instead of string for the word", checkWord(4, simpleNDA)) # -> False