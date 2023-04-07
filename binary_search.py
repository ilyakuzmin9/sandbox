list_test = [1, 5, 7, 9, 3, 5, 5, 9, 0, 3, 4, 6, 121, 150, 75]
list_test_sort = sorted(list_test)
left_pointer = 0
right_pointer = len(list_test) - 1


# classic
def binary_search(a_list, a_left_pointer, a_right_pointer, req_elem):
    while a_left_pointer <= a_right_pointer:
        mid = int((a_left_pointer+a_right_pointer)/2)
        if a_list[mid] == req_elem:
            return print(mid)
        elif req_elem < a_list[mid]:
            a_right_pointer = mid - 1
        elif req_elem > a_list[mid]:
            a_left_pointer = mid + 1
    return print(-1)


print(list_test_sort)
binary_search(list_test_sort, left_pointer, right_pointer, 3)


# recursively
def binary_search_rec(a_list, a_left_pointer, a_right_pointer, req_elem):
    if a_left_pointer > a_right_pointer:
        return print(-1)
    mid = int((a_left_pointer+a_right_pointer)/2)
    if a_list[mid] == req_elem:
        return print(mid)
    elif req_elem < a_list[mid]:
        a_right_pointer = mid - 1
        binary_search_rec(a_list, a_left_pointer, a_right_pointer, req_elem)
    elif req_elem > a_list[mid]:
        a_left_pointer = mid + 1
        binary_search_rec(a_list, a_left_pointer, a_right_pointer, req_elem)


print(list_test_sort)
binary_search_rec(list_test_sort, left_pointer, right_pointer, 150)
