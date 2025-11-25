arr = []

print("Enter 10 Numbers: ")
for i in range(10):
    num = int(input())
    arr.append(num)

num_to_search = int(input("\nEnter a Number to Search: "))

index = -1
for i in range(10):
    if arr[i] == num_to_search:
        index = i
        break

print("\nFound at Index No.", index)
