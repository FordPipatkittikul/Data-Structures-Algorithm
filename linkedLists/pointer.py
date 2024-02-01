# pointer is basiclly a reference to another object

# ex1
obj1 = { "sex" : "boy",
          "age": 12}
obj2 = obj1 # this one I m not just copy obj1. 
            # both obj1 and obj2 point into the same location of memory
            

obj2["age"] = 14

print(obj1) # {'sex': 'boy', 'age': 14}
print(obj2) # {'sex': 'boy', 'age': 14}
print(hex(id(obj1)))
print(hex(id(obj2)))


del obj1
print(obj2) # {'sex': 'girl'}

print("""end ex1
      """)
#_________________________________________________________________

# ex2

obj3 = { "sex" : "boy",
          "age": 12}

obj4 = obj3

obj3 = 4

print(obj3) # {'sex': 'boy', 'age': 14}
print(obj4) # {'sex': 'boy', 'age': 14}
print(hex(id(obj3)))
print(hex(id(obj4)))

#_________________________________________________________________

# ex3

x = [1,2,3]
y = [4,5,6]
z = [7,8,9]

x = y
z = y

y.append(100) 

print(x,y,z) # [4, 5, 6, 100] [4, 5, 6, 100] [4, 5, 6, 100]

