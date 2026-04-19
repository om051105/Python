"""
nums = [5,6,7,7,1,9,1,1,1,5,1,1]

freq_map = {}

for i in range(len(nums)):
    if nums[i] in   freq_map:
        freq_map[nums[i]] += 1
    else:
        freq_map[nums[i]] = 1

print(freq_map)
"""

nums = [5,6,7,7,1,9,1,1,1,5,1,1]

freq_map = {}

for num in nums:
    if num in freq_map:
        freq_map[num] += 1
    else:
        freq_map[num] = 1

print(freq_map)