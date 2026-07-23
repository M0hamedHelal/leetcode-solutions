class Solution(object):
    def groupAnagrams(self, strs):
        hash_map={}
        for i in strs:
            str_word=''.join(sorted(i))
            if str_word in hash_map:
                hash_map[str_word].append(i)
            else:
                hash_map[str_word]=[i] 
        listed=[]           
        for i in hash_map:
            listed.append(hash_map[i]) 
        return listed 
        # return list(hash_map.values())   
            
s=Solution()
print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"])   )         
                
   
        
        
        
        