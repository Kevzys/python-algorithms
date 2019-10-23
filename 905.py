def sortArrayByParity(a):
    even = [2,4,6,8]
    odd = [1,3,5,7,9]

    new_list = []
    temp_list = []
    for x in a:
        if x in even:
            new_list.append(x)
        else:
            temp_list.append(x)
    return new_list + temp_list

a = [3,1,2,4]
print(sortArrayByParity(a))
