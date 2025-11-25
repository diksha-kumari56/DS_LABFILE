def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


try:
    n = int(input("Enter number of elements: "))

    arr = list(map(int, input("Enter elements separated by space: ").split()))

    if len(arr) != n:
        print("❌ Error: You must enter exactly", n, "numbers.")
    else:
        print("Sorted array:", merge_sort(arr))

except ValueError:
    print("❌ Error: Please enter integer values only.")


