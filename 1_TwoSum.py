# Решение задачи two_sum

def twoSum(self, nums: List[int], target: int) -> List[int]:
	lst_range = len(nums)
		for i in range(0, lst_range-1):
			for j in range(i+1, lst_range):
				if nums[i] + nums[j] == target:
					return [i,j]  
