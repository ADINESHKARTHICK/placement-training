def searchRange(nums, target):
    def findLeft(nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def findRight(nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return right

    left_index = findLeft(nums, target)
    right_index = findRight(nums, target)

    if left_index <= right_index and left_index < len(nums) and nums[left_index] == target and nums[right_index] == target:
        return [left_index, right_index]
    else:
        return [-1, -1]
print(searchRange(nums, target))  # Output: [3, 4]
