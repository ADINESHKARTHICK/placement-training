def subarray_sum(nums, k):
    count = 0
    cum_sum = 0
    sum_dict = {0: 1}
    for num in nums:
        cum_sum += num
        if cum_sum - k in sum_dict:
            count += sum_dict[cum_sum - k]
        sum_dict[cum_sum] = sum_dict.get(cum_sum, 0) + 1
    return count
print(subarray_sum([1, 1, 1], 2))  
