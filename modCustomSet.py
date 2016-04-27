


    def getNumElement(self):
        ct=0
        for el in self._setElements:
            ct+=1
        return ct

    def union(self,tmpJoiner):
        res=[]
        for el in self._setElements:
            res.append(el)
        for ele in tmpJoiner._setElements:
            if ele not in self._setElements:
                res.append(ele)
        return res


    



    
        
