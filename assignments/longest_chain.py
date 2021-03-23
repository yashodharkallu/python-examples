def longestConsecutive(nums):
    longest_streak = 0

    for num in nums:
        current_num = num
        current_streak = 1

        while current_num + 1 in nums:
            current_num += 1
            current_streak += 1

        longest_streak = max(longest_streak, current_streak)

    return longest_streak

print(longestConsecutive([100,4,200,1,3,2]))