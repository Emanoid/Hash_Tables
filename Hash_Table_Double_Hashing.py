import random
import string
class Dict:
    def __init__(self,key,elem):
        self._key = key
        self._elem = elem

    def getkey(self):
        return self._key

    def getelem(self):
        return self._elem

    def changekey(self,key):
        self._key = key

    def changelem(self,elem):
        self._elem = elem
#####################################################################################################
#HASH TABLE Double Hashing
# OPEN ADDRESSING
class DH_HASH_TABLE:
    def __init__(self,capacity):
        self._capacity = capacity
        self._array = []
        self._hnum = 13
        self._hnum2 = 7 
        self._collisions = 0
        for i in range(capacity):
            self._array.append(None)

    def print(self):
        for i in self._array:
            if i != None and i != 'Deleted':
                print(i.getkey(),':',i.getelem())
            else:
                print(i)

    def getcollisions(self):
        print(self._collisions)

    def clearcollisions(self):
        self._collisions = 0

    def hasher(self,key):
        hash = 0
        if type(key) == str:
            for i in key:
                hash =  hash + ord(i) 
            hash = hash % self._capacity
        else:
            hash = (key % self._capacity)
        return hash

    def hasher2(self,key):
        hash = 0
        if type(key) == str:
            for i in key:
                hash =  hash + ord(i) 
            hash = self._hnum2 - (hash % self._hnum2)
        else:
            hash = self._hnum2 - (key % self._hnum2)
        return hash

    def next(self,key,i):
        return i + self.hasher2(key) 

    def insert(self,Dict):
        key = Dict.getkey()
        hash = self.hasher(key)
        i = hash
        while i != None:  
            if self._array[i] == None:
                self._array[i] = Dict
                i = None
            elif self._array[i] == 'Deleted':
                i = self.next(key,i)
                self._collisions += 1
            elif self.next(key,i) == hash and self._array[i] != None:
                i = None
                print('Hash Table is Full')
            else:
                i = self.next(key,i) 
                self._collisions += 1

    def search(self,key):
        hash = self.hasher(key)
        i = hash
        while self._array[i] != None and i != None:
            if self._array[i] == 'Deleted':
                if self.next(key,i) == hash:
                    i = None
                    return False
                else:
                    i = self.next(key,i)
                    self._collisions += 1
            else:
                if self._array[i].getkey() == key:
                    i = None
                    return True
                elif self.next(key,i) == hash:
                    i = None
                    return False
                else:
                    i =  self.next(key,i)
                    self._collisions += 1
        return False

    def delete(self,key):
        if self.search(key) == False:
            print(key,'does not exist in Hash Table')
        else:
            hash = self.hasher(key)
            i = hash
            while i !=None and self._array[i] != None:
                if self._array[i] == 'Deleted':
                    i = self.next(key,i)
                    self._collisions += 1
                else:
                    if self._array[i].getkey() == key:
                        self._array[i] = 'Deleted'
                        i = None
                    else:
                        i = self.next(key,i)
                        self._collisions += 1

    def get(self,key):
        if self.search(key) == False:
            print(key,'does not exist in Hash Table')
        else:
            hash = self.hasher(key)
            i = hash
            while i !=None and self._array[i] != None:
                if self._array[i] == 'Deleted':
                    i = self.next(key,i)
                    self._collisions += 1
                else:
                    if self._array[i].getkey() == key:
                        return self._array[i].getelem()
                        i = None
                    else:
                        i = self.next(key,i)
                        self._collisions += 1     

#######################################################################################################
'''
def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))
P = DH_HASH_TABLE(1000)
E = ['sdsd','sdflsdjfsd','sdfsdfsd']
K = []
for i in range(75):
    K.append(randomString())

for i in K:
    P.insert(Dict(i,E))
P.getcollisions()
'''
H = DH_HASH_TABLE(20)
K = ['c','b','a','d','g','f','e','h']
E = ['sdsd','sdflsdjfsd','sdfsdfsd']
for i in K:
    H.insert(Dict(i,E))
#H.print()
print(H.get('d'))



