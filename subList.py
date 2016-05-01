def __sub__(self,firstList,secondList):
    thirdList = [number for number in firstList if number not in secondList]
    return thirdList
