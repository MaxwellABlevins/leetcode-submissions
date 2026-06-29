class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        longP = strs[0]

        for i in strs:
            if longP == "":
                return ""
            preS = i[:len(longP)]
            
            if preS == longP:
                continue
            else:
                while preS != longP:
                    longP = longP[:(len(longP) - 1)]
                    preS = preS[:len(longP)]
                    print(preS)
                    print(longP)
                    
        return longP