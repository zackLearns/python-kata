def merge(left_array, right_array):
    merged_array = []
    left_index = 0
    right_index = 0

    while left_array and right_array and left_index < len(left_array) and right_index < len(right_array):

        if left_array[left_index] < right_array[right_index]:
            merged_array.append(left_array[left_index])
            left_index += 1
        else:
            merged_array.append(right_array[right_index])
            right_index += 1

    while left_index < len(left_array):
        merged_array.append(left_array[left_index])
        left_index += 1

    while right_index < len(right_array):
        merged_array.append(right_array[right_index])
        right_index += 1
    return merged_array


def merge_sort(array):
    if not array or len(array) <= 1:
        return array

    left_index = 0
    right_index = len(array)
    middle_index = (left_index + right_index)//2

    left_array = merge_sort(array[left_index:middle_index])
    right_array = merge_sort(array[middle_index:right_index])
    return merge(left_array, right_array)


if __name__ == '__main__':

    array = [5, 6, 8, -4, 0, 50, -9234, 34, 82.3, 101]

    num_array_sorted = merge_sort(array)

    print("Num array sorted:")
    for num in num_array_sorted:
        print(num)
