class Solution:
    def mySqrt(self, x: int) -> int:

        def recursiveBinarySearch(s, e):
            if s>e:
                return e
            mid = (s+e) // 2
            if mid*mid == x:
                return int(mid) 
            elif mid*mid > x:
                return recursiveBinarySearch(s, mid-1)
            else:
                return recursiveBinarySearch(mid+1, e)
        return recursiveBinarySearch(0,x)
