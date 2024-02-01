# reverse String question
# hint: string are simply an array of char

# way to solve problem
# 1) check input. you cannot assume you always recieve a string


# solution 1 using for loop
def reverse(str):
    
    string_length = len(str)
    list_of_chars = list(str)
    reverse_list_of_chars = ""
    
    if string_length < 2 or type(str).__name__ != 'str' :
        return False
    else:
        for i in str:
            reverse_list_of_chars = i + reverse_list_of_chars
        return reverse_list_of_chars

# str = "Nithi"
# print(reverse(str))

################## the rest of the solution I assume that Input is a string bc I'm lazy ###################

# solution 2 using while loop

def reverse2(str):
    
    length = len(str)
    reverse_str = ""
    i = length - 1
    while i >= 0 :
        reverse_str = reverse_str + str[i]
        i = i - 1
    return reverse_str

# str = "Nithi"
# print(reverse2(str))

# solution 3 using slicing

#For a list or tuple: my_list[::-1] or my_tuple[::-1] 
#                     will return a new list or tuple with the elements in reverse order.
#For a string: my_string[::-1] will return a new string with the characters in reverse order.

def reverse3(string):
    return string[::-1]

# str = "Nithi"
# print(reverse3(str))


# solution4 using .join()

def reverse4(str):
    
    string_length = len(str)
    list_of_chars = list(str)
    reverse_list_of_chars = []
    
    for i in range(string_length):
        reverse_list_of_chars.append( list_of_chars[string_length - (i + 1)] )
    
    answer = "".join(reverse_list_of_chars)
    return answer

str = "ahr"
print(reverse4(str))


