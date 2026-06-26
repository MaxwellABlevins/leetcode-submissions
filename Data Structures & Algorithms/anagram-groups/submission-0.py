class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        final = []
        finalIndex = 0
        seen = {}
        for i, s in enumerate(strs):
            chars = [0] * 26 

            for c in s:
                chars[ord(c) - 97] += 1

            key = tuple(chars)
            if key in seen:
                final[seen[key]].append(strs[i])
            else:
                final.append([strs[i]])
                seen[key] = finalIndex
                finalIndex += 1
            
        return final