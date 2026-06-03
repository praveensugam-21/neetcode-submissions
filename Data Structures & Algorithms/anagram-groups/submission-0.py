class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dicti={}
        for word in strs:
            key=''.join(sorted(word))
            if key in dicti:
                dicti[key].append(word)
            else:
                dicti[key]=[word]
        return list(dicti.values())