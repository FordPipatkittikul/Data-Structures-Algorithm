# Data Structures & Algorithm
## Run time complexity(Big O)
- O(1) Constant – no loops

- O(log N) Logarithmic – usually searching algorithms have log n if they are sorted (Binary Search)

- O(n) Linear – for loops, while loops through n items

- O(n log(n)) Log Linear – usually sorting operations

- O(n^2) Quadratic – every element in a collection needs to be compared to ever other element. Two nested loops
                     
- O(2^n) Exponential – recursive algorithms that solves a problem of size N

- O(n!) Factorial – you are adding a loop for every element

- Iterating through half a collection is still O(n). 

- Two separate collections: O(a * b)
## Space complexity(Big O)
    What causes Space Complexity
    
      • Variables
      
      • Data Structures
      
      • Function Call
      
      • Allocations
![Screenshot (46)](https://github.com/FordPipatkittikul/DataStructures/assets/121902625/792770f3-572f-4683-b056-8331ea22f59b)

![Screenshot (47)](https://github.com/FordPipatkittikul/DataStructures/assets/121902625/1552f166-7265-4e17-b74d-4edd7f62b59c)

![Screenshot (45)](https://github.com/FordPipatkittikul/DataStructures/assets/121902625/f1fad31b-62da-41c2-8fcd-c684f5558578)

![Screenshot (44)](https://github.com/FordPipatkittikul/DataStructures/assets/121902625/3f47a8e9-65bf-4d1d-9ed7-9ed6ee667090)
# Built-in DataStructures
Quick Note using Python programming language as a reference.
## Array
  It is a collections of data type stored contiguous memory locations(ordered collections of values)
    operation run time complexity
    
      - Insertion : O(n)
      
      - Deletion : O(n)
      
      - accessing by index: O(1)
      
      - Append : O(1)
## Hash Table or dictionary
  It is unordered data structure that stores pairs of key-value
    operation run time complexity
    
      - accessing by key : O(1)
      
      - Insertion: O(1)
      
      - Deletion: O(1)
## tuple
   It is ordered collection of data type and being used for immutable things (that don't change).
     
    operation run time complexity
    
     - access by index O(1)
## sets
  It is unorederd collection of unique elements.
    
    operation run time complexity
    
     - Insertion: O(1)
     
     - Deletion: O(1)
# self-defined DataStructures

## Linked Lists
  A linked list is a common data structure made of one or more than one node. Each node contains a value and a pointer to the previous/next node forming the chain-like structure

      operation run time complexity
      
        - prepend: O(1)
        
        - append: O(1)
        
        - lookup: O(n)
        
        - insert: O(n)
        
        - delete: O(n)
### singly linked list
    a linear data structure comprising of nodes chained together in a single direction. Each node contains a data member holding useful information, and a pointer to the next node. Can traverse forward
![LLdrawio](https://github.com/FordPipatkittikul/DataStructures/assets/121902625/c0f2bf7c-4bd4-4878-b4f3-e765db6f4663)
### Doubly linked list
    A doubly linked list contains a pointer to the next node as well as the previous node. This ensures that the list can be traversed in both directions(forward and backward).
![DLL1](https://github.com/FordPipatkittikul/DataStructures/assets/121902625/c97331b9-276d-4993-8b41-6119e6a8e53e)
# Stacks
  Stack is a linear data structure in which the element inserted last is the element to be deleted first. LIFO method(Last In First Out)

    operation run time complexity
    
      - push: O(1)
      
      - pop: O(1)
  
![stack](https://github.com/FordPipatkittikul/DataStructures/assets/121902625/ad9f7fd7-20cd-4683-8419-e3e8db5b82c9)
# queue
  similar to a stack. A queue uses the FIFO method(First In First Out), by which the first element that is enqueued will be the first one to be dequeued.
    operation run time complexity
    
      - enqueue Inserts an element to the end of the queue: O(1)
      
      - dequeue Removes an element from the start of the queue: O(1)
      
      - isempty Returns true if the queue is empty: O(1)
      
      - peek Returns the first element of the queue: O(1)

![queue](https://github.com/FordPipatkittikul/DataStructures/assets/121902625/d784d191-5ac8-4a45-93a6-34d86ab1feb8)
# Tree
# Graph




        


    


