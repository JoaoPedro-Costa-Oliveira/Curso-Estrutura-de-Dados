def bubble(nums):
    size = len(nums)
    for _ in nums:
        print(nums)
        for i in range(size-1):
            if nums[i] > nums[i+1]:
                nums[i+1], nums[i] = nums[i],nums[i+1]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        print(arr)
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

bubble([5,4,3,2,1])
print("--"*10)
bubble_sort([5,4,3,2,1])