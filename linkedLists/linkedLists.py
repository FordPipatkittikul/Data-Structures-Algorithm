class LinkedList() :

    # constructor
    def __init__(self,data):
        self.head = {
            "value" : data,
            "next" : None
        }
        self.tail = self.head
        self.length = 1

    # Originally If you print object, It will return memmory address for that object.
    # So this function is make our print statement more readable.
    def __str__(self):
        return str(self.__dict__)
    
    
    def create_new_node(self,data):
        new_node = {
            "value" : data,
            "next" : None
        }
        return new_node
    
    def append(self,data):
        new_node = self.create_new_node(data)
        self.tail["next"] = new_node
        
        # print(hex(id(self.tail))) # head and are in same memory address
        # print(hex(id(self.head)))
        # print(" ")
        self.tail = new_node
        # print(hex(id(self.tail)))
        # print(hex(id(new_node)))
        # print(" ")
        self.length += 1
    
    # add the beginning of the list
    def prepend(self,data):
        new_node = self.create_new_node(data)
        new_node["next"] = self.head
        self.head = new_node
        self.length += 1

    def insert(self,index,data):
        new_node = self.create_new_node(data)
        if index == 0 :
            self.prepend(data)
            self.length += 1

        if (index == (self.length - 1) ):
            self.append(data)
            self.length += 1

        if (index >= self.length):
            return "out of bound"
        
        if(index > 0 and index < (self.length - 1)):
            new_node["value"] = data
            new_node["next"] = self.traverse_to_index(index)
            leader = self.traverse_to_index(index - 1)
            leader["next"] = new_node
            self.length += 1
    
    def traverse_to_index(self,index):
        counter = 0
        current_node = self.head
        while counter != index :
            current_node = current_node['next']
            counter += 1
        return current_node

    def delete(self,index):

        if(index == 0):
            self.head = self.head['next']
            self.length -= 1

        if (index == (self.length - 1) ):
            before_tail = self.traverse_to_index(self.length - 2)
            before_tail['next'] = None
            self.tail['value'] = before_tail["value"]

            self.length -= 1

        if (index >= self.length):
            return "out of bound"
        
        if(index > 0 and index < (self.length - 1)):
            before_delete_one = self.traverse_to_index(index - 1)
            after_delete_one = self.traverse_to_index(index + 1)
            before_delete_one["next"] = after_delete_one
            # print(hex(id(before_delete_one)))
            # print(hex(id(self.head)))
            # print(hex(id(self.tail)))
            self.length -= 1
        
    # assuming no duplicate value allowed
    def search(self,data):
        counter = 0
        current_node = self.head
        while counter < self.length :
            if(current_node["value"] == data):
                return counter
            current_node = current_node['next']
            counter += 1
        
        if(counter == (self.length) ):
            return "not found"
        
    def reverse(self):

        if(self.length == 1):
            return self.head
        
        first_node = self.head
        self.tail = self.head     
        
        second_node = first_node["next"]
        

        while(second_node != None):
            temp = second_node["next"]
            second_node["next"] = first_node
            first_node = second_node
            second_node = temp

        self.head["next"] = None
        self.head = first_node



            
    
myLinkedList = LinkedList(1)
myLinkedList.append(2)
# myLinkedList.append(3)



print("")
print("myLinklist   "  + str(myLinkedList))
print("")
# myLinkedList.reverse()
# print("myReverseLinklist   "  + str(myLinkedList))
# print(myLinkedList.head)
# print(myLinkedList.head["next"])
# print(myLinkedList.head["next"]["next"])
# print(myLinkedList.head["next"]["next"]["next"])
print("")
# print(myLinkedList.traverse_to_index(2))
# myLinkedList.prepend(6)


