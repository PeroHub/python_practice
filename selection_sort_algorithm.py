"""The selection sort algorithm finds the minimum value in a list and rearrange the list from the minimum value to the highest:  First, its set the first element of the list as the minimumn value, loop through the entire element to the right and set the new minimum value once a lowe number smaller than the initial minimum value is found"""

def selection_sort(list_a):
    indexing_length = range(0, len(list_a)-1)

    for i in  indexing_length:
        min_value = i

        for j in range(i+1, len(list_a)):
            if list_a[j] < list_a[min_value]:
                min_value = j
        if list_a[min_value] != i:
            list_a[min_value], list_a[i] = list_a[i], list_a[min_value]
    return list_a

print(selection_sort([3,4,5,6,7,8,9,5,2,4,6]))