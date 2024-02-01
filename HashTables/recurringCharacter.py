
arrays1 = [2,5,1,2,3,5,1,2,4] # should return 2
arrays2 = [2,1,1,2,3,5,1,2,4] # should return 1
arrays3 = [2,3,4,5]           # should return None
arrays4 = [2,5,5,2,3,5,1,2,4] # should return 5

def first_recurring_character(arrays):
    num_and_distance = {}
    distance = 0
    for i in range (len(arrays)):
        distance = 0
        if(arrays[i] not in num_and_distance): 
            for j  in range (i + 1, len(arrays) ):
                distance += 1
                if(arrays[i] == arrays[j]):
                    num_and_distance[arrays[i]] = distance
                    break

    if num_and_distance == {} :
        return None

    list_of_value = []
    for key in num_and_distance:
        list_of_value.append(num_and_distance[key])
    
    lowest_value = min(list_of_value)  
    for key in num_and_distance:
        if num_and_distance[key] == lowest_value:
            answer = key
            break

    return answer
# O(n^2)

# print(first_recurring_character(arrays3))


def first_recurring_character2(arrays):
    hashtable = {}
    for i in range(len(arrays)):
        if(arrays[i] in hashtable):
            return arrays[i]
        else :
            hashtable[arrays[i]] = i
    return None
# O(n)

print(first_recurring_character2(arrays1))
print(first_recurring_character2(arrays2))
print(first_recurring_character2(arrays3))
print(first_recurring_character2(arrays4))