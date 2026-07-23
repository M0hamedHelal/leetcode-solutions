from collections import Counter
class Solution(object):
    def frequencySort(self, nums):
        count=Counter(nums)
        def custom_sort(n):
            return(count[n],-n)
        nums.sort(key=custom_sort)
        return nums
        