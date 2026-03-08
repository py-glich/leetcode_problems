class Solution:
    def twoSum(self, nums, target):
        hashmap = {}

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in hashmap:
                return [hashmap[complement], i]

            hashmap[nums[i]] = i


nums = [6,11,7,2]
target = 9

obj = Solution()
result = obj.twoSum(nums, target)

print(result)