def binary_search(nums_array, num):
	lo = 0
	hi = len(nums_array)
	passos = 0
	while lo < hi:
		passos +=1
		mid = int((lo+hi)/2)
		if nums_array[mid] == num:
			print(f"passos {passos}")
			return mid
		elif nums_array[mid] < num:
			lo = mid + 1
		else:
			hi = mid
	return -1
a = [1,2,3,4,5,6,7,8,9,10]
binary_search(a,3)