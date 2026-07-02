class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1 
        right = max(piles)
        res = right

        while left <= right:
            mid = left + (right - left) // 2
            TotalTime = 0 
            for pile in piles:
                TotalTime += math.ceil(float(pile) / mid)

            if TotalTime > h:
                left = mid + 1
            else:
                res = mid
                right = mid - 1
        return res 



        