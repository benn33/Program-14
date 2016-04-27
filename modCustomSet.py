"""
Ben was to do: The constructor, the Str method, and the intersction of sets. (#'s 1,9,3)

Martin was to do: The difference of sets, the supset, and determining if a set is a subset (#'s 6,4,7)

George was to do: The number of elements, Union of sets, and testing for membership  (#'s 8,2,5)

"""
__author__ = " Ben Rode, Martin Luna, George Murray "
__date__ = "4/27/16 "

class CustomSet:

    def __init__(self, listSetElements):
        '''
        Preconditions: listSetElements is of type list.

        Postconditions: A CustomSet object is created.

        Description: This is the constructor method of the CustomSet class. listSetElements is of type list.
        
        '''
        self._setElements = []
        
        for number in listSetElements:
            
            if number not in self._setElements:
                
                self._setElements.append(number)



    def __str__(self):
        '''
        Preconditions: none.

        Postconditions: The Custom Set object is converted to a string.

        Description: This is the String method for the class CustomSet. The ending result is that the set appears
                     in the format:  " { SET NUMBERS } "
        
        '''
        
        stringList = "{"+ str(self._setElements) + "}"
        
        return stringList


    def __and__(self,otherElementSet):
        '''
        Preconditions: otherElementSet is of type CustomSet

        Postconditions: A new list is created that has all the common elements of a set together.

        Description: This checks to see if there are any of the same numbers in two different sets,
                     and if there are, they are added to a new list called commonList, then passes
                     that list to commonClassList which then creates an object of type CustomSet.
        
        '''
        
        commonList = [item for item in otherElementSet._setElements if item in self._setElements]
        commonClassList = CustomSet(commonList)
       
        return commonClassList
