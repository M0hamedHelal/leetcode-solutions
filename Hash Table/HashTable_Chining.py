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
        self.table=[[] for _ in range(self.size)]
    
    def hashFunction(self, key):
        index=hash(key) % self.size
        return index
    
    def put(self,key,value):
        index=self.hashFunction(key)
        print(f"index={index} key={key} value={value}")
        inner_list=self.table[index]
        for i in range(len(inner_list)):
            if key==self.table[index][i][0]:
                inner_list[i]=(key,value)
                return
        self.table[index].append((key,value))
    
    
    
    def get(self,key):
        index=self.hashFunction(key)
        for i in range(len(self.table[index])):
            if key==self.table[index][i][0]:
                return self.table[index][i][1] 
        return None
    
    def delete (self,key):
        index=self.hashFunction(key)
        for i in range(len(self.table[index])):
            if key==self.table[index][i][0]:
                del self.table[index][i]
                return True
        return False
    
    def display(self):
        for i in range(len(self.table)):
            print(f"{i} | {self.table[i]}")
            
            
ht=HashTable()
ht.put("name","mo1")            
ht.put("adress","cairo")            
ht.put("phone","1234567890")            
ht.put("nickname","ELMO")            
ht.put("name","mo5") 
print(ht.get("name"))
print(ht.get("adress"))
print(ht.get("phone"))
print(ht.delete("name"))
ht.display()                            
# print(ht.hashFunction("name")                    )
                    