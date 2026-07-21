"""
How to build HashTables
1-Construct the class with basic function like ( get , put , delete ) . 
2-Role of HashFunction
3-Collision Resolution
"""

class HashTable:
    def __init__(self,size=5):
        self.size=size
        self.table=[None]*size
        
    def put(self,key,value):
        for i in range(self.table):
            if self.table[i] is None:
                self.table[i]=(key,value)  
                return
    
    
    
    
    def get(self,key):
        pass
    
    
    
    def delete (self,key):
        pass
    
    
    def display(self):
        for i in range(len(self.table)):
            print(f"{i} | {self.table[i]}")
            
            
ht=HashTable()
ht.put("name","mo1")            
ht.put("name","mo2")            
ht.put("name","mo3")            
ht.put("name","mo4")            
ht.put("name","mo5")            
ht.display()            
            
            
                    