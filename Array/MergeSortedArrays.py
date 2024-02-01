# question merge SortedArrays

# solution 1 combining them and using sort()

def merge_Sorted_Arrays(list1,list2):
    for i in list2:
        list1.append(i)
    
    list1.sort()
    return list1

list1 = [0,3,4,31]
list2 = [4,6,30]
# print(merge_Sorted_Arrays(list1,list2))

# solution 2

def solution2(list1,list2):
    length1 = len(list1)
    length2 = len(list2)
    if(length1 == 0 ):
        return list2
    if(length2 == 0 ):
        return list1
    i = 0
    j = 0
    merge_Arrays = []
    while (i < length1 and j < length2):
        if(list1[i] <= list2[j] ):
            merge_Arrays.append(list1[i])
            i += 1
        elif(list1[i] > list2[j]):
            merge_Arrays.append(list2[j])
            j +=1
    
    return merge_Arrays  + list1[i:]+ list2[j:] 


# print(solution2(list1,list2))



 
        