class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {} 

        for word in strs: 
            anagram = "".join(sorted(word))
            group = seen.get(anagram, [])
            group.append(word)
        
            seen[anagram] = group 

        return list(seen.values())