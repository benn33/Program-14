    def __le__(self, other):
        """
        Description: checks if one set is a subset of another
        Precondition: self(object), other(object)
        Postcondition: None
        """
        for el in self._setElements:
            if not el in other._setElements:
                return False
        return True

    def __ge__(self, other):
        """
        Description: checks if one set is a superset of another
        Precondition: self(object), other(object)
        Postcondition: None
        """
        for el in other._setElements:
            if not el in self._setElements:
                return False
        return True

    def __sub__(self,Other):
        """
        Description: returns a new set with elements in the first list but not
        in the second.
        Precondition: self(object), other(object)
        Postcondition: None
        """
        finalList = [number for number in self._setElements\
                     if number not in other._setElements]
        return finalList
        if finalList == []:
            return "No Difference in list"
