class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for word in strs:
            key = "".join(sorted(word))
            group = seen.get(key, [])
            group.append(word)
            seen[key] = group
        return list(seen.values())
            