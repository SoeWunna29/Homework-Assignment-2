def checking(x):
    input_num = str(x)
    unsorted_list = []
    if x > 0:
        for i in input_num:
            unsorted_list.append(i)
        if unsorted_list == sorted(unsorted_list):
            return True
        else:
            return False
    else:
        return False


print(checking(123))
print(checking(1357))
print(checking(1375))
