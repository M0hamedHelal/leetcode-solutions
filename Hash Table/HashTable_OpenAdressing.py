"""
How to build HashTables
1-Construct the class with basic function like ( get , put , delete ) . 
2-Role of HashFunction
3-Collision Resolution
   |-Open Addressing ==>> (if the index is occupied then we will find the next empty index)
   |-Chaining ==>> (if the index is occupied then we will create a list of values in that index)
"""
class HashTable:
    def __init__(self,size=5):
        self.size=size
        self.table=[None]*size
    
    def hashFunction(self, key):
        index=hash(key) % self.size
        return index
    
    def put(self,key,value):
        index=self.hashFunction(key)
        print(f"index={index} key={key} value={value}")
        for _ in range(self.size):
            if self.table[index] is None or key==self.table[index][0]:
                self.table[index]=(key,value)
            else:
                index=(index+1) % self.size
            
    
    
    
    
    def get(self,key):
        index=self.hashFunction(key)
        for _ in range(self.size):
            if (self.table[index][0]==key):
                return self.table[index][1]
            else:
                index=(index+1)%self.size 
    
    
    
    def delete (self,key):
        index=self.hashFunction(key)
        self.table[index]=None 
    
    
    def display(self):
        for i in range(len(self.table)):
            print(f"{i} | {self.table[i]}")
            
            
ht=HashTable()
ht.put("name","mo1")            
ht.put("adress","cairo")            
ht.put("phone","1234567890")            
ht.put("nickname","ELMO")            
ht.put("name","mo5")            
ht.display()                            
# print(ht.hashFunction("name")                    )
                    