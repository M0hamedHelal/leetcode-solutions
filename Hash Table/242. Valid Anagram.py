# class Solution(object):
#     def isAnagram(self, s, t):
#         if len(s) != len(t):
#             return False
#         hash_map1={}
#         hash_map2={}
#         for i in range(len(s)):
#             if s[i] in hash_map1 :
#                 hash_map1[s[i]] +=1
#             else:
#                 hash_map1[s[i]]=1    
        
#         for i in range(len(t)):
#             if t[i] in hash_map2 :
#                 hash_map2[t[i]] +=1
#             else:
#                 hash_map2[t[i]]=1   
#         if hash_map1 ==hash_map2:
#             return True
#         else:
#             return False              






# =============Anather Solution================
class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        hash_map1={}
        for i in range(len(s)):
            if s[i]  in hash_map1:
                hash_map1[s[i]] +=1
            else:
               hash_map1[s[i]] =1     
            if t[i]  in hash_map1:
                hash_map1[t[i]] -=1
            else:
               hash_map1[t[i]] =-1   
        for value in hash_map1.values():
            if value != 0:
                return False
        return True        
        
        
s1=Solution()

print(s1.isAnagram("anagram","nagaram"))        