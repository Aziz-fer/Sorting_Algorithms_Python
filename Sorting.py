import random
def counting_sort(arr):
    # Determine the range of values in the array
    max_val = max(arr)
    min_val = min(arr)
    range_val = max_val - min_val + 1

    # Create a counting array to store the frequency of each value
    count = [0] * range_val

    # Count the frequency of each value in the array
    for i in arr:
        count[i - min_val] += 1

    # Calculate the starting index for each value
    for i in range(1, range_val):
        count[i] += count[i-1]

    # Create the output array
    output = [0] * len(arr)

    # Build the output array
    for i in reversed(arr):
        output[count[i - min_val] - 1] = i
        count[i - min_val] -= 1

    return output


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def main():
    arr = [random.randint(0, 100) for _ in range(10)]
    print("Original array: ", arr)
    algorithm = input("Enter sorting algorithm (counting/merge): ")
    if algorithm == "counting":
        sorted_arr = counting_sort(arr)
    elif algorithm == "merge":
        sorted_arr = merge_sort(arr)
    print("Sorted array: ", sorted_arr)

if __name__ == "__main__":
    main()