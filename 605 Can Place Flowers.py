class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        res = 0
        index = 0
        while index < len(flowerbed):
            prev_index = index-1 if index > 0 else 0
            prev_value = flowerbed[prev_index]
            next_index = index+1 if index < len(flowerbed)-1 else 0
            next_value = flowerbed[next_index]
            curr_value = flowerbed[index]

            print(prev_value, curr_value, next_value)
            if curr_value == 0 and prev_value == 0 and next_value == 0:
                res += 1
                index += 2
            else:
                index += 1
            print(res)
            return res >= n
        