import pandas as panda

class DynastyFootballCalculatorWRProspects:



    def __init__(self, name, dominator, breakoutAge, seniorYear, smallBlowupGames,
                 bigBlowupGames, draftCapital, ypr, targetShare, ryptpaOA, volumeTargets, volumeReceptions, volumeYards, years):
        self.name = name
        self.dominator = dominator
        self.breakoutAge = breakoutAge
        self.seniorYear = seniorYear
        self.smallBlowupGames = smallBlowupGames
        self.bigBlowupGames = bigBlowupGames
        self.draftCapital = draftCapital
        self.ypr = ypr
        self.targetShare = targetShare
        self.ryptpaOA = ryptpaOA
        self.volumeTargets = volumeTargets
        self.volumeReceptions = volumeReceptions
        self.volumeYards = volumeYards
        self.years = years

    def penalty_and_bonus(self):
        penalty = 0
        bonus = 0
        if(self.seniorYear == "yes"):
            penalty = .8
        else:
            penalty = 1
        bigBlowup = False
        if(self.draftCapital <= 37):
            if(self.bigBlowupGames > 1):
                bonus = 10
                bigBlowup = True
            if(self.smallBlowupGames > 1 and bigBlowup == False):
                bonus = 5
        elif(self.draftCapital <= 56):
            if (self.bigBlowupGames > 1):
                bonus = 10
                bigBlowup = True
            if (self.smallBlowupGames > 1 and bigBlowup == False):
                bonus = 3
        else:
            if (self.bigBlowupGames > 1):
                bonus = 5
                bigBlowup = True
            if (self.smallBlowupGames > 1 and bigBlowup == False):
                bonus = 1
        if self.years > 4:
            penalty = .6
        return penalty, bonus

    def score(self):
        domination = self.dominator
        dominationScore = self.domination(domination)

        draftCapital = self.draftCapital
        draftCapitalScore = self.draft(draftCapital)

        ypr = self.ypr
        yprScore = self.yprScore(ypr)

        targetShare = self.targetShare
        targetShareScore = self.targetShareScore(targetShare)

        ryptpaOA = self.ryptpaOA
        ryptpaOAScore = self.ryptpaOAScore(ryptpaOA)

        breakoutAge = self.breakoutAge
        breakoutAgeScore = self.breakoutAgeScore(breakoutAge)

        

        totalScore = dominationScore + breakoutAgeScore + yprScore + targetShareScore + ryptpaOAScore + draftCapitalScore
        return totalScore

    def yprScore(self, ypr):
        yprScore = 0.0
        count = 0
        adjustedYPR = ypr * 10
        for x in range(0, int(adjustedYPR), 1):
            if (count < 120):
                yprScore += 0.0
            elif (count < 160):
                yprScore += .1
            elif (count < 200):
                yprScore += .2
            else:
                yprScore += .3
            count += 1
        if (yprScore > 10):
            yprScore = 10

        return yprScore

    def targetShareScore(self, targetShare):
        targetShareScore = 0
        count = 0
        adjustedTargetShare = targetShare * 10
        for x in range(0, int(adjustedTargetShare)):
            if (count < 200):
                targetShareScore += 0
            elif (count < 250):
                targetShareScore += .05
            elif (count < 300):
                targetShareScore += .1
            else:
                targetShareScore += .075
            count += 1

        if(targetShareScore < 0):
            targetShareScore = 0

        if (targetShareScore > 15):
            targetShareScore = 15
        return targetShareScore

    def ryptpaOAScore(self, ryptpaOA):
        ryptpaOAScore = 0.0
        count = 0
        adjustedryptpaOA = ryptpaOA * 100
        for x in range(0, int(adjustedryptpaOA)):
            if (count < 100):
                ryptpaOAScore += 0
            elif (count < 200):
                ryptpaOAScore += .02
            elif (count < 400):
                ryptpaOAScore += .06
            else:
                ryptpaOAScore += .05
            count += 1

        if (ryptpaOAScore > 20):
            ryptpaOAScore = 20

        return ryptpaOAScore

    def draft(self, draftCapital):
        draftCapitalScore = 15
        count = 0

        for x in range(0, int(draftCapital)):
            if (count < 10):
                draftCapitalScore -= 0
            elif (count < 20):
                draftCapitalScore -= .1
            elif (count < 64):
                draftCapitalScore -= .04
            else:
                draftCapitalScore -= .2
            count += 1

        if(draftCapitalScore > 10):
            draftCapitalScore = 10

        if (draftCapitalScore < 0):
            draftCapitalScore = 0

        return draftCapitalScore

    def domination(self, domination):
        dominationScore = 0
        adjustedDomination = domination * 10
        count = 0
        for x in range(150, int(adjustedDomination), 1):
            if (count < 50):
                dominationScore += 0
            elif (count < 100):
                dominationScore += .01
            elif (count < 200):
                dominationScore += .04
            else:
                dominationScore += .02
            count += 1

        if dominationScore > 20:
            dominationScore = 20
        return dominationScore


    def breakoutAgeScore(self, breakoutAge):
        breakoutAgeScore = 5
        count = 0
        adjustedBreakoutAge = breakoutAge * 10
        for x in range(180, int(adjustedBreakoutAge), 1):
            if (count < 5):
                breakoutAgeScore -= 0
            elif (count < 15):
                breakoutAgeScore -= .15
            elif (count < 30):
                breakoutAgeScore -= .2
            else:
                breakoutAgeScore -= .1
            count += 1

        if breakoutAgeScore < 0:
            breakoutAgeScore = 0
        return breakoutAgeScore


def partition(start, end, array, dictMatrix):

    # Initializing pivot's index to start
    pivot_index = start
    pivot = array[pivot_index]

    # This loop runs till start pointer crosses
    # end pointer, and when it does we swap the
    # pivot with element on end pointer
    while start < end:

        # Increment the start pointer till it finds an
        # element greater than  pivot
        while start < len(array) and array[start] >= pivot:
            start += 1

        # Decrement the end pointer till it finds an
        # element less than pivot
        while array[end] < pivot:
            end -= 1

        # If start and end have not crossed each other,
        # swap the numbers on start and end
        if (start < end):
            array[start], array[end] = array[end], array[start]
            dictMatrix[start], dictMatrix[end] = dictMatrix[end], dictMatrix[start]


    # Swap pivot element with element on end pointer.
    # This puts pivot on its correct sorted place.
    array[end], array[pivot_index] = array[pivot_index], array[end]
    dictMatrix[end], dictMatrix[pivot_index] = dictMatrix[pivot_index], dictMatrix[end]
    # Returning end pointer to divide the array into 2
    return end


# The main function that implements QuickSort
def quick_sort(start, end, array, dictMatrix):

    if (start < end):
        # p is partitioning index, array[p]
        # is at right place
        p = partition(start, end, array, dictMatrix)

        # Sort elements before partition
        # and after partition
        quick_sort(start, p - 1, array, dictMatrix)
        quick_sort(p + 1, end, array, dictMatrix)

if __name__ == '__main__':
    data = panda.read_csv(r'C:\Users\bbbak\Documents\DynastyFFScouting\2021 Rookie Class\WR Prospects-Copy.csv')  # read the csv file
    print(data)
    names = data['Name'].tolist()
    dominators = data['Dominator Rating'].tolist()
    breakoutAges = data['Breakout Age'].tolist()
    seniorYears = data['Senior Year?'].tolist()
    smallBlowupGames = data['150 yard Blowup games'].tolist()
    bigBlowupGames = data['200 yard Blowup Games'].tolist()
    draftCapitals = data['Draft Capital'].tolist()
    yprs = data['YPR'].tolist()
    targetShares = data['Target Share'].tolist()
    ryptpaOAs = data['RYPTPA OA'].tolist()
    volumeTargets = data['Volume - Targets'].tolist()
    volumeReceptions = data['Volume - Receptions'].tolist()
    volumeYards = data['Volume - Yards'].tolist()
    years = data['Years?'].tolist()
    filmGrade = data['Film Grade'].tolist()
    length = len(names)
    finalScores = []
    dictMatrix = []
    scoreDictionary = {}
    for x in range(0, length):
        prospect = DynastyFootballCalculatorWRProspects(names[x], dominators[x], breakoutAges[x], seniorYears[x], smallBlowupGames[x],
                                                        bigBlowupGames[x], draftCapitals[x], yprs[x], targetShares[x], ryptpaOAs[x], volumeTargets[x],
                                                        volumeReceptions[x], volumeYards[x], years[x])
        penalty, bonus = prospect.penalty_and_bonus()
        score = prospect.score()

        finalScore = score * penalty + bonus + filmGrade[x]
        finalScores.append(finalScore)
        dictMatrix.append(x)
        scoreDictionary[x] = names[x], dominators[x], breakoutAges[x], seniorYears[x], smallBlowupGames[x], \
                             bigBlowupGames[x], draftCapitals[x], yprs[x], targetShares[x], ryptpaOAs[x], volumeTargets[x], \
                             volumeReceptions[x], volumeYards[x], years[x], filmGrade[x], finalScore
    # Driver code
    quick_sort(0, len(finalScores) - 1, finalScores, dictMatrix)

    finalNames = []
    finalDominators = []
    finalBreakoutAges = []
    finalSeniorYears = []
    finalSmallBlowupGames = []
    finalBigBlowupGames = []
    finalDraftCapitals = []
    finalYPRs = []
    finalTargetShares = []
    finalryptpaOAs = []
    finalVolumeTargets = []
    finalVolumeReceptions = []
    finalVolumeYards = []
    finalYears = []
    filmGrade = []


    for x in range(0, length):
        tempDict = scoreDictionary[dictMatrix[x]]
        finalNames.append(tempDict[0])
        finalDominators.append(tempDict[1])
        finalBreakoutAges.append(tempDict[2])
        finalSeniorYears.append(tempDict[3])
        finalSmallBlowupGames.append(tempDict[4])
        finalBigBlowupGames.append(tempDict[5])
        finalDraftCapitals.append(tempDict[6])
        finalYPRs.append(tempDict[7])
        finalTargetShares.append(tempDict[8])
        finalryptpaOAs.append(tempDict[9])
        finalVolumeTargets.append(tempDict[10])
        finalVolumeReceptions.append(tempDict[11])
        finalVolumeYards.append(tempDict[12])
        finalYears.append(tempDict[13])
        filmGrade.append(tempDict[14])

    csvFile = panda.DataFrame({'Name': finalNames,
                                'Dominator Rating': finalDominators,
                               'Breakout Age': finalBreakoutAges,
                               'Senior Year': finalSeniorYears,
                               '150 yard Blowup games': finalSmallBlowupGames,
                               '200 yard Blowup Games': finalBigBlowupGames,
                               'Draft Capital': finalDraftCapitals,
                               'YPR': finalYPRs,
                               'Target Share': finalTargetShares,
                               'RYPTPA OA': finalryptpaOAs,
                               'Volume - Targets': finalVolumeTargets,
                               'Volume - Receptions': finalVolumeReceptions,
                               'Volume - Yards': finalVolumeYards,
                               'Years': finalYears,
                               'Film Grade': filmGrade,
                               'Grades': finalScores})

    finalCSV = csvFile.to_csv("../FinalwrRankings.csv", index=False)