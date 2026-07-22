class Solution(object):
    def twoSum(self, nums, target):
        hash_map={}
        for i in range(len(nums)):
            curent=target-nums[i]
            if nums[i] not in hash_map:
                
                hash_map[curent]=i
            else:
                return (hash_map[nums[i]],i) 
                   
            
s1=Solution()    
result=s1.twoSum([2,7,11,15],9)            
print(result)                
        
    
        