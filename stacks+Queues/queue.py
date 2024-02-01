class queue():

    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0
    
    

    def __str__(self):
        return str(self.__dict__)

    def create_new_node(self,value):
        new_node = {
            "value" : value,
            "next" : None
        }
        return new_node
    
    def peek(self):
        return self.first
    
    def enqueue(self,value):
        new_node = self.create_new_node(value)
        if(self.length == 0):
            self.first = new_node
            self.last = new_node
        else:
            self.last["next"] = new_node
            self.last = new_node
        self.length += 1
    
    def dequeue(self):

        if(self.length == 0 ):
            return None
        
        self.first = self.first["next"]
        
        if(self.length == 1):
            self.last = None
        
        

        self.length -= 1

my_queue = queue()

my_queue.enqueue(3)
my_queue.enqueue(4)
my_queue.enqueue(43)
my_queue.dequeue()
my_queue.dequeue()
print(my_queue.peek())
print(my_queue)