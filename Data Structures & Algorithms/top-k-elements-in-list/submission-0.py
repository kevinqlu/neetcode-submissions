class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        result = []
    
        for num in nums: 
            seen[num] = seen.get(num, 0) + 1
        
        ranked = sorted(seen.items(), key=lambda x:x[1], reverse=True)
        
        for pair in ranked[:k]:
            result.append(pair[0])
        return result