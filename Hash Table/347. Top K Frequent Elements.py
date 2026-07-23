class Solution(object):
    def topKFrequent(self, nums, k):
        hash_map={}
        for i in nums:
            if i in hash_map:
                hash_map[i] +=1
            else:
                hash_map[i]=1
        listed=list(sorted(hash_map.items(),key=lambda x: x[1],reverse=True))
        i=0
        listed2=[]
        while i<k :
            listed2.append(listed[i][0])
            i+=1
        return listed2    
                  
                
                
                
        
        # listed=sorted(hash_map.values(),reverse=True)
        # listed2=[]
        # i=0
        # while i<k:
        #     listed2.append(listed[i])
        #     i +=1
        # return listed2
    
s=Solution()
print(s.topKFrequent([1,2,1,2,1,2,0,2,1,0],2))                