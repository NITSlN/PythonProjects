def quick_sort(seq):
    length = len(seq)
    if length<=1:
        return seq
    else:
        pivot = seq.pop()
        greater_list =[]
        lower_list =[]
        for item in seq:
            if item>pivot:
                greater_list.append(item)
            else:
                lower_list.append(item)
    return quick_sort(lower_list)+[pivot]+ quick_sort(greater_list)
print(quick_sort([5,2,4,6,3]))