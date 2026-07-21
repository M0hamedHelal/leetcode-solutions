class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        i = 0  
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]

        return i + 1        
s=Solution()
arr=s.removeDuplicates([1,1,1,1,2,3,3,5])                    
print(arr)     


#=================================================================
# Anather Solution
# =================================================================
# class Solution(object):
#     def removeDuplicates(self, nums):
#         i = 0
#         while i < len(nums) - 1:
#             if nums[i] == nums[i + 1]:
#                 nums.pop(i + 1)
#             else:
#                 i+=1
#         return nums        
# s=Solution()
# arr=s.removeDuplicates([1,1,1,1,2,3,3,5])                    
# print(arr)


#=================================================================
# Anather Solution
# =================================================================

# class Solution(object):
#     def removeDuplicates(self, nums):
#         list1 = []
#         i = 0
#         while i < len(nums):
#             if nums[i] not in list1:
#                 list1.append(nums[i])
#             i += 1
#         nums[:] = list1 
#         return len(list1)