# lookup O(1)
# append O(1), pop O(1)
# insert O(n)
# delete O(n)
 
lists_of_strings = ['a','b','c']

# access O(1)
#print(lists_of_strings[1]);

# Insertion at the end O(1)
lists_of_strings.append('d');
#print(lists_of_strings);

# deletion at the end O(1)
lists_of_strings.pop()
#print(lists_of_strings);

# Insertion O(n)
# because all the existing elements have to be shifted by one position to make space for the new element at index 0
lists_of_strings.insert(0, 'sad')
#print(lists_of_strings);

# O(n/2)
lists_of_strings.insert(2, 'very_sad')
#print(lists_of_strings);

#___________________________________________________________________________________________________________________________

### static_array V.S. dynamic_array

# Static Array: memory is allocated at compile time having a fixed size of it

# Dynamic Array: memory is allocated at run time but not having a fixed size

#___________________________________________________________________________________________________________________________

### making an array

class Myarray :

    # constructor
    def __init__(self) :
        self.length = 0
        self.data = {}
    
    def __str__(self):
        # Customize the string representation
        return f"Myarray object [ length: {self.length}, data: {self.data} ] "
        
    def get(self, index):
        return self.data[index]
    
    def push(self, item):
        self.data[self.length] = item
        self.length = self.length + 1
        return self.length
    
    def pop(self):
        last_Item = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length -= 1
        return last_Item
    
    def delete(self,index):
        item = self.data[index]
        self.shift_items(index)
    
    def shift_items(self,index):
        i = index
        while i < self.length - 1:
            self.data[i] = self.data[i+1]
            i = i + 1
        
        del self.data[self.length - 1]
        self.length -= 1 

new_array = Myarray()

new_array.push('hi')
new_array.push('I')
new_array.push('love')
# new_array.pop()
# new_array.pop()
new_array.delete(0)
print(new_array)

#___________________________________________________________________________________________________________________________   



    