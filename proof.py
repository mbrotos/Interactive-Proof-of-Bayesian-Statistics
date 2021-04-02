import random as rand

def InteractiveProof(switch=True, output=True):
    correct = True
    choices = list(range(0, 3))
    selection = rand.choice(choices)
    prizeLocation = rand.choice(choices)

    try:
        choices.remove(selection)
        choices.remove(prizeLocation)
    except ValueError:
        pass
    notPrizeLocation = rand.choice(choices)

    if output:
        print(f"Your selection: {selection} \nBe advised that" +
            f" location {notPrizeLocation} does not contain the" + 
            f" prize. \nWould you like to switch: {switch}")

    if(switch):
        selection = (set(range(0, 3)) - {notPrizeLocation, selection}).pop()
    
    if (selection == prizeLocation):
        if output:
            print("You are correct!")
        return correct
    if output:
        print("You are incorrect!") 
    return not correct

if __name__ == "__main__":
    iterations = 10000
    correctC = 0
    incorrectC = 0
    print("If you always switch your inital choice: ")
    for i in range(0,iterations):
        if InteractiveProof(output=False):
            correctC += 1
        else:
            incorrectC += 1
    print(f"Correct count: {correctC}")
    print(f"Incorrect count: {incorrectC}")
    print(f"Precent correct: {correctC/iterations}")

    correctC = 0
    incorrectC = 0
    print("\nIf you never switch your inital choice: ")
    for i in range(0,iterations):
        if InteractiveProof(switch = False, output=False):
            correctC += 1
        else:
            incorrectC += 1
    print(f"Correct count: {correctC}")
    print(f"Incorrect count: {incorrectC}")
    print(f"Precent correct: {correctC/iterations}")