class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        prevfind = intervals[0][1]

        for start, end in intervals[1:]:
            if start >= prevfind:
                prevfind = end

            else:
                res += 1
                prevfind = min(prevfind, end)

        return res




        