import random
import string as string
##########################################################################################
class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None        
    
    def get_head(self):
        return self._head

    def isEmpty(self):
        if self._head == None:
            return True
        else:
            return False

    #To make the given node the head
    def insert_head(self, node):
        node.change_link(self._head)
        self._head = node
    
    def inserttail(self,data):
        node = Node(data,self._tail)
        if self._head == None:
            self._head = node
        else:
            temp = self._head
            while temp != None:
                if temp.get_link() == None:
                    temp.change_link(node)
                    temp = None
                else:
                    temp = temp.get_link()
    
    def print(self,node,LIST):
        if node != None:
            data = node.get_data().print()
            LIST.append(data)
            self.print(node.get_link(),LIST)
        return LIST

    #To compute if a node-data is in the LinkedList
    def search(self,node,key):
        if (node != None and node.get_data().getkey() == key):
            return True
        elif(node != None and node.get_link() != None):
            return self.search(node.get_link(),key)
        else:
            return False

    #To remove a node from the LinkedList
    def remove(self,key):
        elem = []
        elem = self.removehelper(self._head, elem)
        for i in elem:
            if i.getkey() == key:
                elem.remove(i)
        elem.reverse()
        self._head = None
        for i in elem:
            self.insert_head(Node(i,None))

    #To help the remove function
    def removehelper(self,node,elem):
        if (node != None):
            elem.append(node.get_data())
            self.removehelper(node.get_link(),elem)
        return elem
            
    def getnode(self,node,key):
        if node != None:
            if node.get_data().getkey() == key:
                return node.get_data().getelem()
            else:
                return self.getnode(node.get_link(),key)
        
##################################################################################
class Node:
    #Node: data Node
    def __init__(self,data,link):
        self._data = data
        self._link = link
    
    #To get the data in a node
    def get_data(self):
        return self._data
    
    #To mutate the data in a node
    def change_data(self, data):
        self._data = data
    
    #To get node that is linked to this node
    def get_link(self):
        return self._link
    
    #To mutate the node that is linked to this node
    def change_link(self, link):
        self._link = link
############################################################################################
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

    def print(self):
        return f'({self._key}:{self._elem})'
#####################################################################################################
#HASH TABLE - WITH LINKED-LISTS (FROM UNIQUE DYNAMIC ARRAY)
# CLOSED ADDRESSING
# A Bucket is a Linked List
class LL_HASH_TABLE:
    def __init__(self,capacity):
        self._capacity = capacity
        self._array = []
        self._hnum = 13
        for i in range(capacity):
            self._array.append(LinkedList())

    def print(self):
        for i in self._array:
            print(i.print(i.get_head(),[]))

    def hasher(self,key):
        hash = 0
        if type(key) == str:
            for i in key:
                hash =  hash + ord(i) 
            hash = hash % self._capacity
        else:
            hash = (key % self._capacity)
        return hash

    def insert(self,Dict):
        key = Dict.getkey()
        hash = self.hasher(key)
        self._array[hash].inserttail(Dict)

    def search(self,key):
        hash = self.hasher(key)
        head = self._array[hash].get_head()
        return self._array[hash].search(head,key)

    def delete(self,key):
        if self.search(key) == False:
            print(key,'does not exist in Hash Table')
        else:
            hash = self.hasher(key)
            self._array[hash].remove(key)

    def get(self,key):
        if self.search(key) == False:
            print(key,'does not exist in Hash Table')
        else:
            hash = self.hasher(key)       
            head = self._array[hash].get_head()
            print(self._array[hash].getnode(head,key))     
#######################################################################################################
'''
def randomString(stringLength=10):
    #Generate a random string of fixed length 
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))
H = LL_HASH_TABLE(50)
K = []
E = ['sdsd','sdflsdjfsd','sdfsdfsd']
for i in range(75):
    K.append(randomString())
for i in K:
    H.insert(Dict(i,E))

H.print()
'''
'''
H = LL_HASH_TABLE(20)
K = ['c','b','cat','d','g','f','e','h','atc']
E = ['sdsd','sdflsdjfsd','sdfsdfsd']
for i in K:
    H.insert(Dict(i,E))
H.print()
#print(H.search('es'))
#H.get('hsd')
'''