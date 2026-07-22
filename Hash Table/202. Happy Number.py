class Solution(object):
    def isHappy(self, n):
        s=str(n)
        seen=set()
        while True:
            sum=0
            for i in s :
               sum+=int(i)**2
            
            if sum in seen :
                return False
            elif sum==1:
                return True  
            seen.add(sum)  
            s=str(sum) 
        