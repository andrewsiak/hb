
def mergeTwoLists(list1, list2):
    # create a new empty list
    # if list1 and list 2 are empty return new_list 
    # if list1[0] exists
    # check if less than or equal to list 2 index 0
    # if true, pop and add to new_list
    # if false, pop list2[0] and add to new list

    new_list = []
    if list1 == [] and list2 == []:
        return new_list
    if list1[0] <= list2[0]:
        new_list.append(list1[0])
        list1.leftpop()
    else:
        new_list.append(list2[0])
        list2.leftpop
            

