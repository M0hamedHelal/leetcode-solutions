class Solution(object):
    def containsDuplicate(self, nums):
        hash_map={}
        for i in range(len(nums)):
            if nums[i] in hash_map:
                return True
            else:
                hash_map[nums[i]] =1
        return False    
    
    
#=========Anather Solution====================
# class Solution(object):
#     def containsDuplicate(self, nums):
#         seen = set()
#         for num in nums:
#             if num in seen:
#                 return True
#             seen.add(num)
#         return False 