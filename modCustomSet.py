-"""
 -Ben was to do: The constructor, the Str method, and the intersction of sets. (#'s 1,9,3)
 -
 -Martin was to do: The difference of sets, the supset, and determining if a set is a subset (#'s 6,4,7)
 -
 -George was to do: The number of elements, Union of sets, and testing for membership  (#'s 8,2,5)
 -
 -"""
 -__author__ = " Ben Rode, Martin Luna, George Murray "
 -__date__ = "4/27/16 "
 -
 -class CustomSet:
 -
 -    def __init__(self, listSetElements):
 -        '''
 -        Preconditions: listSetElements is of type list.
 -
 -        Postconditions: A CustomSet object is created.
 -
 -        Description: This is the constructor method of the CustomSet class. listSetElements is of type list.
 -        
 -        '''
 -        self._setElements = []
 -        
 -        for number in listSetElements:
 -            
 -            if number not in self._setElements:
 -                
 -                self._setElements.append(number)
 -
 -
 -
 -    def __str__(self):
 -        '''
 -        Preconditions: none.
 -
 -        Postconditions: The Custom Set object is converted to a string.
 -
 -        Description: This is the String method for the class CustomSet. The ending result is that the set appears
 -                     in the format:  " { SET NUMBERS } "
 -        
 -        '''
 -        
 -        stringList = "{"+ str(self._setElements) + "}"
 -        
 -        return stringList
 -
 -
 -    def __and__(self,otherElementSet):
 -        '''
 -        Preconditions: otherElementSet is of type CustomSet
 -
 -        Postconditions: A new list is created that has all the common elements of a set together.
 -
 -        Description: This checks to see if there are any of the same numbers in two different sets,
 -                     and if there are, they are added to a new list called commonList, then passes
 -                     that list to commonClassList which then creates an object of type CustomSet.
 -        
 -        '''
 -        
 -        commonList = [item for item in otherElementSet._setElements if item in self._setElements]
 -        commonClassList = CustomSet(commonList)
 -       
 -        return commonClassList


    def getNumElement(self):
        ct=0
        for el in self._setElements:
            ct+=1
        return ct

    def __add__(self,tmpJoiner):
        res=[]
        for el in self._setElements:
            res.append(el)
        for ele in tmpJoiner._setElements:
            if ele not in self._setElements:
                res.append(ele)
        return res
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

    



    
        
