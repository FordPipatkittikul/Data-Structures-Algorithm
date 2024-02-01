# Hash tables or what we call dictionary in pytohn


# insert O(1)
# lookup O(1)
# delete O(1)
# search O(1)

def scream():
    print('ahhhhhh')

user = {
    'age'    : 54,
    "name"   : "ford",
    "human"  : True,
    'scream' : scream
}


# insert O(1)
# user['sex'] = "male"
# print(user)
# print(user['sex'])

# delete O(1)
# del user['sex']
# print(user)

# access O(1)
# print(user['scream']())





#___________________________________________________________________

class HashTable:
    
    # constructor
    def __init__(self, size):
        self.size = size
        self.data = [None]*self.size
    
    #As in the array implementation, this method is used to print the attributes of the class object in a dictionary format
    def __str__(self): 
        return str(self.__dict__)

    def _hash(self, key): #Our private custom hash function
        hash = 0
        for i in range(len(key)):
            hash = (hash + ord(key[i])*i) % self.size #ord(key[i]) gives the unicode code point of the character key[i]
        return hash #The hash value obtained after applying the hash function to the key is returned
    
    def set(self,key,value):
        address = self._hash(key)
        if (self.data[address] == None ):
            self.data[address] = []
        self.data[address].append([key,value])
    
    def get(self,key):
        address = self._hash(key)
        current_address = self.data[address]
        if(len(current_address) != 0):
            for i in range (len(current_address)):
                if(current_address[i][0] == key):
                    value = current_address[i][1]
                    return value
        return None
    
    # not handle collisions
    def get_all_key(self):
        keys = []
        for i in range(len(self.data)):
            if self.data[i] != None :

                keys.append(self.data[i][0][0])
        return keys

    #handle collisions
    def keys(self):
        keys = []
        for i in range(self.size):   # loop through hash table
            if self.data[i] != None: # check that data is not None
                if (len(self.data[i]) > 1) :    # making sure that is hashcollisions by checking the size of data
                    for j in range(len(self.data[i])): # loop through that hashcollisions data
                        keys.append(self.data[i][j][0]) # append only key in our variable "keys"
                else: # if its not hashcollisions
                    keys.append(self.data[i][0][0])
        return keys

myHash = HashTable(2)

myHash.set("grapes", 100)
myHash.set("apples", 200)

#print(myHash.keys())

#________________________________________________________________
import collections

arrays1 =  [2,5,1,2,3,5,1,2,4]

# case 1
test_dic = {}
for i in range (len(arrays1)):
    test_dic[arrays1[i]] = i

print(test_dic) # {2: 7, 5: 5, 1: 6, 3: 4, 4: 8}


#case 2

test_dic2 = collections.defaultdict(list)
for i in range (len(arrays1)):
    test_dic2[arrays1[i]].append(i)

print(test_dic2) # defaultdict(<class 'list'>, {2: [0, 3, 7], 5: [1, 5], 1: [2, 6], 3: [4], 4: [8]})
