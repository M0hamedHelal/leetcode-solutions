class Solution(object):
    def getIntersectionNode(self, headA, headB):
        seen=set()
        current=headA
        while current is not None:
            seen.add(current)
            current=current.next
        current=headB
        while current is not None :
            if current in seen :
                return current 
            current=current.next   
        return None
          

        