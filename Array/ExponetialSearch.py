def binary_search(nums_array, num, lo, hi):
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
	
	
def exonetial_search(array, target):
			if array[0] == target:
					return 0
			n = len(array)
			i = 1
			
			while i < n and array[i] < target:
					i *= 2
			
			if array[i] == target:
					return 1
					
			return binary_search(array, target, i//2, min (i,n-2))
	
arr= [1, 2, 3,4 ,5 ,6 ,7 ,8 ,9 ,10 ,11 ,12 ,13 ,14 ,15 ,16 ,17 ,18 ,19 ,20 ,21 ,22 ,23 ,24 ,25 ,26,27 ,28, 29,30, 31 ,32 ,33 ,34 ,35 ,36 ,37 ,38 ,39 ,40]
target  = 32
result = exonetial_search(arr,target)
print(f"Elemento encontrado no index {result}")
