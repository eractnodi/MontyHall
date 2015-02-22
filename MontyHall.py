from itertools import permutations
from random import randint

#copied this from the interwebs
def remove_duplicates(values):
    output = []
    seen = set()
    for value in values:
        # If value has not been encountered yet,
        # ... add it to both list and set.
        if value not in seen:
            output.append(value)
            seen.add(value)
    return output

possiblePrizesList = ['car', 'goat', 'goat']

iterable = possiblePrizesList

possiblePrizePermutationsList = []

for prizePermutation in permutations(iterable, r=None):
    possiblePrizePermutationsList.append(prizePermutation)

possiblePrizePermutationsList = remove_duplicates(possiblePrizePermutationsList)

noSwitchCount = 0
switchCount = 0

count = 0
while count < 1000:
    currentDoorPermutation = possiblePrizePermutationsList[randint(0,len(possiblePrizePermutationsList)-1)]
    contestantChoosesInt = randint(0,2)
    montyRevealsInt = -1
    while montyRevealsInt == contestantChoosesInt or currentDoorPermutation[montyRevealsInt] == 'car' or montyRevealsInt < 0:
        montyRevealsInt = randint(0,2)
    if contestantChoosesInt == currentDoorPermutation.index('car'):
        noSwitchCount = noSwitchCount+1
    else:
        switchCount = switchCount+1
    count=count+1

print('should not switch times: '+str(noSwitchCount))
print('should have switched times: '+str(switchCount))
    
    


