class CustomSet:

    def __init__(self, listSetElements):
        
        self._setElements = []
        
        for number in listSetElements:
            
            if number not in self._setElements:
                
                self._setElements.append(number)



    def __str__(self):
        
        stringList = str(self._setElements)
        
        return stringList
