def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]       
        j = i - 1        

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

n = int(input("Enter size of array: "))

arr = []
print("Enter elements:")
for _ in range(n):
    arr.append(int(input()))

insertion_sort(arr)

print("Sorted array:")
for x in arr:
    print(x, end=" ")
