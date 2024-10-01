class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_val = max(candies)
        res = []
        for elem in candies:
            if elem + extraCandies >= max_val:
                res.append(True)
            else:
                res.append(False)
        return res