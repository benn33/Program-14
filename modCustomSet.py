class CustomSet:

    def __init__(self, listSetElements):
        
        self._setElements = listSetElements

    def __str__(self):
        return str(self._setElements[0])
        
CustomSet([10,20,30])
print(CustomSet)
