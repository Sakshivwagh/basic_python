def find_missing_number(arr, n):
    total_sum = 0
    for i in range(1, n + 1):
        total_sum += i  

    arr_sum = 0
    for num in arr:
        arr_sum += num  

    return total_sum - arr_sum  

n = int(input("Enter total numbers: "))
arr = list(map(int, input("Enter the array elements: ").split()))

print("Missing number is:", find_missing_number(arr, n))


Output-
Enter total numbers: 4
Enter the array elements: 1 3 4
Missing number is: 2