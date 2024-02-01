# implement by linked list


class Stack():

    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0
    
    

    def __str__(self):
        return str(self.__dict__)

    def create_new_node(self,data):
        new_node = {
            "value" : data,
            "next" : None
        }
        return new_node

    def push(self, value):
        new_node = self.create_new_node(value)
        
        if self.length == 0:
            self.top = new_node
            self.bottom = new_node
        else:
            new_node["next"] = self.top          #other solution
            self.top = new_node                  #other solution
            
            # holding_pointer = self.top
            # self.top = new_node
            # self.top["next"] = holding_pointer
        
        self.length += 1

    def pop(self):
        value = self.top
        if(self.top == self.bottom):
            self.bottom = None
        self.top = self.top["next"]
        
        self.length -= 1
        return value
    
    def peek(self):
        return self.top

my_stack = Stack()
my_stack.push(3)
my_stack.push(4)
my_stack.push(5)
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())

# my_stack.pop()
# print(my_stack.peek())

print(my_stack)

#implement by array

class Stack2():

    def __init__(self):
        self.array = []
        self.length = 0
    
    def __str__(self):
        return str(self.array)

    def peek(self):
        return self.array[0]

    def push(self, value):
        if (self.length == 0):
            self.array = self.array + [value]
        else:
            self.array = [value] + self.array
        self.length += 1

    def pop(self):
        del self.array[0]
        self.length -= 1

# my_stack2= Stack2()
# my_stack2.push(3)
# my_stack2.push(4)
# my_stack2.push(5)

# my_stack2.pop()
# print(my_stack2.peek())


# print(my_stack2)
